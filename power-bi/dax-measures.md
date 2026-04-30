# Mesures DAX principales

Ce fichier documente les mesures DAX essentielles du projet Power BI.

Table principale du dataset : `ecommerce_performance_2025_2026`

Le fichier `.pbix` utilise aussi une table technique de mesures nommee `# Measures` pour les indicateurs dynamiques, les mesures MTD/QTD et certains visuels SVG.

## 1. Mesures de base du dataset

Ces mesures sont directement basees sur les colonnes du CSV `data/ecommerce_performance_2025_2026.csv`.

```DAX
Sessions = SUM(ecommerce_performance_2025_2026[sessions])
```

```DAX
Vues produit = SUM(ecommerce_performance_2025_2026[vues_produit])
```

```DAX
Ajouts panier = SUM(ecommerce_performance_2025_2026[ajouts_panier])
```

```DAX
Passages checkout = SUM(ecommerce_performance_2025_2026[passages_checkout])
```

```DAX
Commandes = SUM(ecommerce_performance_2025_2026[commandes])
```

```DAX
Unites vendues = SUM(ecommerce_performance_2025_2026[unites_vendues])
```

```DAX
Chiffre affaires = SUM(ecommerce_performance_2025_2026[chiffre_affaires])
```

```DAX
Marge brute = SUM(ecommerce_performance_2025_2026[marge_brute])
```

```DAX
Cout acquisition = SUM(ecommerce_performance_2025_2026[cout_acquisition])
```

```DAX
Retours = SUM(ecommerce_performance_2025_2026[retours])
```

## 2. Taux et ratios metier

```DAX
Taux conversion = DIVIDE([Commandes], [Sessions])
```

```DAX
Taux ajout panier = DIVIDE([Ajouts panier], [Vues produit])
```

```DAX
Taux checkout = DIVIDE([Passages checkout], [Ajouts panier])
```

```DAX
Taux retour = DIVIDE([Retours], [Commandes])
```

```DAX
Panier moyen = DIVIDE([Chiffre affaires], [Commandes])
```

```DAX
Marge moyenne commande = DIVIDE([Marge brute], [Commandes])
```

```DAX
Cout acquisition commande = DIVIDE([Cout acquisition], [Commandes])
```

```DAX
ROAS = DIVIDE([Chiffre affaires], [Cout acquisition])
```

```DAX
Marge nette estimee = [Marge brute] - [Cout acquisition]
```

## 3. Mesures dynamiques utilisees dans le PBIX

Les visuels du fichier `PowerBI_Ecommerce_Performance_Walid.pbix` referencent aussi les mesures suivantes dans la table `# Measures`.

Ces mesures servent surtout aux comparaisons temporelles, aux KPI dynamiques et a la mise en forme visuelle :

```text
Vues produit
Vues produit MTD/QTD
Ajouts panier MTD/QTD
Achats MTD/QTD
Page_Views_MTD/QTD
Adds_to_Cart_MTD/QTD
Purchases_MTD/QTD
Number_of_Products_Purchased_MTD/QTD
Conversion_Rate_MTD/QTD
Conversion_Rate_PMTD/PQTD
Conversion_Rate_%Delta
KPI_1
Variation KPI principal %
KPI_1_ColorConditionalFormatting
Barre performance SVG
Conversion Rate Gauge SVG MTD/QTD
Trend Line Title
```

## 4. Formules avancees extraites du PBIX

Certaines formules avancees sont visibles dans les scripts internes du `.pbix`.

```DAX
Adds_to_Cart = SUM(GeneratedEcommerceData[Adds to Cart])
```

```DAX
Purchases = SUM(GeneratedEcommerceData[Purchases])
```

```DAX
Conversion_Rate_%Delta =
DIVIDE(
    [Conversion_Rate_MTD/QTD] - [Conversion_Rate_PMTD/PQTD],
    [Conversion_Rate_PMTD/PQTD]
)
```

```DAX
Conversion_Rate_MTD/QTD =
IF(
    SELECTEDVALUE('MTD-QTD Selection'[Order]) = 1,
    CALCULATE(
        [Conversion Rate],
        dimDate[MTD] = TRUE()
    ),
    CALCULATE(
        [Conversion Rate],
        dimDate[QTD] = TRUE()
    )
)
```

```DAX
Conversion_Rate_PMTD/PQTD =
VAR _FirstDatePrevtMTD =
    EDATE(MAX(dimDate[FirstOfMonth]), -1)
VAR _LastDatePrevMonth =
    EDATE(MAX(dimDate[Date]), -1)
VAR _Max_Date =
    MAX(dimDate[Date])
VAR _FirstDatePrevtQTD =
    CALCULATE(
        MAX(dimDate[FirstOfMonth]),
        DATEADD(dimDate[Date], -1, QUARTER)
    )
VAR _LastDatePrevQ =
    DATE(YEAR(_Max_Date), MONTH(_FirstDatePrevtQTD), DAY(_Max_Date))
RETURN
IF(
    SELECTEDVALUE('MTD-QTD Selection'[Order]) = 1,
    CALCULATE(
        [Conversion Rate],
        DATESBETWEEN(dimDate[Date], _FirstDatePrevtMTD, _LastDatePrevMonth)
    ),
    CALCULATE(
        [Conversion Rate],
        DATESBETWEEN(dimDate[Date], _FirstDatePrevtQTD, _LastDatePrevQ)
    )
)
```

## 5. Correspondance avec le modele final

Le modele final utilise la table `ecommerce_performance_2025_2026`, mais certaines mesures internes gardent des noms anglais herites du template Power BI.

Correspondances principales :

| Ancien nom / nom technique | Nom metier dans ce projet |
| --- | --- |
| `Page_Views` | `Vues produit` |
| `Adds_to_Cart` | `Ajouts panier` |
| `Purchases` | `Commandes` |
| `Number_of_Products_Purchased` | `Unites vendues` |
| `Conversion Rate` | `Taux conversion` |

Pour GitHub, les mesures de base et les ratios des sections 1 et 2 sont les plus importantes a documenter. Les mesures de la section 3 expliquent pourquoi le `.pbix` contient aussi des noms techniques visibles dans les visuels.
