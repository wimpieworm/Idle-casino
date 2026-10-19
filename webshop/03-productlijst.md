# Stap 3 — Productlijst met calculatie (Hyggehond)

Gegenereerd door `webshop/data/producten.py`; wijzig daar en draai het script opnieuw.

**Aannames**

- Verkoopprijs incl. 21% btw (alle hondenaccessoires vallen onder 21%; er zijn geen 9%-producten zoals voeding).
- Inkoop = **doelinkoopprijs excl. btw** bij een EU-leverancier. Btw op inkoop is aftrekbaar, en bij ES/DE-leveranciers geldt btw-verlegging.
- Verzend = wat de leverancier per order rekent. Wij rekenen conservatief, alsof de verzending voor de klant gratis is.
- Betaalkosten = 1,9% + € 0,25 (gemengd iDEAL/Wero, Bancontact, kaart, Klarna).
- Retourreservering = retour% × (verzend + € 2 handling + 20% afschrijving op inkoop). De klant betaalt zelf de retourzending (zo vermeld in het retourbeleid), behalve bij een defect of een verkeerde levering.
- Brutomarge = (excl. btw − inkoop − verzend − betaalkosten − retourreservering) / excl. btw. Advertentiekosten zitten hier niet in (zie stap 7).
- **Max. inkoop** = de hoogste inkoopprijs waarbij het product nog 40% marge haalt. Leg leveranciersoffertes hiernaast.

| # | Product | Variant | Inkoop | Verzend | Verkoop incl. | Excl. btw | Betaalk. | Retour% | Retourres. | Winst | **Marge** | Max. inkoop |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Orthopedische hondenmand Rust | S – 70 x 50 cm | € 24,00 | € 7,95 | € 74,95 | € 61,94 | € 1,67 | 8% | € 1,18 | € 27,14 | **43,8%** | € 26,32 |
| 1 | Orthopedische hondenmand Rust | M – 90 x 65 cm | € 32,00 | € 9,50 | € 94,95 | € 78,47 | € 2,05 | 8% | € 1,43 | € 33,49 | **42,7%** | € 34,06 |
| 1 | Orthopedische hondenmand Rust | L – 110 x 80 cm | € 42,00 | € 11,50 | € 119,95 | € 99,13 | € 2,53 | 8% | € 1,75 | € 41,35 | **41,7%** | € 43,67 |
| 2 | Donutmand Nest | S – Ø 50 cm | € 14,00 | € 6,95 | € 47,95 | € 39,63 | € 1,16 | 6% | € 0,70 | € 16,81 | **42,4%** | € 14,95 |
| 2 | Donutmand Nest | M – Ø 70 cm | € 19,00 | € 7,95 | € 59,95 | € 49,55 | € 1,39 | 6% | € 0,82 | € 20,38 | **41,1%** | € 19,56 |
| 2 | Donutmand Nest | L – Ø 90 cm | € 26,00 | € 9,50 | € 79,95 | € 66,07 | € 1,77 | 6% | € 1,00 | € 27,80 | **42,1%** | € 27,36 |
| 3 | Hondenplaid Teddy – waterafstotend | 100 x 75 cm | € 8,00 | € 4,95 | € 29,95 | € 24,75 | € 0,82 | 4% | € 0,34 | € 10,64 | **43,0%** | € 8,73 |
| 3 | Hondenplaid Teddy – waterafstotend | 150 x 100 cm | € 12,00 | € 5,95 | € 39,95 | € 33,02 | € 1,01 | 4% | € 0,41 | € 13,64 | **41,3%** | € 12,43 |
| 4 | Benchkussen met antislip | S – 60 x 45 cm | € 10,00 | € 5,95 | € 39,95 | € 33,02 | € 1,01 | 6% | € 0,60 | € 15,46 | **46,8%** | € 12,23 |
| 4 | Benchkussen met antislip | M – 75 x 55 cm | € 13,00 | € 6,95 | € 49,95 | € 41,28 | € 1,20 | 6% | € 0,69 | € 19,44 | **47,1%** | € 15,89 |
| 4 | Benchkussen met antislip | L – 90 x 60 cm | € 17,00 | € 7,95 | € 59,95 | € 49,55 | € 1,39 | 6% | € 0,80 | € 22,41 | **45,2%** | € 19,56 |
| 5 | Autostoel voor kleine honden | Universeel – tot 8 kg | € 18,00 | € 7,95 | € 59,95 | € 49,55 | € 1,39 | 7% | € 0,95 | € 21,26 | **42,9%** | € 19,42 |
| 6 | Waterdichte autostoelhoes achterbank | Universeel | € 16,00 | € 7,95 | € 54,95 | € 45,41 | € 1,29 | 5% | € 0,66 | € 19,51 | **43,0%** | € 17,33 |
| 7 | Y-tuig zacht gevoerd | XS | € 9,00 | € 4,95 | € 34,95 | € 28,88 | € 0,91 | 12% | € 1,05 | € 12,97 | **44,9%** | € 10,38 |
| 7 | Y-tuig zacht gevoerd | S | € 9,00 | € 4,95 | € 34,95 | € 28,88 | € 0,91 | 12% | € 1,05 | € 12,97 | **44,9%** | € 10,38 |
| 7 | Y-tuig zacht gevoerd | M | € 10,00 | € 4,95 | € 36,95 | € 30,54 | € 0,95 | 12% | € 1,07 | € 13,56 | **44,4%** | € 11,31 |
| 7 | Y-tuig zacht gevoerd | L | € 11,00 | € 4,95 | € 39,95 | € 33,02 | € 1,01 | 12% | € 1,10 | € 14,96 | **45,3%** | € 12,71 |
| 8 | Verstelbare riem biothane – 2 m | Standaard | € 7,00 | € 4,95 | € 27,95 | € 23,10 | € 0,78 | 4% | € 0,33 | € 10,03 | **43,4%** | € 7,79 |
| 9 | Halsband biothane | S – 25–35 cm | € 5,00 | € 4,95 | € 22,95 | € 18,97 | € 0,69 | 8% | € 0,64 | € 7,69 | **40,6%** | € 5,11 |
| 9 | Halsband biothane | M – 33–45 cm | € 5,00 | € 4,95 | € 22,95 | € 18,97 | € 0,69 | 8% | € 0,64 | € 7,69 | **40,6%** | € 5,11 |
| 9 | Halsband biothane | L – 42–55 cm | € 6,00 | € 4,95 | € 24,95 | € 20,62 | € 0,72 | 8% | € 0,65 | € 8,29 | **40,2%** | € 6,05 |
| 10 | Regenjas reflecterend | S – rug 30 cm | € 11,00 | € 4,95 | € 39,95 | € 33,02 | € 1,01 | 14% | € 1,28 | € 14,78 | **44,8%** | € 12,53 |
| 10 | Regenjas reflecterend | M – rug 40 cm | € 12,00 | € 4,95 | € 42,95 | € 35,50 | € 1,07 | 14% | € 1,31 | € 16,17 | **45,6%** | € 13,92 |
| 10 | Regenjas reflecterend | L – rug 50 cm | € 13,00 | € 4,95 | € 44,95 | € 37,15 | € 1,10 | 14% | € 1,34 | € 16,76 | **45,1%** | € 14,85 |
| 10 | Regenjas reflecterend | XL – rug 60 cm | € 14,00 | € 4,95 | € 47,95 | € 39,63 | € 1,16 | 14% | € 1,37 | € 18,15 | **45,8%** | € 16,24 |
| 11 | Wandelset drinkfles + opvouwbare bak | Standaard | € 7,00 | € 4,95 | € 27,95 | € 23,10 | € 0,78 | 4% | € 0,33 | € 10,03 | **43,4%** | € 7,79 |
| 12 | Poepzakhouder + 120 composteerbare zakjes | Standaard | € 3,50 | € 3,50 | € 19,95 | € 16,49 | € 0,63 | 2% | € 0,12 | € 8,73 | **53,0%** | € 5,63 |
| 13 | Snoepjestas voor training | Standaard | € 6,00 | € 3,95 | € 22,95 | € 18,97 | € 0,69 | 3% | € 0,21 | € 8,12 | **42,8%** | € 6,53 |
| 14 | Sleeplijn biothane – 10 m | 10 meter | € 12,00 | € 4,95 | € 39,95 | € 33,02 | € 1,01 | 4% | € 0,37 | € 14,68 | **44,5%** | € 13,47 |
| 15 | Slowfeeder voerbak | Standaard – 500 ml | € 6,00 | € 4,95 | € 24,95 | € 20,62 | € 0,72 | 3% | € 0,24 | € 8,70 | **42,2%** | € 6,45 |
| 16 | Keramische voerbakken op bamboe standaard | Set van 2 – verhoogd | € 14,00 | € 7,95 | € 49,95 | € 41,28 | € 1,20 | 6% | € 0,77 | € 17,37 | **42,1%** | € 14,84 |
| 17 | Likmat set van 2 | Set van 2 | € 4,00 | € 3,95 | € 17,95 | € 14,83 | € 0,59 | 2% | € 0,14 | € 6,16 | **41,5%** | € 4,22 |
| 18 | Snuffelmat | Standaard – 45 x 45 cm | € 9,00 | € 4,95 | € 32,95 | € 27,23 | € 0,88 | 3% | € 0,26 | € 12,14 | **44,6%** | € 10,24 |
| 19 | Puzzelspeelgoed niveau 2 | Standaard | € 8,00 | € 4,95 | € 29,95 | € 24,75 | € 0,82 | 3% | € 0,26 | € 10,73 | **43,3%** | € 8,82 |
| 20 | Touwspeelgoed set katoen (3-delig) | Set van 3 | € 5,00 | € 3,95 | € 19,95 | € 16,49 | € 0,63 | 2% | € 0,14 | € 6,77 | **41,1%** | € 5,17 |
| 21 | Kauwbal natuurrubber | M – Ø 6 cm | € 5,00 | € 3,95 | € 19,95 | € 16,49 | € 0,63 | 2% | € 0,14 | € 6,77 | **41,1%** | € 5,17 |
| 21 | Kauwbal natuurrubber | L – Ø 8 cm | € 6,00 | € 3,95 | € 22,95 | € 18,97 | € 0,69 | 2% | € 0,14 | € 8,19 | **43,2%** | € 6,60 |
| 22 | Deshedding borstel | Standaard | € 6,00 | € 3,95 | € 24,95 | € 20,62 | € 0,72 | 3% | € 0,21 | € 9,73 | **47,2%** | € 7,47 |
| 23 | Pootreiniger | M | € 5,00 | € 4,95 | € 22,95 | € 18,97 | € 0,69 | 3% | € 0,24 | € 8,09 | **42,7%** | € 5,50 |
| 23 | Pootreiniger | L | € 6,00 | € 4,95 | € 24,95 | € 20,62 | € 0,72 | 3% | € 0,24 | € 8,70 | **42,2%** | € 6,45 |
| 24 | Hondenbadjas microvezel | S | € 9,00 | € 4,95 | € 34,95 | € 28,88 | € 0,91 | 10% | € 0,88 | € 13,15 | **45,5%** | € 10,56 |
| 24 | Hondenbadjas microvezel | M | € 10,00 | € 4,95 | € 36,95 | € 30,54 | € 0,95 | 10% | € 0,90 | € 13,74 | **45,0%** | € 11,50 |
| 24 | Hondenbadjas microvezel | L | € 11,00 | € 4,95 | € 39,95 | € 33,02 | € 1,01 | 10% | € 0,92 | € 15,14 | **45,9%** | € 12,90 |
| 25 | Speelgoedmand vilt | Standaard – Ø 35 cm | € 9,00 | € 6,95 | € 34,95 | € 28,88 | € 0,91 | 3% | € 0,32 | € 11,70 | **40,5%** | € 9,14 |
| 26 | Cadeauset Nieuwe pup | XS-tuig | € 27,00 | € 5,95 | € 89,95 | € 74,34 | € 1,96 | 4% | € 0,53 | € 38,90 | **52,3%** | € 36,09 |
| 26 | Cadeauset Nieuwe pup | S-tuig | € 27,00 | € 5,95 | € 89,95 | € 74,34 | € 1,96 | 4% | € 0,53 | € 38,90 | **52,3%** | € 36,09 |

**26 producten, 46 varianten. Gemiddelde brutomarge: 44,0%. Alle varianten ≥ 40%.**

## Collecties

- **Rust & slapen**: Orthopedische hondenmand Rust, Donutmand Nest, Hondenplaid Teddy – waterafstotend, Benchkussen met antislip
- **Op pad**: Autostoel voor kleine honden, Waterdichte autostoelhoes achterbank, Y-tuig zacht gevoerd, Verstelbare riem biothane – 2 m, Halsband biothane, Regenjas reflecterend, Wandelset drinkfles + opvouwbare bak, Poepzakhouder + 120 composteerbare zakjes, Snoepjestas voor training, Sleeplijn biothane – 10 m
- **Eten & drinken**: Slowfeeder voerbak, Keramische voerbakken op bamboe standaard, Likmat set van 2
- **Spelen & verrijking**: Snuffelmat, Puzzelspeelgoed niveau 2, Touwspeelgoed set katoen (3-delig), Kauwbal natuurrubber
- **Verzorging**: Deshedding borstel, Pootreiniger, Hondenbadjas microvezel
- **Thuis**: Speelgoedmand vilt
- **Cadeaus**: Cadeauset Nieuwe pup

## Bestsellers voor de homepage (verwachting)
1. Orthopedische hondenmand Rust (hoogste orderwaarde, Q4)
2. Y-tuig zacht gevoerd + verstelbare riem biothane (cross-sell-duo)
3. Snuffelmat en likmat (impulsaankopen, vuurwerkperiode)
4. Cadeauset Nieuwe pup (cadeauseizoen)

## Bewust niet in het assortiment
- Voeding, snacks, supplementen en medicijnen (aparte regelgeving, 9% btw, houdbaarheid)
- Elektrische producten zoals GPS-trackers en lichtgevende halsbanden met batterij (CE/RED/EMC, WEEE en batterijregels)
- Stroom- en prikhalsbanden (omstreden en deels verboden)
- Koelmat met gel: seizoensproduct voor april, eerst de veiligheidsinformatie van de leverancier toetsen

## Fotomateriaal-checklist (per product)
Bestel samples van alle producten met een orderwaarde boven € 30 en van de top 5 (budget € 200). Fotografeer met je eigen hond.

- [ ] Packshot op een rustige, lichte achtergrond (zand/crème), 2048 × 2048 px, vierkant
- [ ] Sfeerfoto in huis of op pad **met je eigen hond** (daglicht, geen flits)
- [ ] Detailfoto's: materiaal, naden, sluitingen en label (ook als bewijs voor GPSR)
- [ ] Maatfoto: product met een meetlint of naast een bekend object; bij manden de hond erin liggend
- [ ] Korte video van 10–20 s, verticaal 9:16 (gebruik, bijvoorbeeld de hond die gaat liggen of de riem verstellen); te hergebruiken voor TikTok/Reels
- [ ] Foto van het etiket/de verpakking met fabrikantgegevens (archief, GPSR)
- [ ] Alt-tekst geschreven (wat is er te zien, inclusief kleur en maat)
- [ ] Bestandsnaam met zoekwoord, bijv. `orthopedische-hondenmand-rust-zand-m.jpg`
- [ ] Geen leveranciersfoto's met watermerk; leveranciersbeelden alleen gebruiken met schriftelijke toestemming
