#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Najde v textu kalky, bohemizmy a antitezi „A, ne B".

    python check.py clanek.md                # cestina
    python check.py --lang sk clanok.md      # slovencina (vcetne bohemizmu)
    cat clanek.md | python check.py -        # text ze stdin
    python check.py --json clanek.md         # strojovy vystup pro agenty
    python check.py --selftest               # overi data, nic nekontroluje

Navratove kody: 0 = nic nenalezeno, 1 = nalezy, 2 = rozbita data nebo vstup.

Jen standardni knihovna, bezi na Pythonu 3.9 a novejsim.
"""
import argparse
import json
import os
import re
import sys

for _s in (sys.stdin, sys.stdout, sys.stderr):
    if hasattr(_s, 'reconfigure'):
        _s.reconfigure(encoding='utf-8')  # konzole na Windows je cp1250

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
LANGS = ('cs', 'sk')

# Odrazka v kalky.md: - „klic" (z „anglicky original") → **„oprava"** ...
# Zaviraci uvozovka u klice je rovna ("), tak ji zapisuje add_calque.py.
KEY_RX = re.compile('^- „([^"]+)"', re.M)
BULLET_RX = re.compile('^- „([^"]+)".*?→\\s*\\*\\*(.+?)\\*\\*', re.M)


class DataError(Exception):
    pass


def load(lang):
    """Nacte data jazyka a overi je. Pri nesouladu vyhodi DataError."""
    base = os.path.join(DATA, lang)
    with open(os.path.join(base, 'calques.json'), encoding='utf-8') as f:
        data = json.load(f)
    with open(os.path.join(base, 'kalky.md'), encoding='utf-8') as f:
        md = f.read()

    md_keys = KEY_RX.findall(md)
    json_keys = [c['key'] for c in data['calques']]
    missing = [k for k in md_keys if k not in json_keys]
    extra = [k for k in json_keys if k not in md_keys]
    if missing or extra:
        raise DataError('%s: kalky.md a calques.json nesedí (bez regexu: %s; bez odrážky: %s)'
                        % (lang, missing, extra))
    fixes = dict(BULLET_RX.findall(md))
    for c in data['calques']:
        c['fix'] = fixes.get(c['key'], '').strip()
        if not re.search(c['rx'], c['probe'], re.I):
            raise DataError('%s: regex „%s" nechytil vlastní ukázkovou větu' % (lang, c['key']))
        if c.get('counter') and re.search(c['rx'], c['counter'], re.I):
            raise DataError('%s: regex „%s" chytil protipříklad' % (lang, c['key']))
    dem = data.get('demonstrative')
    if dem and (not re.search(dem['rx'], dem['probe']) or re.search(dem['rx'], dem['counter'])):
        raise DataError('%s: regex ukazovacích zájmen nesedí s probe/counter' % lang)

    data['bohemisms'] = []
    boh_path = os.path.join(base, 'bohemismy.json')
    if os.path.exists(boh_path):
        with open(boh_path, encoding='utf-8') as f:
            data['bohemisms'] = json.load(f)['bohemisms']
        for b in data['bohemisms']:
            # bez re.I: viz _comment v bohemismy.json
            if not re.search(b['rx'], b['probe']):
                raise DataError('%s: bohemizmus „%s" nechytil vlastní ukázkovou větu' % (lang, b['rx']))
    return data


def prepare(text):
    """Vyhodi bloky kodu; nadpisy, odrazky i tabulky zustanou, kalk je chyba vsude."""
    return re.sub(r'^\s*```.*?^\s*```[^\n]*$', '', text, flags=re.M | re.S)


def check(text, data, antithesis_max=0):
    text = prepare(text)
    flat = ' '.join(l.strip() for l in text.split('\n') if l.strip())
    res = {'calques': [], 'bohemisms': [], 'antithesis': [], 'generic': [], 'demonstrative': []}

    for c in data['calques']:
        for m in re.finditer(c['rx'], flat, re.I):
            res['calques'].append({'key': c['key'], 'match': m.group(0).strip(),
                                   'label': c['label'], 'fix': c['fix']})

    for b in data['bohemisms']:
        for m in re.finditer(b['rx'], flat):
            res['bohemisms'].append({'match': m.group(0).strip(), 'fix': b['fix']})

    anti = [m.group(0).strip() for m in re.finditer(data['antithesis']['rx'], flat)]
    if len(anti) > antithesis_max:
        res['antithesis'] = anti

    # Zobecneny vzor jen varuje: chyta i kalky, ktere v seznamu jeste nejsou,
    # za cenu falesnych poplachu. Shody uz evidovanych kalku se nehlasi dvakrat.
    g = data['generic']
    gen_rx = r'\b(%s)\w*\s+(\w+\s+){0,2}(%s)\w*' % (g['abstract'], g['verbs'])
    seen = set()
    for m in re.finditer(gen_rx, flat, re.I):
        hit = m.group(0).strip()
        if hit in seen or any(re.search(c['rx'], hit, re.I) for c in data['calques']):
            continue
        seen.add(hit)
        res['generic'].append(hit)

    # Vety zacinajici „Tento/Tato/Toto": vadi az nahromadene, proto se pocitaji
    # na cely text a hlasi se jen nad prahem, jako varovani. Bez re.I.
    dem = data.get('demonstrative')
    if dem:
        hits = [m.group(1).strip() for m in re.finditer(dem['rx'], flat)]
        if len(hits) > dem['max']:
            res['demonstrative'] = hits
    return res


def report(res, data, lang):
    out = []
    if res['calques']:
        out.append('Kalky (%d):' % len(res['calques']))
        for h in res['calques']:
            out.append('  - „%s"  →  %s' % (h['match'], h['fix'] or h['label']))
    if res['bohemisms']:
        out.append('Bohemizmy (%d):' % len(res['bohemisms']))
        for h in res['bohemisms']:
            out.append('  - „%s"  →  %s' % (h['match'], h['fix']))
    if res['antithesis']:
        out.append('%s (%d):' % (data['antithesis']['label'], len(res['antithesis'])))
        for h in res['antithesis']:
            out.append('  - %s' % h)
    if res['generic']:
        out.append('Varování, posuď podle kontextu: %s (%d):'
                   % (data['generic']['label'], len(res['generic'])))
        for h in res['generic']:
            out.append('  - %s' % h)
    if res['demonstrative']:
        dem = data['demonstrative']
        out.append('Varování: %s, %dx (text unese nejvýš %dx); %s:'
                   % (dem['label'], len(res['demonstrative']), dem['max'], dem['fix']))
        for h in res['demonstrative']:
            out.append('  - %s…' % h)
    hard = res['calques'] or res['bohemisms'] or res['antithesis']
    out.append('')
    out.append('VERDIKT: %s' % ('K OPRAVĚ' if hard else 'ČISTÉ'))
    return '\n'.join(out).strip()


def main(argv=None):
    ap = argparse.ArgumentParser(description='Najde kalky, bohemizmy a antitezi v českém nebo slovenském textu.')
    ap.add_argument('path', nargs='?', help='soubor s textem, nebo - pro stdin')
    ap.add_argument('--lang', default='cs', choices=LANGS)
    ap.add_argument('--json', action='store_true', help='výstup jako JSON')
    ap.add_argument('--antithesis-max', type=int, default=0,
                    help='kolik antitezí „A, ne B" je ještě v pořádku (výchozí 0)')
    ap.add_argument('--selftest', action='store_true', help='jen ověří data všech jazyků')
    a = ap.parse_args(argv)

    try:
        if a.selftest:
            for lang in LANGS:
                d = load(lang)
                print('%s: %d kalků, %d bohemizmů, data v pořádku'
                      % (lang, len(d['calques']), len(d['bohemisms'])))
            return 0
        data = load(a.lang)
    except (DataError, OSError, ValueError, KeyError, re.error) as e:
        sys.stderr.write('CHYBA DAT: %s\n' % e)
        return 2

    if not a.path:
        ap.error('chybí soubor (nebo - pro stdin)')
    if a.path == '-':
        text = sys.stdin.read()
    else:
        try:
            with open(a.path, encoding='utf-8') as f:
                text = f.read()
        except OSError as e:
            sys.stderr.write('CHYBA: %s\n' % e)
            return 2

    res = check(text, data, a.antithesis_max)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(report(res, data, a.lang))
    return 1 if (res['calques'] or res['bohemisms'] or res['antithesis']) else 0


if __name__ == '__main__':
    sys.exit(main())
