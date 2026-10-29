# Kalky

Seznam kalků z angličtiny, bohemizmů ve slovenštině a obratů, po kterých
text zní jako AI. Ke každé chybě přirozená náhrada a regex, který ji v textu
najde.

Vznikl při redakční práci pro různé weby. Texty tam vznikají s pomocí AI a kalky jsou nejčastější chyba, kterou jazykový
model do češtiny zanese: „uvnitř sedí čip", „výhoda leží v ceně", „ceny
startují na 269 dolarech". Gramaticky je to správně, česky to nezní.

| | |
|---|---|
| české kalky | 135 |
| slovenské kalky | 26 |
| bohemizmy | 31 |
| AI obraty | 8 (posuzují se čtením, strojově jen antiteze) |

Každé pravidlo má větu, kterou regex musí chytit, a většinou i protipříklad,
který chytit nesmí. Test to ověřuje u každé změny, takže seznam může růst
z příspěvků a nerozbije se.

## Použití s agentem

**Claude Code** si repo nainstaluje jako plugin:

```
/plugin marketplace add zdenekdvorak-linki/kalky
/plugin install kalky@kalky
```

Claude pak skill použije sám, když píšete nebo kontrolujete český či
slovenský text.

**Aplikace Claude (claude.ai, desktop):** zabalte složku
[`skills/kalky`](skills/kalky) do ZIPu a nahrajte ji v nastavení aplikace
mezi skilly.

**OpenAI Codex** a další agenti se standardem Agent Skills: zkopírujte
složku `skills/kalky` mezi své skilly.

**ChatGPT a ostatní chaty:** pošlete agentovi odkaz na repo a napište mu,
ať se řídí souborem [`AGENTS.md`](AGENTS.md). Data si stáhne sám.

## Použití z příkazové řádky

Stačí Python 3.9 nebo novější, žádné balíčky:

```bash
python skills/kalky/scripts/check.py clanek.md
python skills/kalky/scripts/check.py --lang sk clanok.md
python skills/kalky/scripts/check.py --json clanek.md
```

```
Kalky (2):
  - „Uvnitř sedí"  →  „uvnitř najdete X" / „základem je X" / „Provoz zajišťuje X"
  - „ceny startují na"  →  „ceny začínají na 269 dolarech / pořídíte od 269 dolarů"

VERDIKT: K OPRAVĚ
```

Návratový kód 0 znamená čistý text, 1 nálezy, 2 rozbitá data.

## Co v repu je

| Cesta | Obsah |
|---|---|
| [`skills/kalky/data/cs/kalky.md`](skills/kalky/data/cs/kalky.md) | české kalky, čitelné pro lidi |
| [`skills/kalky/data/cs/calques.json`](skills/kalky/data/cs/calques.json) | regexy ke kalkům, obecný vzor a antiteze |
| [`skills/kalky/data/sk/`](skills/kalky/data/sk) | slovenské kalky a bohemizmy |
| [`skills/kalky/data/ai-obraty.md`](skills/kalky/data/ai-obraty.md) | obraty, podle kterých čtenář pozná text od AI |
| [`skills/kalky/scripts/check.py`](skills/kalky/scripts/check.py) | kontrola textu |
| [`skills/kalky/scripts/add_calque.py`](skills/kalky/scripts/add_calque.py) | zápis nového kalku |
| [`AGENTS.md`](AGENTS.md) | pokyny pro agenty: použití a návrh nového kalku |
| [`llms.txt`](llms.txt) | rozcestník pro jazykové modely |

Kromě konkrétních kalků hledá `check.py` i obecný vzor: abstraktní podmět
s fyzickým slovesem („problém leží jinde", „úspora stojí na bonusu"). Chytí
tak i kalky, které v seznamu ještě nejsou, ale hlásí je jen jako varování,
protože se občas spustí i nad správnou větou.

Jako varování hlásí i hromadění vět, které začínají „Tento/Tato/Toto", tedy
doslovný převod anglického „This model…". Jedna taková věta nevadí, `check.py`
se ozve až od tří v jednom textu.

## Jak přispět

Narazili jste na kalk, který v seznamu chybí? Pošlete pull request, nebo
vyplňte [formulář](../../issues/new?template=novy-kalk.yml). Agent vám ho umí
předvyplnit. Podrobnosti v [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licence

- Kód (`scripts/`, `tests/`): [MIT](LICENSE)
- Data: [CC BY 4.0](LICENSE-DATA.md), při použití uveďte zdroj s odkazem na
  tohle repo.
- Bohemizmy převzaté z [kuzmany/slovak-humanizer](https://github.com/kuzmany/slovak-humanizer):
  MIT, © 2026 Zdeno Kuzmany.

## Příbuzné projekty

- [kuzmany/slovak-humanizer](https://github.com/kuzmany/slovak-humanizer):
  slovenský humanizer AI textu, zdroj bohemizmů.
- [nowork-ai/anti-ai-slop-cz](https://github.com/nowork-ai/anti-ai-slop-cz):
  české vzorce AI textu od Filipa Dřímalky.

## Autor

Zdeněk Dvořák, [Linki.cz](https://linki.cz/). SEO a nástroje pro práci
s obsahem. Chyba nebo nápad: [zdenek@linki.cz](mailto:zdenek@linki.cz).

---

*English: a curated list of English calques in Czech and Slovak, Czech
interference in Slovak, and AI-writing tells, each with a regex, a test
sentence and a natural replacement. Usable as a Claude Code plugin, an Agent
Skill, or a plain Python checker. Contributions welcome via PR or issue form.*
