#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zapise novy kalk do kalky.md i calques.json naraz.

Dokument a JSON musi mit stejne klice, jinak test i check.py spadnou. Skript
proto zapisuje na obe mista najednou a regex predtim overi proti ukazkove vete
(--probe) i protiprikladu (--counter).

Pouziti:
  python add_calque.py --key "výhoda spočívá v ceně" \\
      --en "the advantage lies in" --fix "výhodou je cena" \\
      --rx '\\bvýhod\\w*\\s+spočív\\w+' \\
      --probe "Výhoda spočívá v ceně." --counter "Klíč spočívá v zámku."

  --lang sk zapisuje do slovenskeho seznamu.
"""
import argparse
import json
import os
import re
import sys

# Konzole na Windows je cp1250 a znak ✓ v ni neexistuje: bez tohohle by skript
# spadl az na zaverecnem printu, kdyz uz ma oba soubory zapsane.
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, 'reconfigure'):
        _s.reconfigure(encoding='utf-8')

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
README = os.path.join(DATA, '..', '..', '..', 'README.md')

# Radek s poctem kalku v tabulce README. Bez prepisu se pocet tise rozesel
# s daty (stalo se: 65 v README, 119 v datech).
README_ROWS = {'cs': 'české kalky', 'sk': 'slovenské kalky'}

# Zaverecna veta (kotva) je v kazdem dokumentu v jeho jazyce. Nova odrazka se
# vklada pred ni.
TAILS = {
    'cs': 'Seznam doplňuj, jakmile na další kalk narazíš.',
    'sk': 'Zoznam doplňuj, jakmile na další kalk narazíš.',
}

ap = argparse.ArgumentParser()
for f in ('key', 'en', 'fix', 'rx', 'probe'):
    ap.add_argument('--' + f, required=True)
ap.add_argument('--counter', help='věta, kterou regex chytit NESMÍ (piš vždy)')
ap.add_argument('--lang', default='cs', choices=sorted(TAILS))
a = ap.parse_args()

KALKY_MD = os.path.join(DATA, a.lang, 'kalky.md')
CALQUES = os.path.join(DATA, a.lang, 'calques.json')
TAIL = TAILS[a.lang]

if '"' in a.key:
    sys.exit('ERROR: klíč nesmí obsahovat rovnou uvozovku "')
try:
    rx = re.compile(a.rx, re.I)
except re.error as e:
    sys.exit('ERROR: nevalidní regex: %s' % e)
if not rx.search(a.probe):
    sys.exit('ERROR: regex nechytil ukázkovou větu, oprav regex nebo větu')
if a.counter and rx.search(a.counter):
    sys.exit('ERROR: regex chytil protipříklad, je moc široký')

with open(KALKY_MD, encoding='utf-8') as f:
    md = f.read()
with open(CALQUES, encoding='utf-8') as f:
    data = json.load(f)
if any(c['key'] == a.key for c in data['calques']):
    sys.exit('ERROR: „%s" už v seznamu je' % a.key)
if TAIL not in md:
    sys.exit('ERROR: v %s chybí kotva „%s"' % (KALKY_MD, TAIL))

bullet = '- „%s" (z „%s") → **„%s"**\n\n' % (a.key, a.en, a.fix)
with open(KALKY_MD, 'w', encoding='utf-8', newline='\n') as f:
    f.write(md.replace(TAIL, bullet + TAIL, 1))

entry = {'key': a.key, 'rx': a.rx, 'label': '%s (%s)' % (a.key, a.en), 'probe': a.probe}
if a.counter:
    entry['counter'] = a.counter
data['calques'].append(entry)
with open(CALQUES, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

if os.path.exists(README):
    with open(README, encoding='utf-8') as f:
        readme = f.read()
    row = re.compile(r'^(\| %s \| )\d+( \|)$' % re.escape(README_ROWS[a.lang]), re.M)
    readme = row.sub(lambda m: '%s%d%s' % (m.group(1), len(data['calques']), m.group(2)), readme, count=1)
    with open(README, 'w', encoding='utf-8', newline='\n') as f:
        f.write(readme)

print('✓ [%s] zapsáno do kalky.md i calques.json: „%s"' % (a.lang, a.key))
print('  Ověř: python -m unittest discover tests  (v kořeni repa)')
