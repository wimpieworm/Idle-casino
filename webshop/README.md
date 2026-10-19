# Hyggehond: dropshipping-webshop NL/BE

Premium hondenaccessoires, Shopify, EU-leveranciers. Rechtspersoon: Dylan Smit Holding B.V. (h.o.d.n. Hyggehond).

| Stap | Document |
|---|---|
| 0 | [Nichekeuze](00-nichekeuze.md) · [Budget, rechtsvorm en naam](00b-budget-entiteit-naam.md) |
| 1 | [Marktanalyse + 3 concurrenten](01-marktanalyse.md) |
| 2 | [Leveranciersvergelijking](02-leveranciers.md) |
| 3 | [Productlijst met calculatie](03-productlijst.md) · generator [`data/producten.py`](data/producten.py) · import [`data/shopify-producten.csv`](data/shopify-producten.csv) |
| 4 | [Sitemap + wireframes + merkstijl](04-sitemap-wireframes.md) |
| 5 | Teksten: [pagina's](05-teksten/paginateksten.md) · [producten](05-teksten/productteksten.md) · [juridisch (concept)](05-teksten/juridisch/) · [blog](05-teksten/blog/) · [e-mailflows](05-teksten/emailflows.md) · [SEO](05-teksten/seo-zoekwoorden.md) · [klantenservice](05-teksten/klantenservice-templates.md) |
| 6 | [Technische setup stap voor stap](06-technische-setup/README.md) · [thema-snippets](06-technische-setup/theme/snippets/) |
| 7 | [Lanceringschecklist + 30-dagenplan](07-lancering.md) |
| — | [Klantenservice en operatie (retouren, leveranciers, wekelijkse check)](08-klantenservice-operatie.md) |

## Jouw to-do's (die ik niet voor je kan doen)
1. Domein `hyggehond.nl` + `.be` registreren; BOIP-check; social handles claimen
2. Handelsnaam bij KvK toevoegen; btw-status van de holding checken met je boekhouder
3. Shopify- en Syncee-account aanmaken; leveranciers kiezen; GPSR-gegevens + samples aanvragen (e-mailsjabloon in stap 2)
4. Fotograferen met je hond (checklist in stap 3)
5. Juridische concepten laten nakijken en placeholders invullen
6. Setup volgen (stap 6) en de lanceringschecklist afwerken (stap 7)

Echte inkoopprijzen? Pas ze aan in `data/producten.py` en draai `python3 webshop/data/producten.py`. Tabel, teksten en CSV worden dan opnieuw gegenereerd.
