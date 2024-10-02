# Projet 360_Degree_Product_Views

Ce projet est une application web de visualisation de produits à 360 degrés, permettant aux utilisateurs de voir les produits sous tous les angles 

## Aperçu

L'application web 360_Degree_Product_Views offre une expérience immersive pour visualiser des produits en 360. Les utilisateurs peuvent faire pivoter les produits, ajuster les quantités et les ajouter à leur panier.

## Structure du projet

```
360_Degree_Product_Views/
├── index.html
├── README.md
├── requirements.txt
├── script.js
├── styles.css
├── data/
│   ├── images/
│   │   ├── Ball_Cap/
│   │   ├── Shoses/
│   │   ├── triko/
│   │   └── watch/
│   └── preprocessed/
├── notebooks/
│   ├── image_preprocessing.ipynb
│   ├── model_evaluation.ipynb
│   └── stitching_and_reconstruction.ipynb
├── output/
│   ├── ball_cap_360_view.gif
│   ├── stitched_image.jpg
│   └── transformations.npy
└── scripts/
    └── create_360_view.py
```
## Structure du projet

Le répertoire du projet est organisé comme suit :

- **`index.html`** : La page principale du projet.
- **`README.md`** : Ce fichier de documentation.
- **`requirements.txt`** : Liste des dépendances Python nécessaires pour le projet.
- **`script.js`** : Fichier JavaScript pour les interactions côté client.
- **`styles.css`** : Fichier CSS pour le style du projet.
- **`data/`** : Contient les données d'entrée et les images prétraitées.
  - **`images/`** : Images originales utilisées dans le projet.
    - **`Ball_Cap/`**, **`Shoses/`**, **`triko/`**, **`watch/`** : Sous-dossiers pour les différentes catégories de produits.
  - **`preprocessed/`** : Images prétraitées pour l'entraînement et l'évaluation du modèle.
- **`notebooks/`** : Notebooks Jupyter pour le prétraitement des images, l'évaluation du modèle et l'assemblage.
- **`output/`** : Fichiers de sortie générés par le projet.
  - **`ball_cap_360_view.gif`** : GIF montrant la vue à 360 degrés de la casquette Ball Cap.
  - **`stitched_image.jpg`** : Image assemblée résultant du traitement des images.
  - **`transformations.npy`** : Fichier NumPy contenant les données de transformation.
- **`scripts/`** : Scripts Python pour des tâches spécifiques.
  - **`create_360_view.py`** : Script pour générer une vue à 360 degrés d'un produit.

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-nom/360_Degree_Product_Views.git
   ```

2. Naviguez vers le répertoire du projet :
   ```
   cd 360_Degree_Product_Views
   ```

3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Utilisation -1 

<<<<<<< HEAD
1. Ouvrez le fichier `index.html` dans un navigateur web moderne.

2. Utilisez la souris pour faire pivoter les produits et voir les différents angles.

3. Ajustez les quantités et ajoutez des produits au panier.

4. Consultez le panier et procédez au paiement.
## Utilisation -2 
  Placez vos images dans le sous-dossier approprié data/images/.

  Exécutez les scripts de Prétraitement des images  et dÉvaluation de la qualité des transitions d'images et Assemblage des images (Stitching) et création d'une vue à 360 degrés en utilisant les notebooks Jupyter situés dans notebooks/.

  Utilisez le script create_360_view.py pour générer la vue à 360 degrés à partir des images traitées.

  Visualisez les résultats dans output/ et ajustez la visualisation 

## Fonctionnalités

- Visualisation de produits à 360 degrés
- Ajout de produits au panier
- Ajustement des quantités
- Calcul du total du panier
- Interface utilisateur réactive et conviviale

## Technologies utilisées

- HTML5
- CSS3 (avec Tailwind CSS)
- JavaScript (ES6+)
- Python (pour le traitement d'images et la création de vues à 360 degrés)
- OpenCV (pour le traitement d'images)
- Jupyter Notebooks (pour l'analyse et le prétraitement des données)
