# E-commerce Performance Dashboard - Power BI

Projet Power BI d'analyse e-commerce base sur un jeu de donnees synthetique genere localement.

## Apercu du dashboard

![Apercu du dashboard Power BI](Capture%20d%27%C3%A9cran%202026-04-30%20053418.png)

## Objectif

Analyser la performance d'un site e-commerce sur la periode 2025-2026 : acquisition, tunnel de conversion, chiffre d'affaires, marge, retours et performance par produit.

## Perimetre d'analyse

Le dashboard permet de suivre :

- les sessions et vues produit ;
- les ajouts au panier ;
- les passages au checkout ;
- les commandes ;
- le chiffre d'affaires ;
- la marge brute ;
- le cout d'acquisition ;
- le taux de conversion ;
- le taux de retour ;
- la performance par canal, pays, device, categorie et produit.

## Donnees

Les donnees sont fictives et generees avec le script :

```text
scripts/generate_ecommerce_dataset.py
```

Fichier principal :

```text
data/ecommerce_performance_2025_2026.csv
```

Le dataset contient plus de 120 000 lignes et couvre plusieurs dimensions : date, pays, canal d'acquisition, device, categorie, produit et indicateurs commerciaux.

## Structure

```text
power_bi_ecomerce/
|-- README.md
|-- Capture d'écran 2026-04-30 053418.png
|-- data/
|   `-- ecommerce_performance_2025_2026.csv
|-- docs/
|   |-- data-dictionary.md
|   |-- dashboard-spec.md
|   |-- rebuild-power-bi.md
|   `-- project-report.md
|-- power-bi/
|   |-- PowerBI_Ecommerce_Performance_Walid.pbix
|   `-- dax-measures.md
`-- scripts/
    `-- generate_ecommerce_dataset.py
```

## Pages recommandees dans Power BI

| Page | Objectif |
| --- | --- |
| Vue executif | KPI globaux : CA, commandes, conversion, marge, cout d'acquisition |
| Tunnel de conversion | Sessions, vues produit, panier, checkout, commandes |
| Performance produits | Analyse par categorie et produit |
| Acquisition | Comparaison SEO, SEA, Email, Social Ads, Direct, Affiliation |
| Rentabilite | Marge brute, cout d'acquisition, retours et ROAS |

## Mesures DAX

Les mesures proposees sont documentees dans :

```text
power-bi/dax-measures.md
```

## Rapport de projet

Le detail du travail realise dans Power Query, DAX, la modelisation et la visualisation est documente ici :

```text
docs/project-report.md
```

## Statut

Le projet contient le dataset synthetique, la documentation, les mesures DAX et le fichier Power BI final.

## Confidentialite

Aucune donnee personnelle ou donnee d'entreprise reelle n'est presente dans ce projet.
