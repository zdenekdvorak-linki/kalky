# Pokyny pro agenty

Tenhle repozitář je seznam kalků z angličtiny, bohemizmů ve slovenštině a
obratů, po kterých text zní jako AI. Každý agent ho může používat při psaní
a kontrole textu a každý může navrhnout nový kalk. Platí pro Claude, ChatGPT,
Codex, Cursor i jakéhokoli jiného agenta.

## Použití

Celý postup je ve skillu [`skills/kalky/SKILL.md`](skills/kalky/SKILL.md).
Zkráceně:

- **Umíš spustit Python 3.9+:** `python skills/kalky/scripts/check.py text.md`
  (slovenština `--lang sk`, strojový výstup `--json`, text ze stdin `-`).
- **Neumíš spouštět kód:** stáhni si surová data a projdi text proti nim.

| Data | Surová URL |
|---|---|
| české kalky | https://raw.githubusercontent.com/zdenekdvorak-linki/kalky/main/skills/kalky/data/cs/kalky.md |
| slovenské kalky | https://raw.githubusercontent.com/zdenekdvorak-linki/kalky/main/skills/kalky/data/sk/kalky.md |
| bohemizmy | https://raw.githubusercontent.com/zdenekdvorak-linki/kalky/main/skills/kalky/data/sk/bohemismy.json |
| AI obraty | https://raw.githubusercontent.com/zdenekdvorak-linki/kalky/main/skills/kalky/data/ai-obraty.md |

Každá odrážka v `kalky.md` má tvar `- „kalk" (z „anglický originál") → **„náhrada"**`.

## Návrh nového kalku

Do seznamu patří vazba, která je kalkem v každém kontextu. Stylová preference
jednoho webu nebo redakce do něj nepatří. Než kalk navrhneš, ověř v
`kalky.md`, že tam ještě není.

Potřebuješ:

| Pole | Příklad |
|---|---|
| kalk | `výhoda spočívá v ceně` |
| anglický originál | `the advantage lies in` |
| náhrada | `výhodou je cena` |
| věta, kterou regex chytí | `Hlavní výhoda spočívá v ceně.` |
| protipříklad, který chytit nesmí | `Klíč spočívá v zámku.` |
| regex (nepovinný) | `\bvýhod\w*\s+spočív\w+` |

### Agent s přístupem ke Gitu

1. Forkni repo a založ větev.
2. Zapiš kalk skriptem, ne ručně (dokument a JSON se musí shodovat):

   ```bash
   python skills/kalky/scripts/add_calque.py --key "výhoda spočívá v ceně" \
     --en "the advantage lies in" --fix "výhodou je cena" \
     --rx '\bvýhod\w*\s+spočív\w+' \
     --probe "Hlavní výhoda spočívá v ceně." --counter "Klíč spočívá v zámku."
   ```

   Pro slovenštinu přidej `--lang sk`. Bohemizmus zapiš rovnou do
   `skills/kalky/data/sk/bohemismy.json` (pole `rx`, `fix`, `probe`).
3. Spusť `python -m unittest discover tests`. Musí projít.
4. Otevři pull request. Do popisu napiš, v jakém textu jsi kalk potkal.

### Chatový agent bez Gitu

Sestav uživateli odkaz na předvyplněné issue a nech ho odeslat jedním klikem.
Hodnoty zakóduj pro URL (mezera `%20`, uvozovky a diakritika přes
percent-encoding):

```
https://github.com/zdenekdvorak-linki/kalky/issues/new?template=novy-kalk.yml&title=Nový%20kalk:%20<kalk>&jazyk=<cs|sk>&kalk=<kalk>&original=<anglický originál>&oprava=<náhrada>&veta=<věta>&protipriklad=<protipříklad>&regex=<regex>
```

Odkaz uživateli ukaž a řekni mu, že issue se odešle až jeho kliknutím na
„Submit new issue".
