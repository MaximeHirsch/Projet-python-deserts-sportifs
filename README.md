# Infrastructures Sportives en France Métropolitaine

Par Maxime Hirsch et Baptiste Leloup, 2025.

**https://maximehirsch.github.io/Projet-python-deserts-sportifs/**

## Table des matières

1. [Définitions](#1-définitions)
2. [Objectifs](#2-objectifs)
3. [Sources des données](#3-sources-des-données)
4. [Présentation du dépôt](#4-présentation-du-dépôt)
5. [Visualisation des cartes interactives](#5-visualisation-des-cartes-interactives)
6. [Méthodologie](#6-méthodologie)

---

## 1. Définitions

### Infrastructure sportive

Une infrastructure sportive désigne tout équipement ou installation destiné à la pratique d'activités sportives. Cela inclut les terrains de football, courts de tennis, piscines, gymnases, stades, city-stades ...

(Source : [data.sports.gouv.fr](https://data.sports.gouv.fr))

### Désert sportif

Zone géographique caractérisée par une faible densité d'infrastructures sportives par rapport à la population, limitant l'accès des habitants à la pratique sportive.

### Revenu médian

Le revenu médian correspond au revenu qui partage la population en deux groupes égaux : la moitié des ménages a un revenu inférieur à ce seuil, l'autre moitié un revenu supérieur.


---

## 2. Objectifs

Ce projet vise à **analyser la répartition des infrastructures sportives en France métropolitaine** et à identifier les facteurs socio-économiques et politiques qui influencent leur distribution.

Plus précisément, nous cherchons à :

1. **Cartographier** la densité des infrastructures sportives par département et commune
2. **Identifier** les éventuels "déserts sportifs" (zones sous-équipées)
3. **Analyser** la corrélation entre infrastructures sportives et :
   - Caractéristiques socio-économiques (revenu médian, population, chômage)
   - Orientation politique des élus (résultats des législatives 2024)
4. **Modéliser** les déterminants du nombre d'infrastructures par commune


---

## 3. Sources des données

Nous nous sommes appuyés sur les sources suivantes :

- **data.sports.gouv.fr** : Base de données des équipements sportifs en France
  - URL : [Équipements sportifs](https://data.sports.gouv.fr/explore/dataset/equipements-sportifs/information/)
  - Variables : type d'équipement, localisation (latitude/longitude), commune, département

- **INSEE** : Données socio-économiques au niveau communal
  - Indicateurs : population (P22_POP), nombre de ménages (P22_MEN), revenu médian (MED21), taux de pauvreté (TP6021), chômage (P22_CHOM1564)
  - URL : [Base comparateur de territoires](https://www.insee.fr/fr/statistiques/2521169)

- **data.gouv.fr** : Résultats des élections législatives 2024 (2nd tour)
  - URL : [Législatives 2024](https://www.data.gouv.fr/fr/datasets/elections-legislatives-des-30-juin-et-7-juillet-2024-resultats-definitifs-du-2nd-tour/)
  - Variables : nuance politique du candidat élu par commune

- **Cartiflette** : Fonds de carte des départements français
  - Source : IGN (EXPRESS-COG-CARTO-TERRITOIRE, 2022)

Les données sont récupérées autant que possible via les API publiques des sources.

---

## 4. Présentation du dépôt

### Fichiers principaux

- **`main.ipynb`** : Notebook Jupyter contenant l'ensemble des analyses
  - Chargement et nettoyage des données
  - Analyses descriptives
  - Visualisations (cartes, graphiques)
  - Analyses statistiques et économétriques
  - Régression Lasso pour sélection de variables

- **`docs/`** : Dossier hébergé sur GitHub Pages contenant les cartes

- **`src`** : Dossier qui contient des scripts python, afin d'alléger le code de main.ipynb



---

## 5. Visualisation des cartes interactives

### Accès en ligne

Les cartes sont **hébergées sur GitHub Pages** et accessibles à l'adresse suivante :

**https://maximehirsch.github.io/Projet-python-deserts-sportifs/**

---

## 6. Méthodologie

#### Analyses descriptives
- Distribution des infrastructures par type
- Statistiques par département
  
#### Cartographie
- Cartes choroplèthes (Folium)
- Cartes de chaleur (HeatMap)
- Visualisations avec GeoPandas et Matplotlib

#### Analyses économétriques

**Régressions linéaires (OLS)**
- Variable dépendante : Nombre d'infrastructures par commune
- Variables explicatives : population, revenu médian, chômage, nuance politique
- Erreurs standard robustes à l'hétéroscédasticité (HC3)

---


