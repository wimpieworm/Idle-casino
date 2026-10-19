# Stap 4 — Sitemap en wireframes (Hyggehond)

Platform: Shopify, met het gratis thema **Dawn** (snelste Shopify-thema, goed toegankelijk en zonder kosten). Mobile-first: de wireframes gaan uit van een scherm van 375 px breed. Op desktop worden ze 2–4 kolommen.

## Merkstijl
| Element | Keuze | Waarom |
|---|---|---|
| Kleuren | Achtergrond `#FAF7F2` (crème) · tekst `#2B2A28` · accent `#5E6B4E` (mosgroen) · knoppen `#2B2A28` met witte tekst · ondersteunend `#D9CBB4` (zand) | Rustig en warm. Tekst op crème heeft een contrast van ca. 13:1 en wit op de donkere knop ca. 14:1, ruim boven de WCAG AA-eis van 4,5:1 |
| Lettertype | Koppen: *Fraunces* (serif); tekst: *Inter* (systeemfallback) | Premium en warm, maar goed leesbaar. Maximaal 2 fonts, vanwege de laadsnelheid |
| Fotografie | Daglicht, natuurlijke tinten, eigen hond, veel ruimte | Echtheid is ons onderscheid (zie stap 1) |
| Tone of voice | Je-vorm, rustig, deskundig, eerlijk; geen hypes of uitroeptekens | Past bij premium en vertrouwd |

## Sitemap
```
/                                   Home
├── /collections/all                Alle producten
│   ├── /collections/rust-slapen
│   ├── /collections/op-pad
│   ├── /collections/eten-drinken
│   ├── /collections/spelen-verrijking
│   ├── /collections/verzorging
│   ├── /collections/thuis
│   └── /collections/cadeaus
├── /products/{handle}              Productpagina's (26)
├── /cart                           Winkelwagen
├── /checkouts/…                    Checkout (Shopify)
├── /pages/over-ons
├── /pages/faq
├── /pages/contact
├── /pages/track-trace              Bestelling volgen
├── /pages/maatgids                 "Meet je hond"
├── /pages/herroepen                Herroepingsknop (verplicht sinds 19-06-2026)
├── /blogs/journal                  Blog (5 startartikelen)
└── Juridisch (footer)
    ├── /policies/terms-of-service       Algemene voorwaarden
    ├── /policies/privacy-policy         Privacyverklaring
    ├── /pages/cookies                   Cookieverklaring
    ├── /policies/refund-policy          Retourbeleid
    ├── /pages/herroepingsrecht          Herroepingsrecht + modelformulier
    ├── /policies/shipping-policy        Verzendbeleid
    └── /policies/contact-information    Bedrijfsgegevens
```

**Hoofdmenu:** Rust & slapen · Op pad · Eten & spelen · Cadeaus · Maatgids
**Footer:** Klantenservice (FAQ, verzending, retour, herroepen, track & trace, contact) · Over Hyggehond (over ons, blog) · Juridisch · Bedrijfsgegevens (KvK, btw-id) · betaalmethodelogo's · nieuwsbrief

## Wireframes

### Home
```
┌──────────────────────────────────┐
│ USP-balk (roteert NIET; 1 regel) │  "Levering in 2–5 werkdagen · 30 dagen bedenktijd · Betalen met iDEAL | Wero"
├──────────────────────────────────┤
│ ☰   HYGGEHOND           🔍  👜(0) │  sticky header
├──────────────────────────────────┤
│ [Hero: foto eigen hond in mand]  │  1 statische afbeelding (géén slider, LCP!)
│ Rust in huis, plezier op pad.    │  H1
│ Mooie basics voor je hond,       │
│ getest door onze eigen hond.     │
│ [ Shop manden ]  [ Op pad → ]    │
├──────────────────────────────────┤
│ 3 USP-iconen                     │  🚚 2–5 werkdagen vanuit EU · ↩ 30 dagen · 🐾 Getest door [naam hond]
├──────────────────────────────────┤
│ Shop per categorie (2×2 tegels)  │
├──────────────────────────────────┤
│ Bestsellers (4 kaarten, scroll)  │  foto · naam · prijs incl. btw · ★ (alleen echte reviews)
├──────────────────────────────────┤
│ Verhaal-blok: "Over [naam hond]" │  foto + 3 zinnen + link over ons
├──────────────────────────────────┤
│ Reviews (Judge.me/Trustpilot)    │  pas tonen vanaf ≥ 5 echte reviews; tot die tijd verborgen
├──────────────────────────────────┤
│ Maatgids-banner                  │  "Twijfel je over de maat? Meet je hond in 2 minuten"
├──────────────────────────────────┤
│ Nieuwsbrief: "Tips + 10% op je   │  dubbele opt-in, geen voorgeselecteerd vinkje
│ eerste bestelling"  [e-mail][→]  │
├──────────────────────────────────┤
│ Footer                           │
└──────────────────────────────────┘
```

### Collectiepagina
```
│ Breadcrumb · H1 "Rust & slapen" · 1–2 zinnen intro (SEO) │
│ [Filter ▾] [Sorteer ▾]   26 producten                    │
│ ┌────┐ ┌────┐   2 kolommen mobiel, 4 desktop             │
│ │foto│ │foto│   naam · "vanaf € 74,95" · ★ (indien echt) │
│ └────┘ └────┘   badge alleen "Nieuw" of "Bijna uitverkocht" bij echte voorraad <5 │
│ SEO-tekst onderaan (150–250 woorden) + FAQ-accordeon       │
```

### Productpagina (belangrijkste conversiepagina)
```
┌──────────────────────────────────┐
│ Breadcrumb                       │
│ [Galerij: swipe, 5–7 foto's +    │  1e foto = LCP, preload; rest lazy
│  video]   ● ○ ○ ○                │
│ Orthopedische hondenmand Rust    │  H1
│ ★★★★★ (12)  ← alleen bij echte    │
│ € 94,95  incl. btw               │  "Verzendkosten: gratis vanaf € 50, anders € 4,95"
│ Maat: [S] [M] [L]  Maatgids ↗    │  knoppen, geen dropdown
│ Kleur: ● zand                    │
│ ✓ Op voorraad — vandaag besteld, │  voorraad uit leverancierssync; levertijd per product
│   levering di 21 – do 23 okt     │  (datum berekend, geen nep-urgentie)
│ [   In winkelwagen   ]           │
│ iDEAL|Wero · Bancontact · Klarna │  logo's
├──────────────────────────────────┤
│ ▸ Beschrijving (open)            │
│ ▸ Specificaties & maten          │
│ ▸ Verzending & retour            │
│ ▸ Veelgestelde vragen            │
│ ▸ Productveiligheid (GPSR)       │  fabrikant + EU-verantwoordelijke + waarschuwingen
├──────────────────────────────────┤
│ "Past mooi bij" (2–3 cross-sell) │  bv. mand → plaid, benchkussen
├──────────────────────────────────┤
│ Reviews (Judge.me) + uitleg hoe  │  "Alleen geverifieerde kopers kunnen een review plaatsen"
│ we reviews controleren           │  (verplicht sinds Omnibus)
├──────────────────────────────────┤
│ [€ 94,95   In winkelwagen]       │  STICKY balk onderin op mobiel zodra knop uit beeld is
└──────────────────────────────────┘
```

### Winkelwagen (drawer + pagina)
```
│ Je winkelwagen (2)                         │
│ Voortgang: "Nog € 12,05 tot gratis verzending" ▓▓▓▓▓░  │  echte drempel € 50
│ [foto] Y-tuig M · € 36,95  [-] 1 [+]  ✕    │
│ Levertijd: 2–4 werkdagen                   │
│ ⚠ (alleen bij meerdere leveranciers):     │
│ "Je bestelling komt in 2 pakketten."       │
│ Past erbij: Verstelbare riem € 27,95 [+]   │
│ Subtotaal € 36,95 · Verzending € 4,95      │  verzendkosten vóór checkout zichtbaar
│ Totaal incl. btw € 41,90                   │
│ [ Afrekenen ]                              │
│ iDEAL|Wero · Bancontact · Apple Pay · ...  │
```

### Checkout (Shopify, standaard)
- Gastafrekenen staat aan (accounts optioneel).
- Express-knoppen: Apple Pay, Google Pay, Shop Pay.
- Betaalmethoden: iDEAL | Wero, Bancontact, creditcard, Klarna, Apple/Google Pay.
- Nieuwsbrief-vinkje staat **uit** (AVG).
- Bevestiging dat je de AV en het herroepingsrecht hebt gelezen, met links.
- Knoptekst: **"Nu betalen"** (wettelijke eis: een duidelijke betalingsverplichting).

### Over ons
Hero met jou en de hond → het verhaal (waarom Hyggehond) → 3 beloftes (echt getest, snel vanuit Europa, eerlijk en zonder trucs) → hoe we werken (we testen samples en werken met Europese partners) → bedrijfsgegevens.

### FAQ
Zoekveld, en accordeons per thema: bestellen & betalen · verzending · retour & herroeping · producten & maten · Hyggehond. Met FAQ-structured data.

### Contact
Formulier (naam, e-mail, ordernummer, vraag), e-mail, reactietermijn "binnen 1 werkdag", bedrijfsgegevens (naam, adres, KvK, btw-id), link naar track & trace. WhatsApp volgt later (fase 2).

### Track & trace
Invoer van ordernummer + e-mail, met daarna de status per pakket (meerdere pakketten zichtbaar). Uitleg: "Je ontvangt per pakket een e-mail met de trackinglink." Technisch via de Shopify-bestelstatuspagina of een tracking-app (stap 6).

### Herroepen (herroepingsknop)
Sinds **19 juni 2026** moeten webshops een online **herroepingsfunctie** hebben (Richtlijn (EU) 2023/2673, art. 11a Richtlijn consumentenrechten). Dat is een duidelijk zichtbare knop, bijvoorbeeld "Overeenkomst hier herroepen". Opbouw: het formulier vraagt naam, ordernummer, e-mail en (optioneel) welke producten → knop **"Herroeping bevestigen"** → de klant ontvangt direct een ontvangstbevestiging per e-mail. De link staat in de footer, in de orderbevestiging en op de bestelstatuspagina.

### Blog (Journal)
Overzicht in 2 kolommen. In elk artikel: inhoudsopgave, 1–2 productblokken (contextueel, geen agressieve pop-ups) en "Lees ook".

## Prestatie en toegankelijkheid (geldt voor alle pagina's)
- LCP < 2,5 s: geen slider; de hero-afbeelding als WebP met `fetchpriority="high"`; maximaal 6 apps met front-end scripts.
- Toetsenbord: zichtbare focusstijl, een skip-link en een drawer die met Esc sluit.
- Alt-tekst op alle productfoto's; formulieren met labels; foutmeldingen in tekst, niet alleen in kleur.
- Klikdoelen ≥ 44 × 44 px; lettergrootte ≥ 16 px op mobiel.
