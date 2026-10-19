"""Hyggehond — productdata, margecalculatie en Shopify-CSV-export.

Gebruik:  python3 webshop/data/producten.py
Genereert:
  webshop/03-productlijst.md            (calculatietabel)
  webshop/05-teksten/productteksten.md  (unieke productteksten)
  webshop/data/shopify-producten.csv    (Shopify-import, status = draft)

Alle inkoopprijzen zijn DOELPRIJZEN excl. btw. Vergelijk ze met echte
leveranciersoffertes: ligt een offerte boven 'max. inkoop', dan haalt het
product de 40%-marge niet.
"""
import csv
import os

BTW = 0.21                 # alle hondenaccessoires: 21% (geen 9%-producten in assortiment)
PAY_PCT, PAY_FIX = 0.019, 0.25   # gemengd: iDEAL/Wero, Bancontact, kaart, Klarna
ADMIN_RETOUR = 2.00        # handling per retour
AFSCHRIJVING = 0.20        # deel van inkoop dat bij retour verloren gaat
DOEL_MARGE = 0.40

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

W_MAND = ("Geen speelgoed: controleer de mand regelmatig op beschadigingen en verwijder losse vulling of "
          "draadjes direct. Houd de plastic verpakking buiten bereik van kinderen en dieren (verstikkingsgevaar). "
          "Volg het wasvoorschrift op het label.")
W_TUIG = ("Controleer voor elk gebruik op slijtage, scheurtjes en de werking van sluitingen. Laat je hond nooit "
          "onbeheerd achter met tuig, halsband of lijn om. Niet gebruiken voor klimmen, trekken van lasten of als "
          "veiligheidsgordel. Juiste pasvorm: twee vingers ruimte.")
W_SPEEL = ("Alleen onder toezicht gebruiken. Kies een formaat dat je hond niet in zijn geheel kan doorslikken. "
           "Verwijder beschadigd speelgoed direct. Dit is geen kinderspeelgoed.")
W_BAK = ("Reinig na elk gebruik. Keramiek is breekbaar: niet meer gebruiken bij barsten of scherpe randen. "
         "Niet geschikt voor de magnetron tenzij anders vermeld.")
W_AUTO = ("Vervangt geen crashgeteste bench of goedgekeurd veiligheidssysteem. Gebruik altijd in combinatie met "
          "een veiligheidsgordel-adapter of tuig. Laat je hond nooit alleen achter in de auto.")
W_VERZ = ("Niet gebruiken op wonden, ontstoken of geïrriteerde huid. Buiten bereik van kinderen bewaren.")

# Elk product: handle, titel, collectie, gewicht(g), retour%, waarschuwing, varianten [(naam, inkoop, verzend, prijs)],
# intro, voordelen, specs, faq, foto-checklist-extra
P = []
def prod(**k): P.append(k)

prod(handle="orthopedische-hondenmand-rust", titel="Orthopedische hondenmand Rust", collectie="Rust & slapen",
     gram=[2500, 3800, 5200], retour=0.08, w=W_MAND,
     var=[("S – 70 x 50 cm", 24, 7.95, 74.95), ("M – 90 x 65 cm", 32, 9.50, 94.95), ("L – 110 x 80 cm", 42, 11.50, 119.95)],
     intro="Een mand waarin je hond echt tot rust komt. De kern van traagschuim vormt zich naar het lichaam en verdeelt het gewicht gelijkmatig. Fijn voor oudere honden, grote rassen en iedere hond die graag languit ligt.",
     voordelen=["Traagschuim kern die niet uitzakt", "Afneembare bouclé hoes, wasbaar op 30 °C", "Antislip onderkant: blijft liggen op laminaat en tegels", "Lage instap, makkelijk voor stijve gewrichten"],
     specs=["Kern: traagschuim (memory foam), ca. 8 cm", "Hoes: polyester bouclé, rits", "Onderkant: antislip, waterafstotend", "Kleur: warm zand"],
     faq=[("Welke maat heeft mijn hond nodig?", "Meet je hond van neus tot staartaanzet als hij ligt en tel daar 15–20 cm bij op. Twijfel je tussen twee maten, kies dan de grotere."),
          ("Kan de kern in de wasmachine?", "Nee, alleen de hoes. De kern kun je luchten en met een vochtige doek schoonmaken."),
          ("Is dit een medisch product?", "Nee. De mand is ontworpen voor comfort en ondersteuning, maar vervangt geen advies van je dierenarts.")])

prod(handle="donutmand-nest", titel="Donutmand Nest", collectie="Rust & slapen",
     gram=[1200, 1800, 2600], retour=0.06, w=W_MAND,
     var=[("S – Ø 50 cm", 14, 6.95, 47.95), ("M – Ø 70 cm", 19, 7.95, 59.95), ("L – Ø 90 cm", 26, 9.50, 79.95)],
     intro="Voor honden die zich graag oprollen. De verhoogde rand geeft steun aan kop en nek en zorgt voor een geborgen gevoel. Ideaal voor de bank-liefhebbers en onrustige slapers.",
     voordelen=["Hoge, zachte rand als hoofdsteun", "Superzacht teddy-materiaal", "Volledig wasbaar op 30 °C", "Antislip bodem"],
     specs=["Materiaal: polyester teddy-pluche", "Vulling: holle vezel", "Kleur: crème of steengrijs"],
     faq=[("Gaat de vulling klonteren na het wassen?", "Was op 30 °C met een lage centrifuge en schud de mand goed op tijdens het drogen. Niet in de droger."),
          ("Welke maat?", "Meet je hond opgerold van neus tot staartaanzet en kies een diameter die 10–15 cm groter is.")])

prod(handle="hondenplaid-teddy-waterafstotend", titel="Hondenplaid Teddy – waterafstotend", collectie="Rust & slapen",
     gram=[700, 1100], retour=0.04, w=W_MAND,
     var=[("100 x 75 cm", 8, 4.95, 29.95), ("150 x 100 cm", 12, 5.95, 39.95)],
     intro="Bescherm je bank, bed of achterbank zonder in te leveren op stijl. Deze plaid is zacht aan de bovenkant en waterafstotend aan de onderkant, dus natte poten en haren blijven waar ze horen.",
     voordelen=["Waterafstotende tussenlaag", "Zacht teddy-materiaal", "Wasbaar op 30 °C", "Ook fijn in de bench of auto"],
     specs=["Bovenkant: teddy-fleece", "Onderkant: waterafstotende microvezel", "Kleur: zand of mosgroen"],
     faq=[("Is de plaid volledig waterdicht?", "Hij is waterafstotend: morsen en natte poten stoppen. Bij langdurig liggen in een plas kan vocht doordringen.")])

prod(handle="benchkussen-antislip", titel="Benchkussen met antislip", collectie="Rust & slapen",
     gram=[600, 900, 1300], retour=0.06, w=W_MAND,
     var=[("S – 60 x 45 cm", 10, 5.95, 39.95), ("M – 75 x 55 cm", 13, 6.95, 49.95), ("L – 90 x 60 cm", 17, 7.95, 59.95)],
     intro="Een stevig kussen dat precies in de meest gangbare benchmaten past. Maakt van de bench een veilige, comfortabele plek waar je hond graag naartoe gaat.",
     voordelen=["Past in standaard benchmaten", "Antislip bodem, schuift niet", "Hoes wasbaar op 30 °C", "Licht en makkelijk mee te nemen"],
     specs=["Dikte: ca. 5 cm", "Hoes: ribstof polyester", "Kleur: steengrijs"],
     faq=[("Past dit in mijn bench?", "Meet de binnenmaat van je bench. Het kussen mag 1–2 cm kleiner zijn; dan ligt het vlak.")])

prod(handle="autostoel-kleine-hond", titel="Autostoel voor kleine honden", collectie="Op pad",
     gram=[1500], retour=0.07, w=W_AUTO,
     var=[("Universeel – tot 8 kg", 18, 7.95, 59.95)],
     intro="Kleine honden zien graag wat er buiten gebeurt. In deze verhoogde autostoel zit je hond stabiel en comfortabel, met een kort aanlijnkoord dat je aan het tuig vastmaakt.",
     voordelen=["Verhoogde zit: uitzicht en minder wagenziek", "Bevestiging met hoofdsteunband en gordel", "Kort koord voor aan het tuig", "Wasbaar kussen"],
     specs=["Geschikt voor honden tot 8 kg", "Afmeting ca. 45 x 40 x 25 cm", "Materiaal: oxford-polyester met stevige wanden"],
     faq=[("Is deze stoel crashgetest?", "Nee. Hij geeft comfort en stabiliteit maar vervangt geen crashgeteste bench. Maak het koord altijd vast aan een tuig, nooit aan een halsband.")])

prod(handle="autostoelhoes-achterbank", titel="Waterdichte autostoelhoes achterbank", collectie="Op pad",
     gram=[1300], retour=0.05, w=W_AUTO,
     var=[("Universeel", 16, 7.95, 54.95)],
     intro="Na een modderige boswandeling gewoon instappen. Deze hoes beschermt de hele achterbank tegen modder, haren en krassen en is in twee minuten geplaatst.",
     voordelen=["Waterdicht en krasbestendig", "Zijflappen beschermen de portieren", "Gordelopeningen met klittenband", "Afneembaar en wasbaar"],
     specs=["Afmeting ca. 147 x 137 cm", "4-laags oxford met waterdichte coating", "Kleur: antraciet"],
     faq=[("Past de hoes in mijn auto?", "De hoes past op de meeste achterbanken van hatchbacks, sedans en SUV's. Controleer de breedte van je achterbank (ca. 135–150 cm).")])

prod(handle="y-tuig-zacht-gevoerd", titel="Y-tuig zacht gevoerd", collectie="Op pad",
     gram=[150, 180, 220, 280], retour=0.12, w=W_TUIG,
     var=[("XS", 9, 4.95, 34.95), ("S", 9, 4.95, 34.95), ("M", 10, 4.95, 36.95), ("L", 11, 4.95, 39.95)],
     intro="Een Y-tuig laat de schouders vrij bewegen en drukt niet op de keel. Zacht gevoerd, met vier verstelpunten en een stevige handgreep voor als je je hond even dicht bij je wilt houden.",
     voordelen=["Y-vorm: vrije schouderbeweging, geen druk op de keel", "4 verstelpunten voor de perfecte pasvorm", "Reflecterende stiksels", "Handgreep op de rug"],
     specs=["Materiaal: nylon webbing met air-mesh voering", "Aluminium D-ring", "Kleuren: zand, mosgroen, antraciet"],
     faq=[("Hoe meet ik mijn hond?", "Meet de borstomvang achter de voorpoten en de nekomvang. Zie de maattabel; zit je tussen twee maten, kies de grotere en stel strakker af."),
          ("Kan mijn hond eruit glippen?", "Bij de juiste afstelling (twee vingers ruimte) is dat onwaarschijnlijk. Controleer de pasvorm voor elke wandeling.")])

prod(handle="verstelbare-riem-biothane", titel="Verstelbare riem biothane – 2 m", collectie="Op pad",
     gram=[200], retour=0.04, w=W_TUIG,
     var=[("Standaard", 7, 4.95, 27.95)],
     intro="Biothane voelt aan als leer maar is waterdicht, vuilafstotend en vrijwel onverwoestbaar. Met drie lengtes in één riem: kort in de stad, lang in het bos.",
     voordelen=["Waterdicht: na de wandeling afspoelen en klaar", "3 lengtes: 1,2 / 1,6 / 2 m", "Geen nare geur, ook niet na regen", "Stevige karabijnhaak"],
     specs=["Materiaal: biothane (gecoat polyester)", "Breedte 16 mm", "Kleuren: zand, mosgroen, zwart"],
     faq=[("Voor welke honden is deze riem geschikt?", "Voor honden van 5 tot 40 kg. Voor zeer sterke trekkers raden we training en een tuig aan.")])

prod(handle="halsband-biothane", titel="Halsband biothane", collectie="Op pad",
     gram=[80], retour=0.08, w=W_TUIG,
     var=[("S – 25–35 cm", 5, 4.95, 22.95), ("M – 33–45 cm", 5, 4.95, 22.95), ("L – 42–55 cm", 6, 4.95, 24.95)],
     intro="Een halsband die tegen een stootje kan. Biothane droogt direct, blijft soepel en ruikt niet. Matcht met onze biothane riem.",
     voordelen=["Waterdicht en makkelijk schoon", "Roestvrije gesp", "Matcht met de biothane riem", "Licht en soepel"],
     specs=["Materiaal: biothane", "Breedte 19 mm", "Kleuren: zand, mosgroen, zwart"],
     faq=[("Halsband of tuig?", "Voor honden die trekken adviseren we een tuig. Een halsband is fijn voor het penning en rustige wandelingen.")])

prod(handle="regenjas-hond-reflecterend", titel="Regenjas reflecterend", collectie="Op pad",
     gram=[200, 250, 320, 400], retour=0.14, w="Laat je hond niet onbeheerd met de jas aan. Controleer of de jas de bewegingsvrijheid niet beperkt.",
     var=[("S – rug 30 cm", 11, 4.95, 39.95), ("M – rug 40 cm", 12, 4.95, 42.95), ("L – rug 50 cm", 13, 4.95, 44.95), ("XL – rug 60 cm", 14, 4.95, 47.95)],
     intro="Droog thuiskomen na een regenwandeling. Deze lichte regenjas houdt rug en flanken droog en is goed zichtbaar in het donker dankzij reflecterende details.",
     voordelen=["Waterdicht en winddicht", "Reflecterende biezen", "Opening voor tuig of riem", "Opvouwbaar in eigen zakje"],
     specs=["Buitenstof: polyester met waterdichte coating", "Voering: licht mesh", "Kleur: mosgroen"],
     faq=[("Welke maat?", "Meet de rug van nekaanzet tot staartaanzet. Kies de maat die daar het dichtst bij ligt.")])

prod(handle="wandelset-drinkfles-bak", titel="Wandelset drinkfles + opvouwbare bak", collectie="Op pad",
     gram=[350], retour=0.04, w=W_BAK,
     var=[("Standaard", 7, 4.95, 27.95)],
     intro="Altijd vers water bij de hand. De drinkfles met klepbakje is met één hand te gebruiken; de opvouwbare siliconen bak gebruik je voor voer of extra water.",
     voordelen=["Drinkfles 500 ml, lekvrij", "Opvouwbare bak klikt aan je riem", "BPA-vrij", "Vaatwasserbestendig (bak)"],
     specs=["Fles: BPA-vrij kunststof, 500 ml", "Bak: siliconen, 350 ml", "Karabijnhaak inbegrepen"],
     faq=[("Is het geschikt voor de vaatwasser?", "De siliconen bak wel; de fles spoel je met de hand om de afdichting te sparen.")])

prod(handle="poepzakhouder-composteerbaar", titel="Poepzakhouder + 120 composteerbare zakjes", collectie="Op pad",
     gram=[150], retour=0.02, w="Niet geschikt als speelgoed. Zakjes buiten bereik van kinderen bewaren (verstikkingsgevaar).",
     var=[("Standaard", 3.5, 3.50, 19.95)],
     intro="Een nette houder die je aan elke riem klikt, met 8 rollen composteerbare zakjes. Stevig, scheurt niet en ruikt neutraal.",
     voordelen=["Houder van gerecycled materiaal", "120 composteerbare zakjes (8 rollen)", "Clip voor elke riem", "Zakjes makkelijk af te scheuren"],
     specs=["Houder: kunststof met clip", "Zakjes: composteerbaar volgens EN 13432 (certificaat leverancier controleren)"],
     faq=[("Mogen de zakjes in de groenbak?", "Dat verschilt per gemeente; de meeste staan hondenpoep in de gft-bak niet toe. Gooi ze bij twijfel bij het restafval.")])

prod(handle="snoepjestas-wandelen", titel="Snoepjestas voor training", collectie="Op pad",
     gram=[150], retour=0.03, w="Reinig regelmatig. Niet geschikt als speelgoed.",
     var=[("Standaard", 6, 3.95, 22.95)],
     intro="Belonen op het juiste moment is de sleutel van goede training. Deze tas gaat met één hand open en weer dicht, en heeft een vak voor sleutels en zakjes.",
     voordelen=["Magnetische sluiting, met één hand te bedienen", "Afneembare, wasbare binnenvoering", "Riemclip en heupband", "Extra vak voor telefoon en sleutels"],
     specs=["Materiaal: waterafstotend polyester", "Kleur: zand of zwart"],
     faq=[("Kan de tas in de wasmachine?", "De binnenvoering wel op 30 °C; de buitenkant reinig je met een vochtige doek.")])

prod(handle="sleeplijn-biothane-10m", titel="Sleeplijn biothane – 10 m", collectie="Op pad",
     gram=[600], retour=0.04, w=W_TUIG,
     var=[("10 meter", 12, 4.95, 39.95)],
     intro="Vrijheid met controle: een lange lijn voor trainen van de terugroep of wandelen waar loslopen niet mag. Biothane blijft niet aan takken haken en wordt niet zwaar van modder.",
     voordelen=["Waterdicht en vuilafstotend", "Glijdt over gras zonder haken", "Geen brandplekken zoals bij nylon", "Stevige karabijnhaak"],
     specs=["Lengte 10 m, breedte 13 mm", "Materiaal: biothane", "Kleur: neonoranje (goed zichtbaar)"],
     faq=[("Aan tuig of halsband?", "Gebruik een sleeplijn altijd aan een tuig, nooit aan een halsband.")])

prod(handle="slowfeeder-voerbak", titel="Slowfeeder voerbak", collectie="Eten & drinken",
     gram=[400], retour=0.03, w=W_BAK,
     var=[("Standaard – 500 ml", 6, 4.95, 24.95)],
     intro="Voor honden die hun bak in tien seconden leeg hebben. Het doolhofpatroon vertraagt het eten en maakt van elke maaltijd een kleine zoektocht.",
     voordelen=["Vertraagt het eten tot 5x", "Antislip rubber rand", "Vaatwasserbestendig", "Ook geschikt voor natvoer"],
     specs=["Materiaal: BPA-vrij voedselveilig kunststof", "Inhoud ca. 500 ml", "Kleur: zand of salie"],
     faq=[("Helpt dit tegen een opgeblazen maag?", "Langzamer eten wordt vaak aangeraden, maar dit is geen medisch product. Overleg bij klachten met je dierenarts.")])

prod(handle="keramische-voerbak-bamboe", titel="Keramische voerbakken op bamboe standaard", collectie="Eten & drinken",
     gram=[2200], retour=0.06, w=W_BAK,
     var=[("Set van 2 – verhoogd", 14, 7.95, 49.95)],
     intro="Een mooi stuk in je keuken. Twee keramische bakken op een verhoogde bamboe standaard: hygiënisch, zwaar genoeg om niet te schuiven en fijn voor de nek van middelgrote honden.",
     voordelen=["Keramiek: geurloos en makkelijk schoon", "Verhoogd: prettiger eten voor middelgrote honden", "Bamboe standaard met antislip voetjes", "Bakken vaatwasserbestendig"],
     specs=["2 bakken van ca. 600 ml", "Hoogte standaard ca. 10 cm", "Materiaal: keramiek, bamboe"],
     faq=[("Is keramiek voedselveilig?", "Ja, wij vragen de conformiteitsverklaring voor voedselcontact (EU 1935/2004) op bij de leverancier.")])

prod(handle="likmat-set", titel="Likmat set van 2", collectie="Eten & drinken",
     gram=[250], retour=0.02, w=W_SPEEL,
     var=[("Set van 2", 4, 3.95, 17.95)],
     intro="Likken werkt kalmerend. Smeer er wat yoghurt, kwark of natvoer op en je hond is een kwartier zoet. Fijn bij onweer, vuurwerk of als je even rust nodig hebt.",
     voordelen=["Kalmerende bezigheid", "Zuignappen voor op tegels of in bad", "Vaatwasserbestendig", "Ook in de vriezer voor langer plezier"],
     specs=["Materiaal: voedselveilig siliconen", "Afmeting ca. 20 x 20 cm"],
     faq=[("Mag mijn hond erop kauwen?", "Nee, een likmat is geen kauwspeelgoed. Haal de mat weg als je hond gaat bijten.")])

prod(handle="snuffelmat", titel="Snuffelmat", collectie="Spelen & verrijking",
     gram=[500], retour=0.03, w=W_SPEEL,
     var=[("Standaard – 45 x 45 cm", 9, 4.95, 32.95)],
     intro="Tien minuten snuffelen is net zo vermoeiend als een halfuur wandelen. Verstop brokjes in de fleece stroken en laat je hond het werk doen: ideaal voor regenachtige dagen.",
     voordelen=["Hersenwerk: vermoeit op een goede manier", "Vertraagt het eten", "Wasbaar op 30 °C", "Antislip onderkant"],
     specs=["Materiaal: fleece op rubberen basis", "Afmeting ca. 45 x 45 cm"],
     faq=[("Mijn hond trekt de stroken eruit, wat nu?", "Gebruik de mat altijd onder toezicht en ruim hem op na gebruik.")])

prod(handle="puzzelspeelgoed-niveau-2", titel="Puzzelspeelgoed niveau 2", collectie="Spelen & verrijking",
     gram=[600], retour=0.03, w=W_SPEEL,
     var=[("Standaard", 8, 4.95, 29.95)],
     intro="Schuiven, draaien en optillen: deze puzzel daagt je hond uit om zijn snoepjes te verdienen. Niveau 2 is geschikt voor honden die een simpele snuffelmat al snel doorhebben.",
     voordelen=["Drie soorten puzzelstukjes", "Antislip rubberen voetjes", "Makkelijk schoon te maken", "Bouwt zelfvertrouwen op"],
     specs=["Materiaal: BPA-vrij kunststof", "Afmeting ca. 30 x 30 cm"],
     faq=[("Mijn hond snapt het niet, wat nu?", "Begin met de vakjes open en help de eerste keren. Na een paar sessies hebben de meeste honden het door.")])

prod(handle="touwspeelgoed-set-katoen", titel="Touwspeelgoed set katoen (3-delig)", collectie="Spelen & verrijking",
     gram=[350], retour=0.02, w=W_SPEEL,
     var=[("Set van 3", 5, 3.95, 19.95)],
     intro="Drie touwen van onbehandeld katoen voor trekspelletjes, apporteren en kauwen. In rustige kleuren die mooi blijven in je woonkamer.",
     voordelen=["Onbehandeld katoen", "Drie vormen: knoop, ring en trektouw", "Helpt bij het schoonhouden van tanden", "Wasbaar op 30 °C"],
     specs=["Materiaal: 100% katoen", "Lengte ca. 25–40 cm"],
     faq=[("Is dit geschikt voor harde kauwers?", "Voor fanatieke kauwers raden we de natuurrubber kauwbal aan; touw kan dan rafelen.")])

prod(handle="kauwbal-natuurrubber", titel="Kauwbal natuurrubber", collectie="Spelen & verrijking",
     gram=[200, 300], retour=0.02, w=W_SPEEL,
     var=[("M – Ø 6 cm", 5, 3.95, 19.95), ("L – Ø 8 cm", 6, 3.95, 22.95)],
     intro="Stevig, stuiterend en vulbaar met snoepjes of pindakaas. Natuurrubber is zacht voor het gebit en houdt het lang vol.",
     voordelen=["Natuurrubber, stevig en flexibel", "Vulbaar met snacks", "Onvoorspelbaar stuiteren", "Vaatwasserbestendig"],
     specs=["Materiaal: natuurrubber", "Kleur: zand"],
     faq=[("Welke maat?", "Kies altijd een bal die niet in de bek van je hond past. Twijfel je, neem dan L.")])

prod(handle="deshedding-borstel", titel="Deshedding borstel", collectie="Verzorging",
     gram=[200], retour=0.03, w=W_VERZ,
     var=[("Standaard", 6, 3.95, 24.95)],
     intro="Minder haren op de bank. Deze borstel verwijdert losse ondervacht zonder de bovenvacht te beschadigen, met een knop om het haar in één keer los te laten.",
     voordelen=["Verwijdert losse ondervacht", "Zelfreinigende knop", "Ergonomische greep", "Voor middellange en lange vachten"],
     specs=["Kam: roestvrij staal", "Greep: antislip"],
     faq=[("Hoe vaak borstelen?", "In de verharingsperiode 2–3 keer per week, kort en zonder hard te drukken.")])

prod(handle="pootreiniger", titel="Pootreiniger", collectie="Verzorging",
     gram=[300], retour=0.03, w=W_VERZ,
     var=[("M", 5, 4.95, 22.95), ("L", 6, 4.95, 24.95)],
     intro="Modderpoten? Vul de beker met wat lauw water, draai een paar keer en dep na met een handdoek. Je vloer blijft schoon.",
     voordelen=["Zachte siliconen borstels", "Makkelijk mee te nemen in de auto", "Vaatwasserbestendig (borstelinzet)", "In twee maten"],
     specs=["Materiaal: kunststof beker met siliconen inzet", "M: kleine en middelgrote honden · L: grote honden"],
     faq=[("Welke maat?", "Past de poot met wat ruimte in een gewone mok, dan is M goed. Anders L.")])

prod(handle="hondenbadjas-microvezel", titel="Hondenbadjas microvezel", collectie="Verzorging",
     gram=[300, 400, 500], retour=0.10, w="Laat je hond niet onbeheerd met de badjas aan.",
     var=[("S", 9, 4.95, 34.95), ("M", 10, 4.95, 36.95), ("L", 11, 4.95, 39.95)],
     intro="Na het zwemmen, de regen of het badje: trek de badjas aan en je hond droogt zichzelf terwijl hij uitrust. Microvezel neemt veel vocht op en droogt snel.",
     voordelen=["Absorbeert tot 5x zijn gewicht", "Klittenband aan buik en nek", "Capuchon voor de kop", "Wasbaar op 40 °C"],
     specs=["Materiaal: microvezel", "Kleur: zand"],
     faq=[("Hoe lang moet mijn hond hem dragen?", "10–20 minuten is meestal genoeg. Daarna kun je eventueel nog nadrogen met een handdoek.")])

prod(handle="speelgoedmand-vilt", titel="Speelgoedmand vilt", collectie="Thuis",
     gram=[600], retour=0.03, w="Geen speelgoed. Plastic verpakking buiten bereik van kinderen en dieren houden.",
     var=[("Standaard – Ø 35 cm", 9, 6.95, 34.95)],
     intro="Alle speeltjes op één plek, en een mooi accent in je interieur. Stevig vilt dat zijn vorm houdt, met handgrepen.",
     voordelen=["Stevig vilt, houdt zijn vorm", "Handgrepen", "Opvouwbaar voor opslag", "Ook voor plaids en riemen"],
     specs=["Materiaal: polyester vilt", "Afmeting ca. Ø 35 x 30 cm", "Kleur: gemêleerd grijs"],
     faq=[("Mag mijn hond zelf zijn speelgoed eruit pakken?", "Ja, dat is juist leuk. Let op dat hij niet op de mand zelf gaat kauwen.")])

prod(handle="cadeauset-nieuwe-pup", titel="Cadeauset Nieuwe pup", collectie="Cadeaus",
     gram=[900], retour=0.04, w=W_SPEEL + " " + W_TUIG,
     var=[("XS-tuig", 27, 5.95, 89.95), ("S-tuig", 27, 5.95, 89.95)],
     intro="Alles om goed te beginnen, in één doos: een zacht Y-tuig, de verstelbare biothane riem, een slowfeeder en een touwspeelgoedset. Een cadeau waar baasje én pup blij van worden.",
     voordelen=["4 producten, voordeliger dan los", "Rustige, bij elkaar passende kleuren", "Inclusief welkomstkaart met tips voor de eerste weken"],
     specs=["Inhoud: Y-tuig (XS of S), biothane riem 2 m, slowfeeder 500 ml, touwset 3-delig"],
     faq=[("Kan ik het tuig ruilen voor een andere maat?", "Ja, binnen 30 dagen. Neem contact op, dan regelen we het.")])
# Seizoensproduct (lancering april): koelmat — niet in startcatalogus.


def calc(inkoop, verzend, prijs, retour):
    excl = prijs / (1 + BTW)
    btw = prijs - excl
    betaal = prijs * PAY_PCT + PAY_FIX
    ret = retour * (verzend + ADMIN_RETOUR + AFSCHRIJVING * inkoop)
    winst = excl - inkoop - verzend - betaal - ret
    marge = winst / excl
    # max inkoop bij 40% marge: excl - i - v - b - r(i) = 0.4*excl
    max_i = (excl * (1 - DOEL_MARGE) - verzend - betaal - retour * (verzend + ADMIN_RETOUR)) / (1 + retour * AFSCHRIJVING)
    return dict(excl=excl, btw=btw, betaal=betaal, ret=ret, winst=winst, marge=marge, max_i=max_i)


def eur(x):
    return f"€ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x):
    return f"{x * 100:.1f}%".replace(".", ",")


def main():
    rows, ok = [], True
    for p in P:
        for naam, i, v, pr in p["var"]:
            c = calc(i, v, pr, p["retour"])
            ok &= c["marge"] >= DOEL_MARGE
            rows.append((p, naam, i, v, pr, c))

    # 03-productlijst.md
    L = ["# Stap 3 — Productlijst met calculatie (Hyggehond)", "",
         "Gegenereerd door `webshop/data/producten.py`; wijzig daar en draai het script opnieuw.", "",
         "**Aannames**", "",
         "- Verkoopprijs incl. 21% btw (alle hondenaccessoires vallen onder 21%; er zijn geen 9%-producten zoals voeding).",
         "- Inkoop = **doelinkoopprijs excl. btw** bij een EU-leverancier. Btw op inkoop is aftrekbaar, en bij ES/DE-leveranciers geldt btw-verlegging.",
         "- Verzend = wat de leverancier per order rekent. Wij rekenen conservatief, alsof de verzending voor de klant gratis is.",
         "- Betaalkosten = 1,9% + € 0,25 (gemengd iDEAL/Wero, Bancontact, kaart, Klarna).",
         "- Retourreservering = retour% × (verzend + € 2 handling + 20% afschrijving op inkoop). De klant betaalt zelf de retourzending (zo vermeld in het retourbeleid), behalve bij een defect of een verkeerde levering.",
         "- Brutomarge = (excl. btw − inkoop − verzend − betaalkosten − retourreservering) / excl. btw. Advertentiekosten zitten hier niet in (zie stap 7).",
         "- **Max. inkoop** = de hoogste inkoopprijs waarbij het product nog 40% marge haalt. Leg leveranciersoffertes hiernaast.", "",
         "| # | Product | Variant | Inkoop | Verzend | Verkoop incl. | Excl. btw | Betaalk. | Retour% | Retourres. | Winst | **Marge** | Max. inkoop |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    n = 0
    last = None
    for p, naam, i, v, pr, c in rows:
        if p is not last:
            n += 1
            last = p
        L.append(f"| {n} | {p['titel']} | {naam} | {eur(i)} | {eur(v)} | {eur(pr)} | {eur(c['excl'])} | {eur(c['betaal'])} | "
                 f"{p['retour']*100:.0f}% | {eur(c['ret'])} | {eur(c['winst'])} | **{pct(c['marge'])}** | {eur(c['max_i'])} |")
    avg = sum(r[5]["marge"] for r in rows) / len(rows)
    L += ["", f"**{len(P)} producten, {len(rows)} varianten. Gemiddelde brutomarge: {pct(avg)}. "
          f"{'Alle varianten ≥ 40%.' if ok else 'LET OP: niet alle varianten halen 40%.'}**", "",
          "## Collecties", ""]
    cols = {}
    for p in P:
        cols.setdefault(p["collectie"], []).append(p["titel"])
    for k, v in cols.items():
        L.append(f"- **{k}**: " + ", ".join(v))
    L += ["", "## Bestsellers voor de homepage (verwachting)",
          "1. Orthopedische hondenmand Rust (hoogste orderwaarde, Q4)",
          "2. Y-tuig zacht gevoerd + verstelbare riem biothane (cross-sell-duo)",
          "3. Snuffelmat en likmat (impulsaankopen, vuurwerkperiode)",
          "4. Cadeauset Nieuwe pup (cadeauseizoen)", "",
          "## Bewust niet in het assortiment",
          "- Voeding, snacks, supplementen en medicijnen (aparte regelgeving, 9% btw, houdbaarheid)",
          "- Elektrische producten zoals GPS-trackers en lichtgevende halsbanden met batterij (CE/RED/EMC, WEEE en batterijregels)",
          "- Stroom- en prikhalsbanden (omstreden en deels verboden)",
          "- Koelmat met gel: seizoensproduct voor april, eerst de veiligheidsinformatie van de leverancier toetsen", "",
          "## Fotomateriaal-checklist (per product)",
          "Bestel samples van alle producten met een orderwaarde boven € 30 en van de top 5 (budget € 200). Fotografeer met je eigen hond.", "",
          "- [ ] Packshot op een rustige, lichte achtergrond (zand/crème), 2048 × 2048 px, vierkant",
          "- [ ] Sfeerfoto in huis of op pad **met je eigen hond** (daglicht, geen flits)",
          "- [ ] Detailfoto's: materiaal, naden, sluitingen en label (ook als bewijs voor GPSR)",
          "- [ ] Maatfoto: product met een meetlint of naast een bekend object; bij manden de hond erin liggend",
          "- [ ] Korte video van 10–20 s, verticaal 9:16 (gebruik, bijvoorbeeld de hond die gaat liggen of de riem verstellen); te hergebruiken voor TikTok/Reels",
          "- [ ] Foto van het etiket/de verpakking met fabrikantgegevens (archief, GPSR)",
          "- [ ] Alt-tekst geschreven (wat is er te zien, inclusief kleur en maat)",
          "- [ ] Bestandsnaam met zoekwoord, bijv. `orthopedische-hondenmand-rust-zand-m.jpg`",
          "- [ ] Geen leveranciersfoto's met watermerk; leveranciersbeelden alleen gebruiken met schriftelijke toestemming",
          ""]
    open(os.path.join(ROOT, "03-productlijst.md"), "w").write("\n".join(L))

    # productteksten.md
    T = ["# Productteksten Hyggehond", "",
         "Unieke teksten, niet overgenomen van de leverancier. **Controleer specificaties en maten tegen het leveranciersblad en het sample vóór publicatie.**", ""]
    for p in P:
        T += [f"## {p['titel']}", "", f"*Collectie: {p['collectie']} · vanaf {eur(min(v[3] for v in p['var']))}*", "",
              p["intro"], "", "**Waarom je dit fijn vindt**"] + [f"- {x}" for x in p["voordelen"]] + \
             ["", "**Specificaties**"] + [f"- {x}" for x in p["specs"]] + \
             ["- Maten: " + " · ".join(v[0] for v in p["var"]), "", "**Veelgestelde vragen**"]
        for q, a in p["faq"]:
            T += [f"- **{q}** {a}"]
        T += ["", f"**Veiligheid (GPSR):** {p['w']}", "",
              f"**SEO-titel:** {p['titel']} | Hyggehond",
              f"**Metabeschrijving:** {p['intro'].split('.')[0]}. Levering in 2–5 werkdagen, 30 dagen bedenktijd.", ""]
    open(os.path.join(ROOT, "05-teksten", "productteksten.md"), "w").write("\n".join(T))

    # Shopify CSV
    hdr = ["Handle", "Title", "Body (HTML)", "Vendor", "Type", "Tags", "Published", "Option1 Name", "Option1 Value",
           "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Policy",
           "Variant Fulfillment Service", "Variant Price", "Variant Requires Shipping", "Variant Taxable",
           "Cost per item", "SEO Title", "SEO Description", "Status",
           "GPSR waarschuwingen (product.metafields.custom.gpsr_warnings)"]
    with open(os.path.join(HERE, "shopify-producten.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        for idx, p in enumerate(P, 1):
            body = (f"<p>{p['intro']}</p><h3>Waarom je dit fijn vindt</h3><ul>" +
                    "".join(f"<li>{x}</li>" for x in p["voordelen"]) + "</ul><h3>Specificaties</h3><ul>" +
                    "".join(f"<li>{x}</li>" for x in p["specs"]) + "</ul><h3>Veelgestelde vragen</h3>" +
                    "".join(f"<p><strong>{q}</strong><br>{a}</p>" for q, a in p["faq"]))
            for j, (naam, i, v, pr) in enumerate(p["var"]):
                first = j == 0
                gram = p["gram"][min(j, len(p["gram"]) - 1)]
                w.writerow([p["handle"], p["titel"] if first else "", body if first else "",
                            "Hyggehond" if first else "", p["collectie"] if first else "",
                            ("hond, " + p["collectie"].lower()) if first else "", "FALSE" if first else "",
                            "Maat" if first else "", naam, f"HH-{idx:02d}-{j+1}", gram, "shopify", "deny", "manual",
                            f"{pr:.2f}", "TRUE", "TRUE", f"{i:.2f}",
                            f"{p['titel']} | Hyggehond" if first else "",
                            (p["intro"].split(".")[0] + ". Levering in 2–5 werkdagen, 30 dagen bedenktijd.")[:160] if first else "",
                            "draft" if first else "", p["w"] if first else ""])
    print(f"{len(P)} producten, {len(rows)} varianten, gem. marge {avg*100:.1f}%, alle >=40%: {ok}")
    for p, naam, i, v, pr, c in rows:
        if c["marge"] < DOEL_MARGE:
            print("  ONDER 40%:", p["titel"], naam, f"{c['marge']*100:.1f}%")


if __name__ == "__main__":
    main()
