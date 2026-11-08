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

    def test_homepages_cover_all_cases_without_turning_links_into_previews(self):
        from showcase import render_homepages, resolve_showcase
        from build import CATEGORIES
        previews=json.loads((ROOT/'data/showcase.json').read_text(encoding='utf8'))
        covers=resolve_showcase(self.history,previews)
        for language,name in [('zh','README.md'),('en','README.en.md')]:
            page=render_homepages(self.cases,self.sources,self.history,previews,CATEGORIES,language)[Path(name)]
            for case in self.cases:
                self.assertEqual(1,page.count(f'id="case-{case["id"]}"'))
            for category in {c['category'] for c in self.cases}:
                section=page.split(f'<a id="category-{category}"></a>',1)[1].split('<a id="category-',1)[0]
                folded=section.find('<summary>Awaiting previews' if language=='en' else '<summary>待补效果')
                for case in (c for c in self.cases if c['category']==category):
                    position=section.index(f'id="case-{case["id"]}"')
                    if case['id'] in covers:self.assertTrue(folded<0 or position<folded)
                    else:self.assertGreater(position,folded)

    def test_showcase_rejects_wrong_case_or_unlicensed_media(self):
        from showcase import check_showcase
        previews=json.loads((ROOT/'data/showcase.json').read_text(encoding='utf8'))
        self.assertEqual([],check_showcase(self.cases,self.history,previews,ROOT))
        bad=deepcopy(previews)
        bad[0]['case_id']='svg-001'
        self.assertTrue(any('mismatched' in e for e in check_showcase(self.cases,self.history,bad,ROOT)))
        bad=deepcopy(previews)
        remote=next(p for p in bad if 'image_url' in p)
        remote['rights']='link_only'
        self.assertTrue(any('license' in e for e in check_showcase(self.cases,self.history,bad,ROOT)))

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

    def test_history_and_gallery_have_bilingual_navigation(self):
        for language,base,switch in [('zh',Path('docs'),'en/'),('en',Path('docs/en'),'../')]:
            pages=render_history(self.cases,self.history,language)
            for name in ('HISTORY.md','GALLERY.md'):
                self.assertIn(f'({switch}{name})',pages[base/name])
            gallery=pages[base/'GALLERY.md']
            for record in self.history:
                if record.get('preview'):
                    self.assertIn(record['preview'],gallery)
                    self.assertIn(record['source_url'],gallery)

if __name__=='__main__':unittest.main()
