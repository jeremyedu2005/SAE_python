# SAE 15 traitement des données

[Demo](https://jeremyedu2005.github.io/SAE_python/)

## Description

Ce site a été développé pendant ma première année universitaire de BUT Réseaux et Télécommunications, dans le cadre de la SAE 15 sur le traitement des données.

Le projet consiste à traiter un fichier CSV recensant les interventions des pompiers en France sur l'année 2021, et à en extraire 5 types d'interventions pour la région Île-de-France (ainsi qu'un cas particulier pour les secours en mer, à l'échelle nationale) :

Fausses alertes
Odeurs / fuites de gaz
Accidents de circulation
Accidents sur voie publique
Secours en mer (FDSM)

Pour chaque intervention, un script Python génère automatiquement une page HTML contenant un tableau récapitulatif par département ainsi qu'un graphique en bâtons (Chart.js), accompagnés d'une brève analyse personnelle des résultats.

## Fonctionnalités

.Génération automatique des pages HTML à partir du CSV via Python
.Visualisation des données sous forme de tableaux et de graphiques interactifs (Chart.js)
.Site responsive (menu hamburger en dessous de 1080px)
.Page de mentions légales, accessible depuis chaque page du site

## Arborescence

```text
SAE_python/
├── accident_circulation/
│   └── accident_de_circulation.html
├── accident_voie_publique/
│   └── accidents_voie_publique.html
├── alertes/
│   └── alertes.html
├── data/
│   └── interventions_2021.csv
├── description/
│   └── description.html
├── fuites/
│   └── fuites_gaz.html
├── img/
│   ├── croix.svg
│   ├── menu.svg
│   └── pompier.jpg
├── secours_mers/
│   └── secours_en_mer.html
├── brouillons_interventions_2021.py
├── index.html
├── interventions_2021.css
├── main_interventions_2021.py
└── mentions_legales.html
```
## Technologies utilisées

.🐍Python 3 (module csv) pour le traitement des données et la génération du HTML
.HTML5 / CSS3 (Flexbox, media queries) pour la structure et le design responsive
.JavaScript (vanilla) pour le menu hamburger
.Chart.js pour les graphiques en bâtons

## Lancer le projet en local

1.Cloner le dépôt :
git clone https://github.com/jeremyedu2005/SAE_python.git

2. Depuis la racine du projet, exécuter le script Python pour générer les pages HTML :
python main_interventions_2021.py

3.Ouvrir index.html dans un navigateur (ou avec l'extension Live Server de VS Code).

## Auteur

RAODSON Miaro Jérémy Étudiant en BUT MMI (Métiers du Multimédia et de l'Internet) à l'IUT de Bobigny, Université Sorbonne Paris Nord
