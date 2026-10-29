# -*- coding: utf-8 -*-
"""Testy dat a checkeru. Spusteni v koreni repa: python -m unittest discover tests"""
import json
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, 'skills', 'kalky')
DATA = os.path.join(SKILL, 'data')
CHECK = os.path.join(SKILL, 'scripts', 'check.py')
sys.path.insert(0, os.path.join(SKILL, 'scripts'))

import check  # noqa: E402


def read_json(*p):
    with open(os.path.join(DATA, *p), encoding='utf-8') as f:
        return json.load(f)


def read(*p):
    with open(os.path.join(DATA, *p), encoding='utf-8') as f:
        return f.read()


class DataTest(unittest.TestCase):

    def test_load_all_languages(self):
        # load() sam overuje shodu md/json, ukazkove vety a protipriklady
        for lang in check.LANGS:
            with self.subTest(lang=lang):
                d = check.load(lang)
                self.assertTrue(d['calques'])

    def test_keys_unique(self):
        for lang in check.LANGS:
            keys = [c['key'] for c in read_json(lang, 'calques.json')['calques']]
            dup = sorted({k for k in keys if keys.count(k) > 1})
            self.assertEqual(dup, [], '%s: duplicitní klíče' % lang)

    def test_required_fields(self):
        for lang in check.LANGS:
            for c in read_json(lang, 'calques.json')['calques']:
                with self.subTest(lang=lang, key=c.get('key')):
                    for f in ('key', 'rx', 'label', 'probe'):
                        self.assertTrue(c.get(f), 'chybí pole %s' % f)
                    re.compile(c['rx'])

    def test_every_bullet_has_fix(self):
        # check.py ukazuje opravu z tucne casti odrazky; bez ni agent nevi, cim kalk nahradit
        for lang in check.LANGS:
            for c in check.load(lang)['calques']:
                with self.subTest(lang=lang, key=c['key']):
                    self.assertTrue(c['fix'], 'odrážka nemá opravu ve tvaru → **„…"**')

    def test_bohemisms(self):
        for b in read_json('sk', 'bohemismy.json')['bohemisms']:
            with self.subTest(rx=b.get('rx')):
                for f in ('rx', 'fix', 'probe'):
                    self.assertTrue(b.get(f), 'chybí pole %s' % f)
                self.assertTrue(re.search(b['rx'], b['probe']))

    def test_czech_proper_names_pass_bohemism_letters(self):
        # ceska vlastni jmena ve slovenskem textu projit maji (regex bez re.I)
        res = check.check('Rozprával Jiří Dvořák z Přerova.', check.load('sk'))
        self.assertEqual(res['bohemisms'], [])

    def test_readme_counts(self):
        # pocty v tabulce README se uz jednou tise rozesly s daty (65 vs 119)
        with open(os.path.join(ROOT, 'README.md'), encoding='utf-8') as f:
            readme = f.read()

        def row(label):
            m = re.search(r'^\| %s \| (\d+)' % re.escape(label), readme, re.M)
            self.assertTrue(m, 'README nemá řádek „%s"' % label)
            return int(m.group(1))

        self.assertEqual(row('české kalky'), len(read_json('cs', 'calques.json')['calques']))
        self.assertEqual(row('slovenské kalky'), len(read_json('sk', 'calques.json')['calques']))
        self.assertEqual(row('bohemizmy'), len(read_json('sk', 'bohemismy.json')['bohemisms']))
        self.assertEqual(row('AI obraty'), len(re.findall(r'^## \d+\.', read('ai-obraty.md'), re.M)))

    def test_json_format(self):
        # jednotny format = citelne diffy v PR
        for p in (('cs', 'calques.json'), ('sk', 'calques.json'), ('sk', 'bohemismy.json')):
            raw = read(*p)
            want = json.dumps(json.loads(raw), ensure_ascii=False, indent=2) + '\n'
            self.assertEqual(raw, want, '%s: přeformátuj JSON (indent 2, ensure_ascii=False, LF)' % '/'.join(p))


class CheckTest(unittest.TestCase):

    def run_cli(self, args, stdin=None):
        p = subprocess.run([sys.executable, CHECK] + args, input=stdin,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True, encoding='utf-8')
        return p.returncode, p.stdout

    def test_finds_calque(self):
        code, out = self.run_cli(['-'], 'Uvnitř sedí čip Snapdragon.')
        self.assertEqual(code, 1)
        self.assertIn('Uvnitř sedí', out)
        self.assertIn('K OPRAVĚ', out)

    def test_clean_text(self):
        code, out = self.run_cli(['-'], 'Uvnitř najdete čip Snapdragon a baterii na dva dny.')
        self.assertEqual(code, 0)
        self.assertIn('ČISTÉ', out)

    def test_counter_examples_are_clean(self):
        d = check.load('cs')
        for c in d['calques']:
            if c.get('counter'):
                with self.subTest(key=c['key']):
                    hits = [h['key'] for h in check.check(c['counter'], d)['calques']]
                    self.assertNotIn(c['key'], hits)

    def test_antithesis(self):
        code, out = self.run_cli(['-'], 'Rozhoduje uživatel, ne algoritmus.')
        self.assertEqual(code, 1)
        code, _ = self.run_cli(['--antithesis-max', '1', '-'], 'Rozhoduje uživatel, ne algoritmus.')
        self.assertEqual(code, 0)

    def test_slovak_bohemism(self):
        code, out = self.run_cli(['--lang', 'sk', '-'], 'Stlačte tlačítko na boku.')
        self.assertEqual(code, 1)
        self.assertIn('tlačidlo', out)

    def test_json_output(self):
        code, out = self.run_cli(['--json', '-'], 'Výhoda leží v ceně.')
        self.assertEqual(code, 1)
        res = json.loads(out)
        self.assertEqual(set(res), {'calques', 'bohemisms', 'antithesis', 'generic', 'demonstrative'})
        self.assertTrue(res['calques'][0]['fix'])

    def test_demonstratives_warn_from_three(self):
        d = check.load('cs')
        two = 'Tento model je malý. Tato baterie vydrží týden.'
        self.assertEqual(check.check(two, d)['demonstrative'], [])
        three = two + ' Toto řešení je levné.'
        self.assertEqual(len(check.check(three, d)['demonstrative']), 3)
        # jen varovani: verdikt zustava cisty, navratovy kod 0
        code, out = self.run_cli(['-'], three)
        self.assertEqual(code, 0)
        self.assertIn('Tento/Tato/Toto', out)
        self.assertIn('ČISTÉ', out)

    def test_demonstratives_only_at_sentence_start(self):
        d = check.load('cs')
        text = 'V tento den. Na toto téma. Pro tyto lidi. A tento model taky.'
        self.assertEqual(check.check(text, d)['demonstrative'], [])

    def test_code_blocks_ignored(self):
        code, _ = self.run_cli(['-'], '```\nUvnitř sedí čip.\n```\nText bez chyb.')
        self.assertEqual(code, 0)

    def test_selftest(self):
        code, out = self.run_cli(['--selftest'])
        self.assertEqual(code, 0)
        self.assertIn('data v pořádku', out)


if __name__ == '__main__':
    unittest.main()
