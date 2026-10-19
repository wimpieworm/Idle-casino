# SEO: zoekwoordonderzoek (NL/BE)

Methode: zoekwoorden per zoekintentie, gekoppeld aan één pagina per cluster (geen kannibalisatie). **De zoekvolumes zijn schattingen (laag/middel/hoog).** Controleer ze gratis in de Google Keyword Planner (Google Ads-account, land NL + BE, taal Nederlands) en vul de kolom "volume" vóór de lancering in.

| Cluster | Hoofdzoekwoord | Gerelateerd / long-tail | Intentie | Concurrentie | Pagina |
|---|---|---|---|---|---|
| Manden | hondenmand | hondenmand kopen, hondenmand groot, wasbare hondenmand | Transactioneel | Hoog | /collections/rust-slapen |
| Orthopedisch | orthopedische hondenmand | hondenmand traagschuim, hondenmand oude hond, memory foam hondenbed | Transactioneel | Middel | /products/orthopedische-hondenmand-rust |
| Donut | donut hondenmand | ronde hondenmand, fluffy hondenmand | Transactioneel | Middel | /products/donutmand-nest |
| Maat | hondenmand maat | welke maat hondenmand, hondenmand afmetingen | Informatief | Laag | Blog 1 + /pages/maatgids |
| Tuig | hondentuig | y tuig hond, tuig voor hond die trekt, hondentuig maat | Transactioneel | Hoog | /collections/op-pad + Y-tuig |
| Tuig vs halsband | tuig of halsband | halsband of tuig pup, is een tuig beter | Informatief | Laag | Blog 3 |
| Biothane | biothane riem | biothane lijn, waterdichte hondenriem, sleeplijn 10 meter | Transactioneel | Laag | Riem + sleeplijn |
| Verrijking | snuffelmat | snuffelmat hond, hond vermaken binnen, likmat hond | Gemengd | Middel | Blog 4 + snuffelmat |
| Vuurwerk | hond bang vuurwerk | hond rustig krijgen vuurwerk, likmat vuurwerk | Informatief (piek dec.) | Middel | Blog 4 (sectie) / nieuwsbrief |
| Auto | hond in de auto | hond vervoeren auto, autostoel hond, achterbank hoes hond | Gemengd | Middel | Blog 5 + autoproducten |
| Voerbak | slowfeeder hond | anti schrok bak, verhoogde voerbak hond | Transactioneel | Middel | Slowfeeder + keramische bakken |
| Pup | puppy uitzet | eerste spullen pup, cadeau nieuwe pup | Gemengd | Laag | Blog 2 + cadeauset |

## On-page-regels
- **Metatitel:** ≤ 60 tekens, met het zoekwoord vooraan en "| Hyggehond" achteraan.
- **Metabeschrijving:** ≤ 155 tekens, met een voordeel, de levertijd en een CTA.
- Eén H1 per pagina, met het zoekwoord. Duidelijke H2's.
- **URL's** kort en Nederlandstalig (`/products/orthopedische-hondenmand-rust`).
- Afbeeldingen: bestandsnaam met zoekwoord, alt-tekst die beschrijft wat er te zien is.
- **Interne links:**
  - blog → product/collectie
  - product → maatgids
  - collectie → blog

## Structured data
- **Product + Offer + AggregateRating/Review:** Dawn geeft Product/Offer al standaard. Judge.me voegt Review/AggregateRating toe, maar pas bij echte reviews.
- **FAQPage:** op /pages/faq en in de FAQ-accordeons van producten (snippet in `06-technische-setup/theme/snippets/faq-jsonld.liquid`).
- **Organization + WebSite:** zit in Dawn. Vul het logo en de sociale profielen in de thema-instellingen in.
- **BreadcrumbList:** via de snippet.
- **Article:** standaard in Dawn voor blogposts.

Test alles met de Rich Results Test van Google (search.google.com/test/rich-results).

## Belgische markt
Dezelfde Nederlandse content werkt in Vlaanderen. Let op Vlaamse varianten: "hondenkussen" wordt vaker gebruikt dan "hondenmand", en "leiband" vaker dan "riem". Verwerk die als synoniemen in de teksten, bijvoorbeeld "riem (leiband)". Aparte hreflang is niet nodig zolang er één Nederlandstalige versie is.
