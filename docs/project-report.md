# Rapport de projet - Refonte du dashboard Performance E-commerce

## 1. Travail realise dans Power Query

L'ancienne source de donnees du rapport Power BI a ete remplacee par un nouveau fichier CSV :

```text
data/ecommerce_performance_2025_2026.csv
```

L'objectif etait de stabiliser l'actualisation du rapport, d'eviter les chemins locaux obsoletes et de repartir sur un jeu de donnees synthetique maitrise.

### Nettoyage et typage

La requete principale a ete corrigee pour pointer vers le nouveau CSV. Les en-tetes ont ete promus et les types de donnees ont ete adaptes :

- `date` en type Date ;
- indicateurs de volume en nombres entiers : sessions, vues produit, ajouts panier, commandes ;
- indicateurs financiers en nombres decimaux : chiffre d'affaires, marge brute, cout d'acquisition ;
- dimensions analytiques en texte : pays, canal, device, categorie, produit.

### Calendrier

Les requetes `minDate`, `maxDate` et `Calendrier` ont ete corrigees pour utiliser la nouvelle colonne `date`. Cette table calendrier sert de base aux analyses temporelles : mois en cours, trimestre en cours, tendances hebdomadaires et comparaisons de periode.

## 2. Modelisation et intelligence de donnees

La structure du modele a ete adaptee pour rendre le rapport plus dynamique et plus robuste.

### Parametres de champs

Les parametres de champs ont ete francises et repares :

- `MTD-QTD Selection` permet de basculer entre mois en cours et trimestre en cours ;
- `M-W-D` permet de changer la granularite d'analyse : mensuel, hebdomadaire ou quotidien ;
- `KPI_#1` permet de choisir dynamiquement l'indicateur affiche sur les courbes de tendance.

### Nettoyage du modele

Les champs obsoletes restes apres migration ont ete identifies et retires des filtres et visuels. Cela evite les erreurs de modele et garantit que les visuels utilisent uniquement les champs du nouveau dataset.

## 3. Travail realise en DAX

Les mesures ont ete adaptees au nouveau modele de donnees en francais.

### KPIs de base

Les indicateurs principaux couvrent le tunnel de conversion :

- vues produit ;
- ajouts panier ;
- passages checkout ;
- commandes ;
- unites vendues ;
- chiffre d'affaires ;
- marge brute ;
- cout d'acquisition.

### Time intelligence

Des mesures de comparaison temporelle ont ete mises en place pour analyser les variations entre periode courante et periode precedente :

- MTD vs PMTD ;
- QTD vs PQTD ;
- variation absolue ;
- variation en pourcentage.

### Indicateur d'alerte SVG

Une mesure avancee de mise en forme conditionnelle a ete creee pour afficher une alerte visuelle uniquement lorsque la performance est negative.

Exemple de logique :

```DAX
KPI_1_ColorConditionalFormatting =
IF(
    [Variation KPI principal %] < 0,
    "data:image/svg+xml;utf8,...",
    BLANK()
)
```

Ce principe permet d'injecter un SVG dans Power BI et d'afficher un point rouge dynamique lorsque l'indicateur choisi baisse.

## 4. Visualisation et design

L'interface a ete retravaillee pour proposer un rendu clair, lisible et oriente decision.

### Rendu SVG

Les mesures SVG ont ete configurees en tant qu'URL d'image afin que Power BI les interprete comme des elements graphiques et non comme du texte brut.

### Optimisation des matrices

Les matrices ont ete ajustees pour ameliorer la lisibilite :

- colonnes renommees avec un espace lorsque le titre n'etait pas utile ;
- reduction de largeur pour les colonnes d'alerte ;
- taille des images ajustee autour de 15 a 20 px ;
- alignement des indicateurs visuels avec les libelles.

### Mise en forme conditionnelle

La mise en forme conditionnelle permet de faire ressortir les baisses de performance :

- icones de baisse ;
- texte colore en rouge ;
- alertes SVG ;
- lecture immediate des variations negatives.

### Interactions entre visuels

Les interactions de filtrage ont ete revues afin que les tableaux et graphiques restent coherents lors de la selection d'un canal, d'un produit, d'un pays ou d'une periode.

## Resume final

Le projet transforme un rapport Power BI e-commerce en dashboard metier francise, reconnecte a un dataset synthetique original et structure autour d'indicateurs de performance.

Le travail couvre toute la chaine Power BI :

- preparation des donnees dans Power Query ;
- modelisation ;
- calendrier et intelligence temporelle ;
- mesures DAX ;
- indicateurs SVG ;
- design et interactions ;
- documentation technique.

Le resultat est un dashboard e-commerce exploitable pour analyser le tunnel de conversion, la performance produit, les canaux d'acquisition et la rentabilite.
