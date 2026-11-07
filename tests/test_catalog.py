import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import check_data

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases=json.loads((ROOT/'data/cases.json').read_text(encoding='utf8'))
        cls.sources=json.loads((ROOT/'data/sources.json').read_text(encoding='utf8'))

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

if __name__=='__main__':unittest.main()
