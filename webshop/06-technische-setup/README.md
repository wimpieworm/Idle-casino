# Stap 6 — Technische setup, stap voor stap

Volgorde = afhankelijkheden. Reken op ca. 2–3 avonden werk.
Apps: maximaal **6 apps met front-end-script**, omdat elke app de laadtijd verhoogt.

## Fase A — Account en basis (dag 1)
1. **Shopify Basic** aanmaken op shopify.com. Kies land **Nederland** en valuta **EUR**.
2. **Domein:**
   - Registreer `hyggehond.nl` en `hyggehond.be`. Dat kan via Shopify (Instellingen → Domeinen), of via een registrar als TransIP, wat vaak goedkoper is.
   - Stel `hyggehond.nl` in als primair domein en laat `.be` daar met een 301 naartoe doorsturen.
   - SSL wordt automatisch geregeld.
3. **E-mail:**
   - Maak `info@`, `privacy@` en `hallo@hyggehond.nl` aan via de mailhosting bij je registrar of Zoho Mail Free.
   - Stel SPF, DKIM en DMARC in. Shopify Email geeft de DKIM-records onder Instellingen → Meldingen → Afzender-e-mail.
   - *Waarom:* zo komen je mails in de inbox terecht en niet in de spam.
4. **Instellingen → Algemeen:**
   - Winkelnaam: Hyggehond.
   - Juridische naam: Dylan Smit Holding B.V.
   - Adres, KvK en btw-id invullen.
   - Ordernummer-prefix: `#HH`.
5. **Beveiliging:** zet tweestapsverificatie aan op het Shopify-account. Voeg je boekhouder later toe als medewerker met beperkte rechten.

## Fase B — Btw, verzending en betalen (dag 1)
6. **Belastingen (Instellingen → Belastingen en heffingen):**
   - Nederland: 21% (standaard).
   - **"Alle prijzen zijn inclusief btw"** aanzetten.
   - **België:**
     - Zolang je samen onder € 10.000 per jaar aan EU-afstandsverkopen blijft, reken je **Nederlandse btw (21%)**. Het tarief is in BE ook 21%, dus de prijs blijft gelijk.
     - Boven de drempel: OSS-registratie via de Belastingdienst (Mijn Belastingdienst Zakelijk). Daarna in Shopify de "OSS"-optie inschakelen, zodat er Belgische btw wordt gerekend.
   - Zet een reminder in de boekhouding om op € 8.000 te controleren hoe ver je zit.
7. **Verzending (Instellingen → Verzending en bezorging):**
   - Zone NL + BE.
   - Tarief 1: "Standaard (2–5 werkdagen)", € 4,95 bij een bestelwaarde van € 0–49,99.
   - Tarief 2: "Gratis verzending (2–5 werkdagen)" bij € 50+.
   - Vink "Lokale bezorging/afhalen" uit.
8. **Betalingen:**
   - Activeer **Shopify Payments** met de KYC-gegevens van de B.V. en het zakelijke rekeningnummer van de holding.
   - Zet aan: iDEAL | Wero, Bancontact, creditcards, Apple Pay, Google Pay, Shop Pay en **Klarna**. Klarna is in NL/BE beschikbaar via Shopify Payments; staat het er niet tussen, voeg het dan toe via de Klarna-app.
   - *Waarom Shopify Payments:* je betaalt geen extra transactiefee (anders 2%) en alles komt binnen in één uitbetaling.
   - *Alternatief:* Mollie-app, als Shopify Payments je B.V. weigert.
   - Uitbetalingsschema: dagelijks, voor je werkkapitaal.
9. **Checkout (Instellingen → Afrekenen):**
   - Klantaccounts optioneel (gastafrekenen staat aan).
   - Contact: e-mail verplicht. Telefoon optioneel, maar bij leveranciers die het eisen voor de vervoerder: verplicht, met de uitleg "voor de bezorger".
   - Marketing-opt-in: **niet vooraf aangevinkt**.
   - Taal: Nederlands. Controleer of de knoptekst "Nu betalen" is.
   - Bevestigingsvakje voor AV/herroeping via een checkout-blok "Voorwaarden" (Checkout-editor). Of plaats een tekst met links onder de knop: "Door te bestellen ga je akkoord met onze algemene voorwaarden".

## Fase C — Thema en pagina's (dag 2)
10. **Thema:** Online Store → Themes → **Dawn**.
    - Thema-instellingen: kleuren en lettertypen zoals in `04-sitemap-wireframes.md`.
    - Knoppen met een afgeronde hoek van 4 px.
    - Productkaarten: "tweede afbeelding bij hover" aan.
    - Winkelwagen: **drawer**.
11. **Snippets installeren** (Online Store → Themes → … → Code bewerken). Maak eerst een kopie van het thema.
    - Kopieer de bestanden uit `theme/snippets/` naar `snippets/`.
    - `sections/main-product.liquid`:
      - onder de prijs: `{% render 'delivery-estimate', product: product %}`
      - als laatste accordeon: `{% render 'gpsr-block', product: product %}`
      - onderaan: `{% render 'sticky-atc', product: product %}`
      - na de FAQ: `{% render 'faq-jsonld', faqs: product.metafields.custom.faq.value %}`
    - `snippets/cart-drawer.liquid` en `sections/main-cart-footer.liquid`: `{% render 'free-shipping-bar' %}` en `{% render 'cart-split-notice' %}` boven het subtotaal.
    - `layout/theme.liquid`, in `<head>`: `{% render 'breadcrumb-jsonld' %}`.
12. **Metafield-definities** (Instellingen → Aangepaste gegevens → Producten):

| Naam | Namespace.key | Type |
|---|---|---|
| GPSR fabrikant | custom.gpsr_manufacturer_name | Tekst (één regel) |
| GPSR adres fabrikant | custom.gpsr_manufacturer_address | Tekst (meerdere regels) |
| GPSR contact fabrikant | custom.gpsr_manufacturer_contact | Tekst (één regel) |
| GPSR EU-verantwoordelijke | custom.gpsr_eu_responsible | Tekst (meerdere regels) |
| GPSR waarschuwingen | custom.gpsr_warnings | Tekst (meerdere regels) |
| Leverancier (intern) | custom.leverancier | Tekst (één regel) |
| Levertijd min | custom.levertijd_min | Geheel getal |
| Levertijd max | custom.levertijd_max | Geheel getal |
| FAQ | custom.faq | Lijst met metaobjecten "faq" (velden: vraag, antwoord) |

13. **Producten importeren:**
    - Producten → Importeren → `webshop/data/shopify-producten.csv`. Alle producten komen binnen als **concept**, met de waarschuwingen al in de GPSR-metafield.
    - Koppel daarna elk product aan het leveranciersproduct in Syncee (stap 15), of importeer via Syncee en kopieer de tekst/SEO uit de CSV. Kies één van beide om dubbele producten te voorkomen.
    - *Advies:* importeer via **Syncee** (voor voorraad- en prijssync) en plak de teksten uit `05-teksten/productteksten.md` erin.
14. **Pagina's en beleid:**
    - Online Store → Pagina's: over-ons, faq, contact, track-trace, maatgids, herroepen, herroepingsrecht, cookies.
    - Instellingen → Beleid: retour-, privacy-, verzend- en servicevoorwaarden, en contactgegevens.
    - Teksten staan in `05-teksten/`. Menu's zoals in de sitemap.
    - **Herroepingsknop (`/pages/herroepen`):**
      - De wet eist dat de klant **direct een ontvangstbevestiging op een duurzame gegevensdrager** krijgt, met datum en tijd. Het standaard Dawn-contactformulier stuurt geen bevestiging naar de klant.
      - Gebruik daarom een formulier-app **met autoresponder**, en controleer vóór installatie of het gratis plan een autoresponder bevat. Zet daarin de velden uit `herroepingsrecht.md` en de knoptekst "Herroeping bevestigen". De autoresponder-tekst staat ook in `herroepingsrecht.md`.
      - Noodoplossing tot de app werkt: het Dawn-contactsjabloon, waarbij jij de bevestiging dezelfde dag handmatig stuurt.
      - Link in de footer, in de orderbevestiging en op de bestelstatuspagina.

## Fase D — Leveranciers en automatisering (dag 2)
15. **Syncee** installeren via de Shopify App Store. Daarna:
    - Selecteer de leveranciers volgens de checklist in `02-leveranciers.md`.
    - Importeer de producten.
    - **Prijsregels:** vaste verkoopprijs uit de calculatie, geen automatische opslag. *Waarom:* zo voorkom je dat Syncee-prijswijzigingen je prijzen laten springen. Zet wel een **melding** aan bij een inkoopprijswijziging van meer dan 5%.
    - **Voorraadsync:** aan, minimaal dagelijks. Bij 0 voorraad: "product verbergen" (bijv. een Shopify Flow-regel: als de voorraad 0 is, product status = draft). Of in de thema-instellingen uitverkochte producten onderaan zetten. Advies: verbergen.
    - **Automatische ordersync:** aan. Orders worden betaald doorgestuurd naar de leverancier. Zet een **betaalmethode** bij Syncee klaar (zakelijke creditcard/debitcard) voor de automatische inkoop.
    - **Tracking:** de leverancier vult het trackingnummer in → Syncee zet de fulfillment in Shopify → Shopify stuurt automatisch de verzendmail met link. Bij een split order gebeurt dit per leverancier, dus de klant krijgt 2 mails.
16. **Shopify Flow** (gratis) voor deze regels:
    - Order > € 150 of een afwijkend factuur-/afleveradres → tag "controle" en mail naar jou (fraude).
    - Order zonder fulfillment na 2 werkdagen → mail naar jou, zodat je de leverancier kunt aansporen.
    - Product voorraad = 0 → status concept. Voorraad > 0 → actief.
    - Klant tag "retour" → herinnering na 10 dagen om de terugbetaling te controleren.
17. **Track & trace-pagina:**
    - Shopify heeft standaard een bestelstatuspagina. Voor `/pages/track-trace` kun je de gratis app **Parcel Panel** (free plan) gebruiken. Die toont meerdere pakketten per order en NL-vervoerders.
    - *Alternatief:* in plaats van de pagina de link "Bestelling bekijken" in het klantaccount en de verzendmails. Advies: Parcel Panel free, omdat het minder klantvragen oplevert.

## Fase E — Vertrouwen, reviews en e-mail (dag 3)
18. **Reviews: Judge.me** (free plan).
    - Alleen geverifieerde kopers, met automatisch reviewverzoek 7 dagen na fulfillment.
    - Tekst zoals in `emailflows.md`.
    - Review-snippets aan (structured data).
    - **Geen import van leveranciersreviews.** Dat is misleidend en mag niet volgens de ACM-regels.
19. **Trustpilot** (gratis bedrijfsprofiel) koppelen voor reviews over de winkel. Toon de widget pas bij ≥ 10 reviews.
    - **Thuiswinkel Waarborg** of **WebwinkelKeur:** zinvol in fase 2 (vanaf ca. € 3.000 omzet per maand). Kosten zijn in jaar 1 niet begroot.
20. **E-mail:**
    - Shopify Email en Marketing Automations instellen volgens `emailflows.md`.
    - Pas de transactionele meldingen aan (Instellingen → Meldingen): orderbevestiging, verzendbevestiging, terugbetaling. Zet in de orderbevestiging de link naar de herroepingsknop en de AV.
    - Nieuwsbrief-aanmelding met **dubbele opt-in**: Instellingen → Meldingen → "Marketingtoestemming bevestigen".

## Fase F — Privacy, tracking en feeds (dag 3)
21. **Cookiebanner:**
    - Instellingen → Klantprivacy → **Cookiebanner** aan, regio EU.
    - Knoppen "Accepteren", "Weigeren" en "Beheren" moeten even prominent zijn.
    - Tekst: "We gebruiken cookies om de website te laten werken en, als je dat goed vindt, om te analyseren en advertenties te meten. Lees de [cookieverklaring](/pages/cookies)."
    - Zet "Cookie-instellingen" in de footer.
    - *Waarom de ingebouwde banner:* gratis, en hij werkt automatisch samen met de apps van Google, Meta en TikTok via de Customer Privacy API.
22. **Google & YouTube-app** (gratis):
    - Koppel het Google-account.
    - Maak **Google Merchant Center** aan. Dat geeft de productfeed met gratis vermeldingen + Shopping.
    - Maak **GA4** aan en koppel het (de app plaatst de tag, inclusief Consent Mode v2).
    - Google Ads-conversie: "Aankoop".
    - Merchant Center:
      - Verzendinstellingen gelijk aan Shopify (NL/BE, € 4,95 / gratis vanaf € 50, 2–5 dagen).
      - Retourbeleid 30 dagen.
      - Bedrijfsgegevens en telefoon/e-mail verifiëren.
    - Product-ID's: geen GTIN? Kies "Geen GTIN" alleen bij echt merkloze producten. Vraag GTIN/EAN op bij de leverancier.
23. **Facebook & Instagram-app** (Meta):
    - Koppel de Business Manager, maak een Pixel aan, en zet **Data-sharing op "Maximaal"** (= Conversions API, server-side).
    - Instagram Shopping-catalogus.
    - Domeinverificatie via een DNS TXT-record.
24. **TikTok-app:** TikTok Pixel + **Events API** (data-sharing "maximaal"), plus een catalogus voor later.
25. **Google Search Console:** verifieer het domein via DNS en dien `hyggehond.nl/sitemap.xml` in.
26. **Test van de tracking:**
    - GA4 DebugView, Meta Events Manager "Test events" en TikTok Pixel Helper.
    - Controleer dat er **niets** wordt verstuurd vóór toestemming in de cookiebanner (Chrome DevTools → Network, zoek op `collect`, `facebook`, `tiktok`).

## Fase G — Snelheid en toegankelijkheid
27. **Afbeeldingen:**
    - Upload op 2048 px. Shopify levert automatisch WebP/AVIF en responsive formaten aan.
    - Hero: 1 afbeelding, geen slider of video als hero.
    - Bestandsgrootte vóór upload < 400 KB (squoosh.app).
28. **Fonts:** Fraunces alleen voor koppen, Inter voor tekst. Gebruik de Shopify font library (self-hosted, `font-display: swap`).
29. **Apps:**
    - Na elke installatie: meet met PageSpeed Insights (mobiel).
    - Doel: LCP < 2,5 s, CLS < 0,1, INP < 200 ms.
    - Apps die je niet meer gebruikt: verwijderen, en eventuele overgebleven code uit het thema halen.
30. **Toegankelijkheid:**
    - Controleer met WAVE (wave.webaim.org) en alleen met het toetsenbord (Tab, Shift-Tab, Enter, Esc).
    - Contrast via de kleurkeuzes (zie stap 4).
    - Alt-teksten: in Shopify per afbeelding "Alt-tekst bewerken".
    - Formuliervelden hebben labels (Dawn heeft dat standaard).
    - *Wettelijk:* de European Accessibility Act (vanaf 28-06-2025) geldt **niet** voor micro-ondernemingen (< 10 medewerkers én ≤ € 2 mln omzet). Voor Hyggehond is WCAG 2.1 AA dus "best practice", geen plicht. Wel goed voor conversie en SEO.

## Overzicht apps en kosten
| App/dienst | Doel | Kosten |
|---|---|---|
| Shopify Basic | Platform | ca. € 27–36 per maand (jaar- vs maandbetaling); let op introductieacties |
| Syncee | Leveranciers, sync | Gratis → ca. € 37 per maand |
| Judge.me | Productreviews | Gratis |
| Parcel Panel | Track & trace-pagina | Gratis plan |
| Shopify Email / Flow / Forms | E-mail, automatisering, formulieren | Gratis (tot 10.000 mails per maand) |
| Google & YouTube, Facebook & Instagram, TikTok | Tracking + feeds | Gratis |
| Trustpilot | Winkelreviews | Gratis plan |
| **Totaal vaste lasten** | | **ca. € 65–75 per maand** |

## Wat ik niet voor je kon doen (accounts op jouw naam)
- Shopify-, Syncee-, Google-, Meta- en TikTok-accounts aanmaken; de KYC voor betalingen; de domeinregistratie.
- Samples bestellen en fotograferen.
- Echte inkoopprijzen en GPSR-gegevens invullen.

Als je de accounts hebt, kan ik je per scherm verder helpen, of de code in je thema-export controleren.
