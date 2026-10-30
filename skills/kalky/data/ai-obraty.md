# Obraty, po kterých text okamžitě zní jako AI

Obraty, které jazykový model produkuje sám od sebe a kterých si čtenář všimne
dřív než čehokoli jiného. Platí pro jakýkoli český text, ať ho píše člověk,
nebo model, stejně jako seznam kalků v `cs/kalky.md`.

Strojově se z toho kontroluje jen antiteze (`scripts/check.py`). Zbytek musí
odchytit člověk nebo model při čtení, proto si těmito body projdi text zvlášť, než ho
odevzdáš.

## 1. Zmizelý konatel na začátku věty

Věta popisuje děj, který se odehrál sám od sebe, a člověk z ní zmizel.

- ✗ „Do jednoho týdenního seznamu se vešla korektura rozhovoru a překlad katalogu."
- ✓ „Minulý týden jsem zvládl korekturu rozhovoru a překlad katalogu."

Platí to dvojnásob pro **první větu perexu** a pro **první větu každé sekce**.
Tam je zmizelý konatel nejvíc vidět a čtenář podle něj pozná strojový text
během vteřiny. Souvisí to s pravidlem o nominální stavbě, ale je to širší:
netýká se jen zpodstatnělého děje jako podmětu, ale každé bezpodměté vazby
typu „vešlo se", „podařilo se", „ukázalo se" na exponovaném místě.

## 2. Aforistická trojice bez slovesa

Tři členy, rytmus, žádné sloveso. Zní to chytře a nesdělí to nic, co by v textu
nebylo.

- ✗ „Sedm dní, osm klientů, jedna společná linka."
- ✗ „Faktické chyby, stavba vět, typografie."
- ✓ „Hledal jsem faktické nepřesnosti, kostrbaté věty a chyby v typografii."

Ozdobnou trojici škrtni celou. Věcnému výčtu dej sloveso a konatele. Výjimkou
je výčet, který popisuje pořadí nebo parametry, kde by sloveso překáželo
(„Na mobilu jiné pořadí: nadpis, datum, obrázek, tlačítko.").

## 3. Text, který si sám vysvětluje, co je na něm zajímavé

Autor čtenáři sděluje, co si má myslet, místo aby mu tu věc ukázal.

- ✗ „Zajímavější než každá z těch věcí zvlášť je jejich rozptyl."
- ✗ „Cenné bylo, co druhý model našel v tom prvním."
- ✗ „Nejde o úsporu hodiny měsíčně. Jde o to, že…"
- ✓ Ukaž tu věc a nech závěr na čtenáři.

Poznávací znamení: „zajímavé je", „podstatné je", „cenné bylo", „nejdůležitější
není", „nejde o X, jde o Y", „když se na to podíváme zpětně". Když chceš
navázat, oslov čtenáře přímo: „Zajímají vás detaily? Tady jsou."

## 4. Antiteze „A, ne B" (ZÁKAZ)

Konstrukce „potvrzení + negace protikladu" typu „Placení je volba, ne
podmínka." nebo „Rozhoduje uživatel, ne algoritmus." Je to nejoblíbenější
obrat jazykových modelů a text po něm zní strojově okamžitě.

Zákaz platí i pro rozvolněné varianty, které strojová kontrola nechytí:

- ✗ „Nešlo o výměnu, ale o srovnání."
- ✗ „Překlad tu neznamená záměnu slov."

Default je běžná oznamovací věta. Kontroluje `scripts/check.py`, přepínač
`--antithesis-max` (výchozí 0 = zákaz).

## 5. Nedoložený dovětek k doloženému faktu

Věta začne pravdivým jádrem a skončí soudem, který nikdo neřekl a nikde nestojí.

- ✗ „Zabralo mi to hodinu měsíčně **a nikomu to nic nepřineslo**."
- ✓ „Zabralo mi to hodinu měsíčně."

Doložená je první polovina. Druhá vznikla proto, že věta potřebovala pointu.
Je to **halucinace v miniatuře**: model si nevymyslí číslo ani událost, protože
ty jdou ověřit, ale vymyslí si hodnocení, které zní jako autorský postoj. Ověří
se hůř a čtenáře zavede stejně spolehlivě. V citovaném případě navíc nebyl jen
nedoložený, ale i nepravdivý — ta práce výsledek měla.

Odlišuj od bodu 3. Tam jde o nadbytečné vysvětlování něčeho pravdivého, tady o
tvrzení, které se nestalo.

**Kde vzniká nejčastěji:**

| Tvar | Příklad |
| --- | --- |
| absolutní soud | „nikomu", „nikdy", „vůbec", „k ničemu", „zbytečně" |
| kvantifikace od oka | „stovky notifikací", „za dvacet minut", „odkládal jsem to roky" |
| následek za „takže" | „otravovalo mě to, **takže v tom bývaly chyby**" |
| spekulace o minulosti | „**dřív** bych na to sháněl kolegu **celé dny**" |

**Pravidlo:** každý údaj a každý soud musí mít oporu ve zdroji, ze kterého text
vzniká — v podkladu, v zadání, v tom, co autor řekl. Když oporu nenajdeš,
tvrzení **vypusť**. Nepřepisuj ho do opatrnější formulace, protože opatrně
podaný výmysl je pořád výmysl.

**Když si myslíš, že to pravda je, ale nemáš doklad**, napiš to autorovi do
shrnutí místo do článku. Když to pravda je, vrátí ti to sám.

Kandidáty umí vypsat skript, rozhodnout ale musí člověk: sémantiku regex
neověří.

## 6. Vymyšlená motivace autora

Nejnebezpečnější podtyp bodu 5, a proto stojí zvlášť. Text tvrdí, **proč** autor
něco udělal, co si u toho myslel nebo jak se cítil.

- ✗ „Ani jeden z těch kroků jsem neplánoval jako investici do automatizace.
  Všechny vznikly z podráždění, že něco dělám podruhé."
- ✓ „Ptám se na to u každé zakázky: co z téhle práce může převzít AI?"

Ta špatná verze je doložený případ. Skutečnost byla **přesně opačná** — autor
u každé práce systematicky hledá, co může převzít AI. Text z něj udělal
někoho, kdo automatizuje nahodile z frustrace.

**Proč je to horší než ostatní výmysly:**

- Zdroj pravdy motivaci nikdy neobsahuje. Podklad zaznamenává, **co** autor
  řekl, ne **proč**. Nedá se tedy ověřit, jen vypustit nebo se zeptat.
- Zní to jako autorský vhled, takže působí věrohodněji než vymyšlené číslo.
- Když se model splete, plete se rád **o sto osmdesát stupňů**, protože sahá po
  té psychologicky líbivější variantě. Náhodné podráždění je „lepší příběh" než
  metodická práce, ale je to lež o člověku, pod kterým je text podepsaný.

**Pravidlo:** o motivaci, pocitech a úmyslech autora piš **jen to, co sám
řekl**. Jinak popiš, co se stalo, a proč nech být. Zvlášť pozor na pointy
odstavců a na závěr článku — tam se vymyšlená motivace usazuje nejčastěji,
protože text v tu chvíli hledá vyústění.

Pozor na hraniční případy: „šli jsme vědomě proti číslům" **je** v pořádku,
když autor v podkladu řekl „nám to nevadí, chceme uživatele na téhle stránce".
Doložený úmysl je fakt jako každý jiný.

## 7. Reklamní klišé z anglických tiskových zpráv

Obraty, které model přebírá z anglické tiskové zprávy a které v české větě
nic neříkají. Napiš místo nich, co se konkrétně změnilo.

- ✗ „Nový hardware mění pravidla hry." (z „a game changer")
- ✗ „S Qi2 jsou kabely minulostí." (z „cables are a thing of the past")
- ✓ „Nabíječka Qi2 nabíjí bezdrátově rychlostí 15 W, kabel už nepotřebujete."

## 8. Střídání synonym místo názvu

Model se bojí zopakovat název, a tak z reproduktoru udělá „krychli", ze
čtečky „stroj" a z vysavače „kousek". Čtenář pak tápe, jestli jde pořád o
tutéž věc. Zopakuj název nebo druh přístroje, případně použij zájmeno.

- ✗ „BADKRUKA je černá krychle… Kolik krychle dá watů, IKEA neuvádí."
- ✓ „BADKRUKA je černý reproduktor… Kolik dá watů, IKEA neuvádí."

## 9. Autor obhajuje vlastní číslo

Model vytuší, že údaj může vypadat vycucaný z prstu, a předřadí mu obhajobu
proti námitce, kterou čtenář nevyslovil. Věta pak nenese fakt, jen nejistotu
pisatele. Rovnou napiš, z čeho číslo vychází; obhajoba zmizí sama.

- ✗ „Osm hodin denně jsem nevzal od stropu." (navíc kalk z „off the top of my head")
- ✗ „Nejde o náhodné číslo." / „To si nevymýšlím."
- ✓ „Osm hodin denně beru proto, že přístroj nejede pořád."

Je to blízký příbuzný bodu 3: tam text vysvětluje, co je na něm zajímavé,
tady vysvětluje, proč mu máte věřit. Obojí je řeč o textu místo textu.

## Změny & rozhodnutí

| datum | co | proč |
| --- | --- | --- |
| 2026-10-30 | Přidán bod 9 (autor obhajuje vlastní číslo) | Úprava uživatele v draftu GeekLife 25134: škrtl „Osm hodin denně jsem nevzal od stropu." V témže článku označil dalších pět vazeb, kde neživá věc dostala lidské sloveso (hodnota povyleze, vývod sedí, sloupec nese, krabice radí); dvě z nich odešly jako kalky do cs/kalky.md, zbytek je stylová preference GeekLife. |
| 2026-10-29 | Přidány body 7 (klišé z tiskových zpráv) a 8 (střídání synonym místo názvu) | Porovnání prvních a finálních revizí 174 redakčních článků: redakce smazala „kabely jsou minulostí", čtyřikrát přepsala „krychli" a třikrát „stroj" na název přístroje; „mění pravidla hry" jen zmírnila na „chce měnit". |
| 2026-08-27 | Přidán bod 6 o vymyšlené motivaci | Text tvrdil, že autor automatizuje neplánovaně „z podráždění". Skutečnost byla opačná: dělá to systematicky u každé zakázky. Vymyšlená motivace se od ostatních výmyslů liší tím, že ji zdroj pravdy nikdy neobsahuje a že se model plete rád o 180 stupňů — sáhne po líbivějším příběhu. |
| 2026-08-27 | Přidán bod 5 o nedoloženém dovětku | Autor nachytal větu „Zabralo mi to hodinu měsíčně a nikomu to nic nepřineslo." První půlka pravda, druhá vymyšlená. V témže článku se našlo dalších devět nedoložených tvrzení, takže nešlo o výjimku. |
| 2026-08-27 | Dokument založen; antiteze zpřísněna z „max 1x" na zákaz na všech webech | Autor obraty nachytal v perexu prvního AI deníčku, všechny čtyři najednou, a k antitezi řekl výslovně „nesnáším je". Pravidlo o antitezi do té doby žilo ve třech kopiích, po jedné pro každý web, které se mohly rozejít. |
