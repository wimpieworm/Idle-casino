# Stap 7 — Lanceringschecklist + plan voor de eerste 30 dagen

## A. Lanceringschecklist (alles afvinken vóór je het wachtwoord van de winkel haalt)

### Juridisch en bedrijf
- [ ] Handelsnaam **Hyggehond** ingeschreven bij KvK onder Dylan Smit Holding B.V.; statuten en SBI-code staan handel toe
- [ ] Btw-id actief voor webshopactiviteiten; boekhouder geïnformeerd (geen KOR)
- [ ] Merknaam gecheckt bij het BOIP; Instagram- en TikTok-handle @hyggehond geclaimd
- [ ] Juridische concepten gecontroleerd door een jurist; placeholders ([ADRES], [KVK], [BTW], [DATUM]) ingevuld
- [ ] KvK-nummer, btw-id, adres en e-mail zichtbaar in de footer en op de contactpagina
- [ ] Herroepingsknop `/pages/herroepen` werkt **en** stuurt een automatische ontvangstbevestiging met datum en tijd
- [ ] Modelformulier, AV en retourbeleid gelinkt in de orderbevestiging
- [ ] Per product GPSR-gegevens ingevuld (fabrikant, EU-verantwoordelijke indien nodig, waarschuwingen); documenten gearchiveerd in een map per leverancier
- [ ] UPV Textiel en verpakkingsregels gecheckt (zie juridisch/00-LEES-MIJ)
- [ ] Geen doorgestreepte "van"-prijzen, afteltimers, nepvoorraad of reviews zonder echte koper
- [ ] Hygiëne-uitzondering (likmat, kauwspeelgoed) alleen gebruikt als de leverancier verzegeld levert; anders weggehaald

### Producten
- [ ] Samples ontvangen en goedgekeurd (kwaliteit, maat, geur); niet-goedgekeurde producten verwijderd
- [ ] Inkoopprijzen ≤ max. inkoop uit `03-productlijst.md`; script opnieuw gedraaid met de echte prijzen
- [ ] Eigen foto's (minimaal 3 per product) + alt-teksten; maatgids-links bij manden, tuigen en jassen
- [ ] Specificaties in de teksten vergeleken met het leveranciersblad en het sample
- [ ] Metafields leverancier en levertijd ingevuld; uitverkocht → verborgen (Flow-regel getest)
- [ ] Producten op **actief** gezet (CSV importeert als concept)

### Betalen en checkout
- [ ] Shopify Payments geverifieerd; uitbetalingsrekening gekoppeld
- [ ] **Testbestellingen** (testmodus van Shopify Payments + 1 echte bestelling met iDEAL, daarna terugbetaald):
  - [ ] iDEAL | Wero
  - [ ] Bancontact (in testmodus)
  - [ ] Creditcard
  - [ ] Apple Pay (iPhone) en Google Pay (Android)
  - [ ] Klarna
- [ ] Verzendkosten correct: € 4,95 onder € 50 en gratis vanaf € 50; NL- en BE-adres getest
- [ ] Btw correct op de factuur (21%, prijs inclusief btw)
- [ ] Kortingscode WELKOM10 werkt en vervalt na 14 dagen
- [ ] Gastafrekenen werkt; marketing-opt-in staat niet vooraf aangevinkt

### Fulfillment (de echte testbestelling)
- [ ] Order komt automatisch bij de leverancier binnen (Syncee), en is betaald vanaf je zakelijke kaart
- [ ] Track & trace komt terug in Shopify en de klant krijgt de verzendmail met de juiste link
- [ ] **Split order getest**: 2 producten van 2 leveranciers geven 2 verzendmails, de melding in de winkelwagen en 2 pakketten in Parcel Panel
- [ ] Pakket ontvangen: neutrale of white-label verpakking, geen factuur van de leverancier, levertijd ≤ 5 werkdagen
- [ ] Retour getest: aanmelding via de herroepingsknop → bevestiging → retouradres → terugbetaling in Shopify

### E-mails
- [ ] Alle transactionele mails in het Nederlands en in de huisstijl: bevestiging, verzending, terugbetaling, verlaten checkout
- [ ] Welkomstflow, verlaten-winkelwagenflow, na-aankoopflow en Judge.me-reviewverzoek actief
- [ ] Dubbele opt-in werkt; afmeldlink werkt
- [ ] SPF/DKIM/DMARC gecontroleerd (mail-tester.com, score ≥ 9/10)

### Tracking
- [ ] Cookiebanner: weigeren is even makkelijk als accepteren; niets wordt geladen vóór toestemming (getest in DevTools)
- [ ] GA4: purchase-event met de juiste waarde (DebugView)
- [ ] Meta: Purchase via de pixel én CAPI, met deduplicatie zichtbaar in Events Manager
- [ ] TikTok: CompletePayment-event
- [ ] Merchant Center: producten goedgekeurd (geen afkeuringen over verzending, retour of identifiers)
- [ ] Search Console: sitemap ingediend

### Snelheid en mobiel
- [ ] PageSpeed Insights mobiel: home, collectie en product scoren **groen** voor LCP < 2,5 s, CLS < 0,1 en INP < 200 ms
- [ ] Getest op iPhone (Safari) en Android (Chrome): menu, filter, variantkeuze, sticky winkelwagenknop, drawer, checkout
- [ ] Alleen-toetsenbordtest: alles bereikbaar, focus zichtbaar; WAVE zonder contrastfouten
- [ ] 404-pagina en zoekfunctie werken; favicon en social share-afbeelding ingesteld

### Content
- [ ] 5 blogartikelen live (met interne links)
- [ ] Over ons, FAQ, contact, maatgids en track & trace live
- [ ] Instagram en TikTok: minimaal 9 posts / 6 video's klaar vóór de livegang

---

## B. Lanceringsplan voor de eerste 30 dagen (advertentiebudget € 400)

**Uitgangspunt:** met € 400 test je, je schaalt nog niet. Het doel van maand 1 is leren:
- welke 2–3 producten verkopen
- welke creatives werken
- wat je echte CPA en conversieratio zijn

Organische content met je eigen hond is het belangrijkste kanaal.

**Verdeling:**
| Kanaal | Budget | Waarom |
|---|---|---|
| Meta (Instagram/Facebook) Advantage+ Sales | € 240 (€ 8 per dag) | Visueel product en emotionele aankoop: daar werken Reels met je hond goed. Het algoritme zoekt zelf de doelgroep |
| Google Shopping (Performance Max, alleen feed) | € 150 (€ 5 per dag) | Vangt mensen die al zoeken ("orthopedische hondenmand"). Plus de **gratis vermeldingen** in Merchant Center |
| Reserve | € 10 | Een winnende post boosten |
| TikTok | € 0 (alleen organisch) | Organisch bereik is hier het grootst; betaald pas vanaf maand 2, met Spark Ads op een video die organisch goed scoort |

**Rekensom:**
- Bij een gemiddelde orderwaarde van ca. € 55 en een brutomarge van 44% heb je per order ca. € 20 aan brutowinst.
- **Break-even CPA ≈ € 20.** Daarboven verlies je geld op de eerste order. Herhaalaankopen via e-mail maken dat later goed.
- Verwachting maand 1: 15–25 betaalde orders, plus organische en directe orders.

### Week 0 (vóór de lancering): voorbereiden
- Content-voorraad opbouwen: 10 korte video's (9:16, 7–20 s) en 15 foto's met je hond.
- Instagram en TikTok vullen: 9 posts, bio met link.
- Lokale lijst maken: 10 trimsalons, hondenscholen en uitlaatservices in je regio. Bied ze een samenwerking aan: een kortingscode voor hun klanten en 10% commissie, of een product ter waarde van € 30 om in de wachtruimte te gebruiken.

### Week 1: soft launch (dag 1–7)
- Live voor vrienden, familie en je eigen netwerk. Vraag om **eerlijke** feedback en, na levering, een review (geen beloning).
- Meta-campagne starten: 1 Advantage+ Sales-campagne met **5 creatives** (zie hieronder), NL + BE, 25–55 jaar.
- Google PMax-campagne met alleen de feed, NL + BE, doel "Conversiewaarde maximaliseren" zonder doel-ROAS (te weinig data).
- Organisch: 1 video per dag op TikTok en Instagram Reels.

### Week 2: eerste data (dag 8–14)
- Na € 60–80 Meta-spend: pauzeer creatives met een CTR (link) < 0,8% of zonder add-to-carts. Voeg 2 nieuwe varianten toe van de winnaar.
- Controleer de **winkelwagen → checkout → aankoop**-trechter in GA4. Valt de checkout tegen? Kijk dan naar de verzendkosten en betaalmethoden.
- Eerste nieuwsbrief: "Ons eerste weekje + [NAAM HOND] test de nieuwe mand".
- Bekijk de eerste leveringen: levertijd per leverancier, en of klanten iets melden.

### Week 3: optimaliseren (dag 15–21)
- Budget verschuiven naar wat werkt (Meta of Google). Hoog geen budget op boven de € 13 per dag.
- Vuurwerk en de feestdagen voorbereiden (als de lancering in nov/dec valt):
  - blog/sectie "Hond bang voor vuurwerk"
  - de likmat en snuffelmat uitlichten
  - cadeaugids met de cadeauset
- 2 samenwerkingen met lokale partners actief.

### Week 4: evalueren (dag 22–30)
- **Evaluatie:**
  - Omzet, aantal orders, gemiddelde orderwaarde, conversieratio (doel ≥ 1,2%), CPA per kanaal, retourpercentage, levertijd per leverancier, reviews.
- **Besluit voor maand 2:**
  - CPA < € 20: budget naar € 15–20 per dag, met de winst uit maand 1.
  - CPA > € 30: niet opschalen. Eerst de productpagina's en het aanbod verbeteren (bundels), meer organische content, en andere creatives testen.
  - Producten die na 30 dagen geen enkele verkoop of add-to-cart hebben, vervangen.

### Creatives om te testen (Meta en organisch)
| # | Concept | Haak (eerste 2 seconden) | Product |
|---|---|---|---|
| 1 | **"De test"** | "We hebben 4 manden getest. Deze wint." Je hond kiest tussen manden | Orthopedische mand Rust |
| 2 | **Voor/na modder** | Modderige hond springt in de auto, daarna een schone achterbank | Autostoelhoes + pootreiniger |
| 3 | **Snuffel-ASMR** | Close-up: snuitje zoekt in de snuffelmat, met geluid | Snuffelmat |
| 4 | **Maat-uitleg** | "Zo meet je je hond in 10 seconden." Educatief, met de maatgids | Y-tuig |
| 5 | **Rustig moment** | Hond valt in slaap in de mand terwijl het buiten regent (hygge-sfeer, geen tekst) | Donutmand / plaid |

Regels:
- Echte beelden, geen leveranciersvideo's.
- Ondertitels in beeld (85% kijkt zonder geluid).
- De prijs mag in de tekst.
- Geen claims als "de beste", "medisch", "voorkomt gewrichtsklachten", of zelfverzonnen kortingen.

### KPI-dashboard (wekelijks in een spreadsheet)
| KPI | Doel maand 1 |
|---|---|
| Sessies | 2.500+ |
| Conversieratio | ≥ 1,2% |
| Gemiddelde orderwaarde | ≥ € 50 |
| CPA (betaald) | ≤ € 20 |
| Levertijd (bestelling → bezorgd) | ≤ 5 werkdagen in 95% van de orders |
| Retourpercentage | ≤ 8% |
| Reviews | ≥ 10 echte reviews |
| Nieuwsbriefabonnees | 150+ |
