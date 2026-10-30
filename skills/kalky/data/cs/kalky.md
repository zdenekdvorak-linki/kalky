# Anglicismy a kalky v češtině

Seznam kalků, tedy doslovně přeložených anglických vazeb, které zní česky
nepřirozeně, i když jsou gramaticky správně. Vznikl při redakční práci pro
různé weby a roste z každého textu, ve kterém nějaký kalk najdeme.

Ke každé odrážce patří regex v `calques.json` ve stejné složce. Test v repu
hlídá, že dokument a JSON mají stejné klíče a že každý regex chytí svou
ukázkovou větu a mine protipříklad.

**Nový kalk přidávej skriptem `scripts/add_calque.py`**, ne ruční editací.
Zapisuje do obou souborů naráz a regex předtím ověří.

## Anglicismy a kalky (vyhýbat se)

Nepřekládej anglické vazby doslova. Kalk zní česky nepřirozeně, i když je gramaticky správný. Když píšeš obrat, který ti „zní povědomě z angličtiny", ověř, jestli není doslovný převod.

- „běžet před realitou" (z „to run ahead of") → **„předbíhat realitu"**
- „uvnitř sedí / nesedí X" / „uvnitř pracuje X" (z „inside sits/works") → **„uvnitř najdete X" / „základem je X" / „Provoz zajišťuje X"**. Pozn.: „článek" ve významu „galvanický článek" (baterie) zní krkolomně a plete se s „článkem na webu" — piš „baterie" / „akumulátor".
- „žene text enginem" (z „to drive/run through") → **„pohání ho"**
- „zařízení odpovídá majiteli" (z „answers to") → **„patří majiteli"**
- „nese krytí / rating" (z „to carry a rating") → **„má krytí" / „je odolné podle"**
- „nad displejem / nad hardwarem běží software" (z „runs on top of / atop") → **„základem softwaru je X" / „X pohání zařízení"**
- „ovladač nese tlačítka" / „čepičky nesou symboly" / „tělo nese port" (z „to carry / to bear / to feature") → **„na ovladači jsou tlačítka" / „na čepičkách jsou symboly" / „na těle najdete port"**. Věc pasivně „nenese" své součásti ani popisky, prostě je má nebo na ní jsou.
- „reakce na pohyb běží mimo aplikaci" / „automatika běží i bez internetu" (z „to run") → **„na pohyb reaguje i bez aplikace" / „automatika funguje i bez internetu"**. Sloveso „běžet" si nech pro procesy a programy, funkce zařízení prostě fungují nebo reagují.
- „nejnižší stupeň sedne k posteli" / „varianta sedne do malého bytu" (z „to fit / to sit well") → **„hodí se k posteli" / „hodí se do malého bytu"**. „Sednout" ve významu „vyhovovat" je hovorové a nepřesné, „hodit se" je jednoznačné.
- „peníze leží v sadách" / „výhoda leží v ceně" / „problém leží jinde" (z „the money lies in / to lie in") → **„nejvíc ušetříte na sadách" / „výhodou je cena" / „problém je jinde"**. Abstraktní věc v češtině nikde neleží, prostě někde je, nebo ji rovnou popíšeš slovesem.
- „skutečné peníze najdete v balení" / „velké peníze jsou v příslušenství" (z „the real money is in") → **„skutečnou úsporu najdete s příslušenstvím"**. Stejná anglická figura jako u „leží": v české větě pojmenuj rovnou to, o co jde (úspora, rozdíl, cena), ne „peníze" jako abstraktní entitu.
- „mechanika stojí na jednoduchém pravidle" / „hlavní úspora stojí na bonusu" (z „to rest on / to be built on") → **„akce funguje s jednoduchým pravidlem" / „hlavní úsporu přináší bonus"**. Popiš, co věc dělá, místo aby na něčem stála.
- „nejhlubší škrt" / „hluboká sleva" (z „deep cut / deep discount") → **„nejvyšší sleva"**. Sleva se v češtině měří výškou, ne hloubkou. U cenových akcí piš rovnou „sleva", slovo „škrt" si nech pro rozpočty.

- „přínos spočívá v ceně" (z „the benefit lies in") → **„hlavní je cena"**

- „kategorie nese 30 % tržeb" (z „to carry a share") → **„kategorie má 30 % tržeb"**

- „článek slib nedoručí" (z „to deliver on a promise") → **„článek slib nesplní"**

- „přesně ta výměna, kterou popisuje" (z „trade-off") → **„přesně ten kompromis, který popisuje"**

- „autor drží podíl na 5 %" (z „to hold a share at") → **„autor má podíl 5 %"**

- „kde to sedí konkrétně" (z „where it sits") → **„kde je problém konkrétně"**

- „motor ztráty důvěry" (z „the driver of") → **„zdroj ztráty důvěry"**

- „placená zeď" (z „paywall") → **„paywall"**

- „Google začal tlačit články publiku" (z „to push content to") → **„Google začal články ukazovat publiku"**

- „per-článkový test" (z „per-article") → **„test na úrovni jednotlivých článků"**

- „propad sazby" (z „a drop in the rate") → **„propad proklikovosti"**

- „napříč vším" (z „across everything") → **„u všech"**

- „propad se otevřel" (z „the gap opened") → **„propad začal"**

- „časování jednoduchý práh nepodporuje" (z „the timing does not support") → **„časování jednoduchému prahu neodpovídá"**

- „hype slovník" (z „hype vocabulary") → **„nafouknutý slovník"**

- „je předmětem otevřené otázky" (z „is subject to an open question") → **„zůstává otevřená otázka"**

- „jít o X Kč níž / dolů (o ceně)" (z „prices go down by X") → **„být o X Kč levnější / stát o X Kč míň / zlevnit o X Kč"**

- „je fér přiznat / říct" (z „it's fair to say / admit") → **„je třeba přiznat; musím přiznat"**

- „web stojí vedle firemního" (z „to stand next to / to sit alongside") → **„mám dva weby / vedle firemního mám ještě osobní"**

- „rovnou z krabice" (z „out of the box") → **„rovnou od výroby / už z výroby / předinstalovaný"**

- „křemík ve významu čip" (z „the same silicon") → **„čip / procesor"**

- „v/pod/za X sedí komponenta" (z „the module houses / a sensor sits inside") → **„je / je uvnitř / obsahuje (napiš rovnou, co tam je)"**

- „ceny startují na X (prices start at X)" (z „prices start at $269") → **„ceny začínají na 269 dolarech / pořídíte od 269 dolarů"**

- „štědrá výbava/paměť (generous specs)" (z „a generous set of specs") → **„bohatá výbava, nadstandardní výbava"**

- „signál/síť bojuje s X" (z „the signal struggles/battles with X") → **„rušení signál oslabuje / signál je oslabený"**

- „obsah kreslí/vykresluje X PPI" (z „text/type renders at X PPI") → **„displej vykresluje písmo v ostrosti X PPI (nebo: písmo má rozlišení X PPI)"**

- „obrazovka spánku" (z „sleep screen") → **„obrázek po uspání / spořič, který čtečka ukáže po uspání"**

- „navrchu / vzadu sedí komponenta" (z „the button sits on top") → **„v horní části najdete / je umístěné"**

- „vrstvu vyhazuje ven / drops the layer" (z „drops/throws out the layer") → **„je bez X / vynechává X (neživotná věc nemůže vyhazovat)"**

- „drží (nižší|vyšší) cenu / holds a lower price" (z „holds a lower/higher price") → **„má cenu / nabízí cenu (drží se u ceny, ne cenu)"**

- „chodit-do-vyhledavace" (z „to go into search / to go to the search engine") → **„ve vyhledávači nemá co dělat / nemá se dostat do vyhledávání"**

- „poháněný modelem / AI" (z „powered by (model / AI)") → **„využívá model X / běží na modelu X"**

- „přemosťuje do X (bridges into X)" (z „bridges into Matter / bridges devices into the network") → **„propojí s X, pustí do X, začlení do sítě X"**

- „tlačítko / konektor sedí na hraně" (z „the button sits on the bottom edge") → **„tlačítko je na spodní straně"**

- „překládá na X (translates to X)" (z „which the manufacturer translates to 90 days") → **„což podle výrobce odpovídá 90 dnům"**

- „držet jednotný design / styl" (z „to hold / keep a consistent design") → **„sjednotit design / zachovat jednotný styl"**

- „za zlomek času" (z „in a fraction of the time") → **„mnohem rychleji, za pár minut místo hodin"**

- „ceny začínají na X" (z „prices start at X") → **„nejlevnější verze stojí X / ceny začínají od X"**

- „objednávky startují / spouští (datum)" (z „orders start / open on (date)") → **„objednat půjde od…, prodej začíná…"**

- „rozdat internet / Wi-Fi" (z „hand out internet / give out Wi-Fi") → **„připojit k internetu, sdílet připojení"**



- „svítí N nitů" (z „shines / glows at N nits") → **„jas displeje dosahuje 3 000 nitů; displej má jas 3 000 nitů"**

- „displej svítí (= má podsvícení)" (z „the display glows / lights up") → **„displej má podsvícení / přední světlo"**

- „nejschopnější model" (z „our most capable model") → **„nejvýkonnější model"**

- „jezdí na baterii" (z „runs on a battery") → **„napájí ji baterie AA / funguje na baterii AA"**

- „poslat do prodeje" (z „to send to market / ship to") → **„začít prodávat / uvést na trh / začne prodávat v Evropě"**

- „vede skladem" (z „carries in stock") → **„má skladem"**

- „cena nekončí" (z „the price doesn't end there") → **„cenou náklady nekončí"**

- „nabít z kabelu" (z „charge from a cable") → **„nabíjet kabelem / přes kabel"**

- „nejvíc peněz rozhoduje" (z „what decides the most money") → **„největší vliv na cenu má"**

- „rozměry mohou rozhodnout" (z „size can make the difference") → **„mohou mít vliv"**

- „přístroj vyfoukne prach" (z „the device blows out / emits dust") → **„pustí zpátky do místnosti / propustí (filtrem) / vypustí"**

- „pracovat vzdáleně" (z „to work remotely") → **„pracovat na dálku / z domova"**

- „naše expertíza (ve významu odbornost)" (z „our expertise") → **„naše odbornost / znalosti / zkušenosti"**

- „evidence ukazuje (ve významu důkazy)" (z „the evidence shows / suggests") → **„důkazy ukazují / data naznačují"**

- „cestovní mapa (projektu, reformy)" (z „road map") → **„plán / harmonogram"**

- „vitální role / součást" (z „vital role / part") → **„zásadní role / součást"**

- „přístroj míří na náročné posluchače" (z „is aimed at / targets") → **„je určený pro náročné posluchače / hodí se pro"**

- „klíčové je vědět" (z „it's key to (know)") → **„důležité je vědět / zásadní je"**

- „zvukový zážitek" (z „audio / listening experience") → **„zvuk / poslech"**

- „jazyk prostředí pokrývá angličtinu" (z „covers English and German") → **„umí anglicky a německy / nabízí angličtinu a němčinu"**

- „jede na Matteru" (z „runs on Matter / Thread") → **„funguje přes Matter / komunikuje přes Thread"**

- „je relevantní pro" (z „is relevant for") → **„hodí se pro / týká se"**

- „získává na významu / získává využití" (z „gains importance / gains wider use") → **„je stále důležitější / najde širší uplatnění"**

- „větší sourozenec (o modelu)" (z „bigger / pricier sibling") → **„větší model / dražší varianta téže řady"**

- „audio společník" (z „audio / travel companion") → **„pojmenuj přístroj: sluchátka, reproduktor, čtečka"**

- „32 GB tvoří strop" (z „is the ceiling / cap") → **„maximum je 32 GB / víc paměti nemá"**

- „čísla sedí (= vyplatí se)" (z „the numbers add up") → **„vyplatí se / dává ekonomický smysl"**

- „přináší pohodlí" (z „brings convenience / peace of mind") → **„je pohodlnější / nemusíte se bát"**

- „čistý design" (z „clean design / clean lines") → **„jednoduchý vzhled / střídmé tvary"**

- „Uživatelé mohou" (z „users can") → **„jde / dá se / můžete"**

- „následovně (uvozuje výčet)" (z „as follows") → **„takto / dvojtečka"**

- „jsou následující:" (z „are the following") → **„jsou tyto: / jen dvojtečka"**

- „následovný postup / následujícně" (z „the following") → **„tento postup / takto"**

- „eventuálně (= nakonec)" (z „eventually") → **„nakonec / časem"**

- „kontrolovat osvětlení (= ovládat)" (z „to control") → **„ovládat / řídit"**

- „virtuálně žádný (= prakticky)" (z „virtually no / all") → **„prakticky / téměř"**

- „seriózní problém (= vážný)" (z „serious problem") → **„vážný problém"**

- „telefon přichází s (= obsahuje)" (z „comes with") → **„má / obsahuje / v balení je"**

- „Pro otevření souboru, klikněte" (z „To open the file, click") → **„Chcete-li otevřít soubor, klikněte"**

- „mnohem komplexnější (= složitější)" (z „far more complex") → **„mnohem složitější"**

- „shledat jako nemožné" (z „to find it (impossible)") → **„připadalo mi to nemožné / bylo to nemožné"**

- „referovat k" (z „to refer to") → **„odkazovat na"**

- „exekuce kódu" (z „code execution") → **„spuštění kódu / provedení příkazu"**

- „poslední dekáda (= desetiletí)" (z „decade") → **„desetiletí"**

- „adresovat problém" (z „to address an issue") → **„řešit / zabývat se / reagovat na"**

- „dává to logiku" (z „(kontaminace make sense / mít logiku)") → **„má to logiku"**

- „lehký jogurt (= light)" (z „light") → **„nízkotučný / se sníženým obsahem cukru"**

- „subjekt fotografie (= motiv)" (z „subject") → **„motiv / objekt"**

- „ultimátní (= nejlepší)" (z „ultimate") → **„nejlepší / dokonalý / definitivní"**

- „nastavení žijí v souboru" (z „lives in (a file, the cloud)") → **„je uložené v / najdete v"**

- „nákladový motor" (z „cost driver") → **„hlavní položka nákladů / nejvíc peněz jde na"**

- „na denní bázi" (z „on a daily basis") → **„denně / každý týden / pravidelně"**

- „firma je v problémech" (z „to be in trouble") → **„má problémy / je v potížích"**

- „na konci dne (= nakonec)" (z „at the end of the day") → **„nakonec / v konečném důsledku"**

- „Jste si jisti, že chcete" (z „Are you sure you want…?") → **„Opravdu chcete…?"**

- „Přečtěte si více" (z „Read more / Learn more") → **„Další informace / Číst dál"**

- „kruciální" (z „crucial") → **„zásadní / rozhodující"**

- „signaturní design / jídlo" (z „signature (dish, design)") → **„typický / charakteristický / poznávací"**

- „kompetice (= soutěž, konkurence)" (z „competition") → **„soutěž / konkurence"**

- „orchestrovat služby" (z „to orchestrate") → **„řídit / koordinovat / organizovat"**

- „designérská kolaborace" (z „collaboration (brand collab)") → **„spolupráce / společná kolekce"**

- „diseminace výsledků" (z „dissemination") → **„šíření / zveřejnění"**

- „aplikovat na pozici" (z „to apply for a job") → **„ucházet se o místo / poslat přihlášku"**

- „skvělá zkušenost (= zážitek)" (z „a great experience") → **„skvělý zážitek / dojem"**

- „věc je, že" (z „the thing is…") → **„jde o to, že / problém je v tom, že"**

- „je to, co to je" (z „it is what it is") → **„tak to prostě je / nedá se nic dělat"**

- „čelit realitě" (z „to face reality") → **„smířit se s realitou / přijmout skutečnost"**

- „zněl zklamaně" (z „he sounded disappointed") → **„z hlasu bylo slyšet zklamání / působil zklamaně"**

- „kořenové příčiny" (z „root causes") → **„základní příčiny / skutečná příčina"**

- „přinese přidanou hodnotu" (z „adds value / brings added value") → **„užitek / něco navíc (napiš co)"**

- „stále více důležitější" (z „more and more important") → **„stále důležitější"**

- „považovat jako" (z „to consider as") → **„považovat za"**

- „outdoor kamera" (z „outdoor camera / activities") → **„venkovní kamera / venkovní aktivity"**

- „patetický (= ubohý)" (z „pathetic") → **„ubohý / žalostný / mizerný"**

- „kid-friendly / pet-friendly" (z „kid-friendly, pet-friendly, eco-friendly") → **„vhodný pro děti / pro zvířata / šetrný k přírodě"**

- „must-have doplněk" (z „a must-have") → **„nezbytný / povinná výbava"**

- „chill-out zóna" (z „chill-out zone") → **„odpočinková zóna / koutek na odpočinek"**

- „adults only hotel" (z „adults-only hotel") → **„hotel jen pro dospělé"**

- „nosí prokliky / návštěvnost" (z „to bring clicks / traffic") → **„posílá, přivádí, získává"**

- „dá Androidu displej (aplikace dá zařízení vzhled/funkci)" (z „gives Android a display / gives your phone a look") → **„napodobí na Androidu displej; Android s ní vypadá jako…; přidá do telefonu funkci"**

- „přepínač čeká v nastavení (funkce čeká v menu)" (z „the most important switch awaits in the settings") → **„najdete v nastavení; je v nastavení"**

- „dole leží číselník (prvek rozhraní leží/sedí)" (z „the keypad sits / lies at the bottom") → **„dole najdete číselník; dole je číselník; dole se nachází"**

- „vývod sedí nízko u země" (z „the outlet sits low to the ground") → **„vývod je nízko u země"**

- „sloupec nese štítkovou kapacitu" (z „the column carries the rated capacity") → **„sloupec uvádí štítkovou kapacitu"**

Seznam doplňuj, jakmile na další kalk narazíš.
