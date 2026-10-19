# Klantenservice en operatie

Standaardantwoorden: zie `05-teksten/klantenservice-templates.md`.

## 1. Afspraken met elke leverancier (vastleggen per e-mail vóór de start)
| Situatie | Wie betaalt | Termijn |
|---|---|---|
| Defect of beschadigd bij aankomst | **Leverancier**: vervanging of creditnota inclusief verzending | Claim binnen 7 dagen na melding van de klant, met foto's |
| Verkeerd product geleverd | **Leverancier**: juiste product + retourlabel | Claim binnen 7 dagen |
| Pakket verloren (tracking stopt > 5 werkdagen) | **Leverancier/vervoerder**; jij levert de klant meteen opnieuw | Leverancier start het onderzoek binnen 2 werkdagen |
| Herroeping door de klant (product in orde) | **Klant** betaalt de retourverzending; jij betaalt de klant terug. De leverancier crediteert de inkoop na ontvangst (eventueel minus een restocking fee; spreek die vooraf af) | Leverancier crediteert binnen 14 dagen na ontvangst |
| Retour beschadigd door de klant | Klant (waardevermindering); jij beoordeelt het op basis van de foto's van de leverancier | Leverancier meldt het binnen 3 werkdagen na ontvangst |
| Conformiteitsklacht na de bedenktijd | **Jij** tegenover de klant (wettelijk); verhaal op de leverancier volgens de afspraak (bijv. 12–24 maanden) | Per geval |

**Belangrijk:** tegenover de klant ben **jij** altijd verantwoordelijk, ook als de leverancier traag is. Los het eerst op voor de klant en verhaal het daarna.

## 2. Retourproces (stap voor stap)
1. De klant meldt zich via de herroepingsknop of per e-mail en krijgt een automatische bevestiging.
2. **Binnen 1 werkdag:**
   - Zoek in Shopify de order en de leverancier op (metafield `leverancier`).
   - Vraag het retouradres of RMA-nummer op bij de leverancier.
   - Stuur de klant het retouradres met het ordernummer als kenmerk (template 2).
   - Tag de order "retour".
3. De klant stuurt het product terug en mailt de tracking. Noteer die in de order.
4. Na ontvangst bij de leverancier, of na het verzendbewijs: **terugbetalen in Shopify** (Order → Terugbetalen).
   - Inclusief de standaardverzendkosten als de klant die betaald heeft.
   - Uiterlijk 14 dagen na de herroeping.
   - Doel: binnen 5 werkdagen na ontvangst.
5. Creditnota van de leverancier controleren en de boekhouding bijwerken.
6. Shopify Flow herinnert je op dag 10 als de tag "retour" er nog op staat zonder terugbetaling.

## 3. Klachtenproces
1. Ontvangst bevestigen binnen 2 werkdagen.
2. Classificeren: levering, product, service of anders. Noteer het in de klachtenlog (spreadsheet: datum, order, type, leverancier, oplossing, kosten).
3. Inhoudelijke oplossing binnen 14 dagen. Bij twijfel: kies in het voordeel van de klant als de kosten < € 30 zijn. Een goede review en een terugkerende klant zijn meer waard.
4. Productveiligheidsprobleem (bijv. een sluiting die breekt of een scherp onderdeel)?
   - Product **direct offline**.
   - Leverancier en fabrikant informeren.
   - Bij een ernstig risico: melden via **Safety Business Gateway** (EU) / NVWA. Dat is een GPSR-plicht van de distributeur.
   - Klanten die het product hebben gekocht informeren.

## 4. Wekelijkse check (elke maandag, ca. 45 minuten)
| Onderdeel | Wat | Actie bij afwijking |
|---|---|---|
| **Levertijd per leverancier** | Gemiddelde dagen order → bezorgd (Parcel Panel / Shopify-rapport) | > 5 werkdagen: leverancier aanspreken; 2 weken op rij: levertijd op de site aanpassen of een alternatief zoeken |
| **Uitval** | Orders geannuleerd door "niet op voorraad" | > 2% : sync-frequentie controleren, product verwijderen |
| **Klachten en retouren** | Aantal, % per product, redenen | Retour > 10% bij een product: maatgids/tekst verbeteren of product vervangen |
| **Marges** | Inkoopprijswijzigingen in Syncee; `producten.py` opnieuw draaien met de nieuwe inkoop | Marge < 40%: prijs aanpassen (nooit met een nep-"van"-prijs) of product vervangen |
| **Advertenties** | Spend, CPA, ROAS per kanaal en creative | Zie de regels in stap 7 |
| **Reviews** | Nieuwe reviews; alle reviews beantwoorden (ook de positieve) | Negatief: binnen 1 werkdag contact opnemen |
| **Voorraad en sync** | Producten op concept door 0 voorraad | Weer op actief zetten als ze terug zijn; zo niet binnen 14 dagen, vervangen |
| **Financiën** | Shopify-uitbetalingen vs. leveranciersafschrijvingen; buffer > € 100? | Buffer te laag: advertentiebudget verlagen |
| **Btw-drempel BE** | Totaal EU-afstandsverkopen dit jaar | > € 8.000: OSS-registratie voorbereiden |

## 5. Maandelijks
- Leveranciers beoordelen (score 1–5 op levertijd, kwaliteit, communicatie en retour). De slechtste leverancier krijgt een verbetergesprek of wordt vervangen.
- Btw-administratie en facturen naar de boekhouder.
- Productassortiment: 2 slechtst verkopende producten eruit, 2 nieuwe testen (seizoen: koelmat in april, regenjas in september).
- PageSpeed-meting opnieuw doen na wijzigingen aan apps of het thema.
