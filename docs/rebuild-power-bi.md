# Rebuild Power BI

Ce guide explique comment finaliser un rapport Power BI original avec le nouveau dataset.

## 1. Creer ou ouvrir le rapport

Dans Power BI Desktop, creer un nouveau rapport ou ouvrir un brouillon local non publie.

Le fichier PBIX final ne doit etre ajoute au depot qu'apres avoir ete reconnecte au nouveau dataset et refait selon cette specification.

## 2. Importer la source de donnees

Importer le CSV :

```text
data/ecommerce_performance_2025_2026.csv
```

Verifier les types :

- `date` en Date ;
- indicateurs de volume en nombres entiers ;
- `prix_unitaire`, `taux_remise`, `chiffre_affaires`, `marge_brute`, `cout_acquisition` en nombres decimaux.

Renommer la table :

```text
ecommerce_performance_2025_2026
```

## 3. Creer les mesures

Ajouter les mesures du fichier :

```text
power-bi/dax-measures.md
```

## 4. Refaire les pages

Construire les pages decrites dans :

```text
docs/dashboard-spec.md
```

## 5. Verification

Avant publication, verifier :

- les filtres fonctionnent ;
- les KPI ne sont pas vides ;
- le taux de conversion est coherent ;
- les visuels affichent bien les donnees 2025-2026 ;
- le rapport n'utilise plus l'ancien CSV `GeneratedEcommerceData.csv`.

## 6. Ajouter le PBIX final

Quand le rapport est reconstruit, enregistrer le fichier sous :

```text
power-bi/PowerBI_Ecommerce_Performance_Walid.pbix
```

Puis retirer temporairement la ligne `power-bi/*.pbix` du `.gitignore` si le fichier doit etre publie sur GitHub.
