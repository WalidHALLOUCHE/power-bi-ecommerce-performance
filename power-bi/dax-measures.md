# Mesures DAX proposees

Table principale : `ecommerce_performance_2025_2026`

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
Taux conversion = DIVIDE([Commandes], [Sessions])
```

```DAX
Taux ajout panier = DIVIDE([Ajouts panier], [Vues produit])
```

```DAX
Taux checkout = DIVIDE([Passages checkout], [Ajouts panier])
```

```DAX
Taux retour = DIVIDE(SUM(ecommerce_performance_2025_2026[retours]), [Commandes])
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
