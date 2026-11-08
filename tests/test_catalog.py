import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import check_data
from build import render
from history import check_history, render_history

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases=json.loads((ROOT/'data/cases.json').read_text(encoding='utf8'))
        cls.sources=json.loads((ROOT/'data/sources.json').read_text(encoding='utf8'))
        cls.history=json.loads((ROOT/'data/history.json').read_text(encoding='utf8'))

    def test_valid_schema(self):
        self.assertEqual([],check_data(self.cases,self.sources))

    def test_source_counts_match_data(self):
        self.assertGreater(len(self.cases), 0)
        for source in self.sources:
            self.assertEqual(source["count"],len([c for c in self.cases if c["source_id"]==source["id"]]))

    def test_mutation_catches_duplicate(self):
        cases=[dict(c) for c in self.cases]
        cases[1]['id']=cases[0]['id']
        self.assertTrue(any('duplicate id' in err for err in check_data(cases,self.sources)))

    def test_all_cases_link_to_original_site(self):
        self.assertTrue(all(c['source_url'].startswith('https://') for c in self.cases))
        self.assertTrue(all(c['prompt_status']=='source_only' for c in self.cases))

    def test_missing_english_description_is_rejected(self):
        cases=[dict(c) for c in self.cases]
        cases[0].pop('summary_en')
        self.assertTrue(any('summary_en' in err for err in check_data(cases,self.sources)))

    def test_translation_count_mismatch_is_rejected(self):
        cases=[dict(c) for c in self.cases]
        cases[0]['checks_en']=cases[0]['checks_en'][:2]
        self.assertTrue(any('translation count mismatch' in err for err in check_data(cases,self.sources)))

    def test_both_indexes_cover_every_case_and_switch_languages(self):
        for language, index_path, switch in [
            ('zh', Path('docs/INDEX.md'), '(en/INDEX.md)'),
            ('en', Path('docs/en/INDEX.md'), '(../INDEX.md)'),
        ]:
            with self.subTest(language=language):
                pages=render(self.cases,self.sources,language)
                index=pages[index_path]
                self.assertEqual(len(pages),6)
                self.assertIn(switch,index)
                for case in self.cases:
                    self.assertEqual(index.count(f'`{case["id"]}`'),1)

    def test_history_covers_every_case_with_valid_provenance(self):
        expected={c['id'] for c in self.cases if c.get('evidence_level') != 'prompt_only'}
        self.assertEqual(expected,{r['case_id'] for r in self.history})
        prompt_only={c['id'] for c in self.cases if c.get('evidence_level') == 'prompt_only'}
        self.assertTrue(all(c['prompt_availability']=='public' for c in self.cases if c['id'] in prompt_only))
        self.assertEqual([],check_history(self.cases,self.history,ROOT))

    def test_research_preserves_discovery_and_rejects_false_promotions(self):
        from research import check_research
        records=json.loads((ROOT/'data/research.json').read_text(encoding='utf8'))
        self.assertEqual([],check_research(self.cases,records))
        bad=deepcopy(records)
        bad[0]['included_case_id']='invented-case'
        self.assertTrue(any('unknown case' in e for e in check_research(self.cases,bad)))

    def test_gallery_groups_related_works_without_losing_catalog_entries(self):
        from showcase import render_homepages
        from site_catalog import render_site_catalog
        from build import CATEGORIES
        previews=json.loads((ROOT/'data/showcase.json').read_text(encoding='utf8'))
        script=render_site_catalog(self.cases,self.sources,self.history,previews)[Path('site/catalog.js')]
        gallery=json.loads(script.split('window.AI_FUN_CATALOG = ',1)[1].strip().removesuffix(';'))
        covered=[v['id'] for work in gallery['works'] for v in (work['variants'] or [work])]
        works=[c for c in self.cases if c.get('evidence_level')!='prompt_only']
        self.assertCountEqual([c['id'] for c in works],covered)
        self.assertEqual(len(self.cases)-len(works),len(gallery['prompts']))
        series=next(w for w in gallery['works'] if w['id']=='svg-001')
        self.assertEqual(30,len(series['variants']))
        prince=next(w for w in gallery['works'] if w['id']=='sac-little-prince')
        self.assertEqual('https://littleprince.dev/',prince['play'])
        for language,name in [('zh','README.zh-CN.md'),('en','README.md')]:
            page=render_homepages(self.cases,self.sources,self.history,previews,CATEGORIES,language)[Path(name)]
            gallery_url='https://java4ye.github.io/awesome-ai-fun/site/' + ('?lang=zh' if language=='zh' else '')
            self.assertIn(gallery_url,page)
            self.assertIn('README.md)' if language=='zh' else 'README.zh-CN.md)',page)
            self.assertEqual(len(gallery['works']),page.count('<td width="33%"'))
            self.assertEqual(sum(bool(w['image']) for w in gallery['works']),page.count('<img '))
            self.assertIn('COLLECTIONS.md#svg-001',page)
            self.assertNotIn('Featured works' if language=='en' else '精选作品',page)

    def test_showcase_rejects_wrong_case_or_unlicensed_media(self):
        from showcase import check_showcase
        previews=json.loads((ROOT/'data/showcase.json').read_text(encoding='utf8'))
        self.assertEqual([],check_showcase(self.cases,self.history,previews,ROOT))
        bad=deepcopy(previews)
        next(p for p in bad if 'history_id' in p)['case_id']='svg-001'
        self.assertTrue(any('mismatched' in e for e in check_showcase(self.cases,self.history,bad,ROOT)))
        bad=deepcopy(previews)
        remote=next(p for p in bad if 'image_url' in p)
        remote['rights']='link_only'
        self.assertTrue(any('license' in e for e in check_showcase(self.cases,self.history,bad,ROOT)))

    def test_source_capture_is_checked_and_not_relicensed(self):
        from showcase import check_showcase
        records=json.loads((ROOT/'data/showcase.json').read_text(encoding='utf8'))
        bad=deepcopy(records)
        capture=next(p for p in bad if p.get('capture'))
        capture['capture_sha256']='0'*64
        self.assertTrue(any('checksum' in e for e in check_showcase(self.cases,self.history,bad,ROOT)))
        bad=deepcopy(records)
        reference=next(p for p in bad if p.get('rights')=='source_reference')
        reference['license_status']='MIT'
        self.assertTrue(any('must not imply' in e for e in check_showcase(self.cases,self.history,bad,ROOT)))

    def test_link_only_media_cannot_become_a_local_preview(self):
        record=deepcopy(next(r for r in self.history if r.get('preview')))
        record['rights']='link_only'
        self.assertTrue(any('redistribution license' in e for e in check_history(self.cases,[record],ROOT)))

    def test_changed_or_mislabelled_preview_is_rejected(self):
        record=deepcopy(next(r for r in self.history if r.get('preview')))
        record['preview_sha256']='0'*64
        record['model']='An unrelated model'
        errors=check_history(self.cases,[record],ROOT)
        self.assertTrue(any('checksum mismatch' in e for e in errors))
        self.assertTrue(any('attribution mismatch' in e for e in errors))

    def test_preview_paths_cannot_escape_repository(self):
        record=deepcopy(next(r for r in self.history if r.get('preview')))
        record['preview']='../outside.jpg'
        self.assertTrue(any('unsafe or missing preview' in e for e in check_history(self.cases,[record],ROOT)))

    def test_history_rejects_unknown_case_and_duplicate_record(self):
        record=deepcopy(self.history[0])
        record['case_id']='not-a-case'
        errors=check_history(self.cases,[record,record],ROOT)
        self.assertTrue(any('unknown case' in e for e in errors))
        self.assertTrue(any('duplicate id' in e for e in errors))

    def test_history_and_category_pages_retain_previews(self):
        from html import escape
        from showcase import resolve_showcase
        previews=json.loads((ROOT/'data/showcase.json').read_text(encoding='utf8'))
        covers=resolve_showcase(self.history,previews)
        for language,base,switch in [('zh',Path('docs'),'en/'),('en',Path('docs/en'),'../')]:
            pages=render_history(self.cases,self.history,language)
            self.assertIn(f'({switch}HISTORY.md)',pages[base/'HISTORY.md'])
            details=render(self.cases,self.sources,language,self.history,previews)
            all_details='\n'.join(text for path,text in details.items() if path.parent.name=='categories')
            for preview in covers.values():
                image=preview.get('preview') or preview.get('capture') or preview.get('image_url')
                self.assertIn(escape(image,quote=True),all_details)
            for record in self.history:
                if record.get('preview'):
                    self.assertIn(record['preview'],all_details)
                    self.assertIn(record['source_url'],all_details)

if __name__=='__main__':unittest.main()
