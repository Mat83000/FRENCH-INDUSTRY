# Industrie Française

## Présentation du projet
Le projet **Industrie Française** a pour objectif d'analyser les inégalités en France à travers des données socio-économiques fournies par l'INSEE. À partir de ces données, nous avons réalisé des analyses exploratoires, des visualisations, et construit des modèles prédictifs basés sur le Machine Learning.

### Auteurs :
- **Mathieu LARGAUD**
- **Nicolas DELANGRE**

### Formation :
- **Programme :** Data analyst - DataScientest  
- **Cohorte :** Sep 24 Bootcamp

---

## Objectifs du projet
1. **Explorer et visualiser les données** pour identifier les tendances et les disparités.
2. **Nettoyer et préparer les données** pour garantir leur qualité.
3. **Construire des modèles de Machine Learning** pour prédire des variables clés comme le salaire moyen.
4. **Présenter les résultats** via des outils comme **Streamlit** et **Power BI**.

---

## Jeux de données utilisés
Les analyses reposent sur quatre fichiers CSV de l'INSEE :
1. **Base des établissements par tranche** : Données sur la taille des entreprises.
2. **Base des salaires par catégories socio-professionnelles.**
3. **Base de la population** : Données sur la tranche d'âge, le sexe et le mode de vie.
4. **Base géographique** : Informations sur les villes françaises.

---

## Étapes principales
### 1. **Exploration des données**
- Comparaison des entreprises par taille et localisation.
- Analyse des salaires moyens par catégories socio-professionnelles, sexe, et âge.
- Étude des modes de cohabitation dans les grandes villes.

### 2. **Nettoyage et traitement des données**
- Agrégation des colonnes pour simplifier les données.
- Traitement des valeurs manquantes et suppression des doublons.
- Normalisation des données et création de nouvelles variables (ex. : taux d'emploi, écarts salariaux).

### 3. **Data-visualisation**
Exemples de graphiques réalisés :
- Répartition des entreprises par taille et localisation.
- Comparaison des salaires moyens par ville, âge, et sexe.
- Boxplots et lineplots pour analyser les disparités régionales et démographiques.

### 4. **Modélisation**
- **Modèles testés :** Régression linéaire, XGBoost, Random Forest, et K-Nearest Neighbors.
- **Modèle final retenu :** XGBoost avec un R² moyen de **0,86** après validation croisée.

---

## Résultats clés
1. **Concentration géographique :** Les entreprises, en particulier les micro-entreprises, sont principalement localisées dans les grandes villes (notamment Paris).
2. **Disparités salariales :**
   - Écarts significatifs entre hommes et femmes (jusqu'à 22% à Paris).
   - Les cadres bénéficient de rémunérations nettement supérieures aux autres catégories.
3. **Impact de l'âge et du niveau d'éducation :**
   - Les salaires augmentent avec l'expérience professionnelle.
   - La densité de diplômés Bac+5 est un facteur clé dans la prédiction des salaires moyens.

---

## Recommandations
1. **Réduction des inégalités salariales :** Mettre en œuvre des politiques pour favoriser l'égalité entre les sexes.
2. **Soutien aux PME :** Encourager la croissance des petites et moyennes entreprises en régions.
3. **Accessibilité à l'éducation :** Promouvoir la formation et les diplômes supérieurs pour réduire les disparités.

---

## Technologies utilisées
- **Python** (Pandas, NumPy, Matplotlib, Scikit-learn, XGBoost).
- **Google Colab** pour le travail collaboratif.
- **Streamlit** et **Power BI** pour la présentation interactive des résultats.

---

## Accéder au rapport complet
Le rapport détaillé est disponible au format PDF :  
[📄 Rapport Industrie Française](Rapport_French_Industry.pdf)

---

## Contact
- **Mathieu LARGAUD** : [LinkedIn](https://linkedin.com/in/mathieu-largaud)
- **Nicolas DELANGRE** : [LinkedIn](https://linkedin.com/in/nicolas-delangre)
