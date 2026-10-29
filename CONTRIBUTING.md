# Jak přispět

Návrhy přijímám od lidí i od agentů. Každý nový kalk musí mít větu, kterou
regex chytí, a protipříklad, který chytit nesmí. Test na GitHubu obojí ověří
u každého pull requestu, takže o obsahu pak rozhoduju jen já, technickou
správnost hlídá stroj.

## Co do seznamu patří

- **Kalk:** anglická vazba přeložená doslova, která česky nebo slovensky zní
  nepřirozeně, i když je gramaticky správně („uvnitř sedí čip").
- **Bohemizmus:** české slovo nebo tvar ve slovenském textu („tlačítko"
  místo „tlačidlo").

Nepatří sem stylová pravidla jednoho webu (zákaz „my", délka perexu), běžné
anglicismy, které čeština přijala („paywall" je v pořádku, „placená zeď"
ne), ani překlepy.

## Pull request

1. Forkni repo a založ větev.
2. Kalk zapiš skriptem, ručně do dokumentu ani JSONu nesahej:

   ```bash
   python skills/kalky/scripts/add_calque.py --key "výhoda spočívá v ceně" \
     --en "the advantage lies in" --fix "výhodou je cena" \
     --rx '\bvýhod\w*\s+spočív\w+' \
     --probe "Hlavní výhoda spočívá v ceně." --counter "Klíč spočívá v zámku."
   ```

   Slovenský kalk s `--lang sk`. Bohemizmus přidej rovnou do
   `skills/kalky/data/sk/bohemismy.json` s poli `rx`, `fix` a `probe`; hledá
   se bez ignorování velikosti písmen, varianty piš do regexu (`[Tt]ady`).
3. Spusť testy:

   ```bash
   python -m unittest discover tests
   ```

4. Otevři pull request a napiš, v jakém textu jsi na kalk narazil.

## Jak psát regex

- Začni hranicí slova `\b`, jinak regex chytí i konec jiného slova.
- Chytej kmen, ne jeden tvar: `\bspočív\w+` pokryje „spočívá" i „spočívala".
- Hledá se bez ohledu na velikost písmen.
- Protipříklad vybírej tak, aby se od kalku lišil co nejméně: stejné sloveso
  v doslovném významu („Kabel leží v krabici." proti „Výhoda leží v ceně.").

## Issue bez Gitu

Formulář [Nový kalk](../../issues/new?template=novy-kalk.yml) stačí vyplnit.
Chatový agent ho umí předvyplnit, postup je v [`AGENTS.md`](AGENTS.md).
