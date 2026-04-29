# Dictionnaire de donnees

Fichier : `data/ecommerce_performance_2025_2026.csv`

## Colonnes temporelles

| Colonne | Type | Description |
| --- | --- | --- |
| `date` | Date | Date d'observation |
| `annee` | Nombre entier | Annee de l'observation |
| `mois` | Texte | Mois au format `YYYY-MM` |

## Dimensions d'analyse

| Colonne | Type | Description |
| --- | --- | --- |
| `pays` | Texte | Pays du trafic e-commerce |
| `canal_acquisition` | Texte | Canal marketing : SEO, SEA, Email, Social Ads, Direct, Affiliation |
| `device` | Texte | Type d'appareil : Mobile, Desktop, Tablet |
| `categorie` | Texte | Categorie produit |
| `produit` | Texte | Nom du produit |

## Indicateurs de tunnel

| Colonne | Type | Description |
| --- | --- | --- |
| `sessions` | Nombre entier | Nombre de visites/session |
| `vues_produit` | Nombre entier | Nombre de vues de fiches produit |
| `ajouts_panier` | Nombre entier | Nombre d'ajouts au panier |
| `passages_checkout` | Nombre entier | Nombre de passages a l'etape checkout |
| `commandes` | Nombre entier | Nombre de commandes validees |
| `unites_vendues` | Nombre entier | Nombre total d'unites vendues |

## Indicateurs financiers

| Colonne | Type | Description |
| --- | --- | --- |
| `prix_unitaire` | Decimal | Prix unitaire catalogue |
| `taux_remise` | Decimal | Taux de remise applique |
| `chiffre_affaires` | Decimal | Chiffre d'affaires net apres remise |
| `marge_brute` | Decimal | Marge brute estimee |
| `cout_acquisition` | Decimal | Cout marketing estime du trafic |
| `retours` | Nombre entier | Nombre de commandes retournees |
