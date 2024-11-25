import streamlit as st
import pandas as pd
import xgboost as xgb
import os

# Fonction pour ajouter un fond couleur marron clair élégant
def add_background_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f4e7d3;
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Charger le modèle XGBoost
model_path = "xgboost_model.json"
model_xgb = xgb.Booster()
if os.path.exists(model_path):
    model_xgb.load_model(model_path)
else:
    st.error(f"Le fichier de modèle '{model_path}' est introuvable. Vérifiez le chemin et réessayez.")

# Configuration de la navigation dans la barre latérale
page = st.sidebar.radio("Navigation", ["Présentation", "Pré-processing", "Feature Engineering", "Modélisation", "Prédiction", "Conclusions"])

# Page de Présentation
if page == "Présentation":
    # Centrage du contenu
    presentation_html = """
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; text-align: center;">
        <h1 style="font-size: 3em; color: black; margin-bottom: 20px;">FRENCH INDUSTRY</h1>
    </div>
    """
    st.markdown(presentation_html, unsafe_allow_html=True)

    # Vérification de l'image
    image_path = "presentation_image.png"
    if os.path.exists(image_path):
        # Affichage de l'image avec Streamlit
        st.image(image_path, caption="Présentation de l'application", use_column_width=True)
    else:
        st.warning("L'image 'presentation_image.png' est introuvable. Vérifiez le chemin.")
    
    st.write("""
    Bienvenue dans notre projet FRENCH INDUSTRY, réalisée par **DELANGRE Nicolas et LARGAUD Mathieu**.
    Il est composé de 4 fichiers CSV provenant de l'INSEE:
    - Base des établissements par tranche,
    - Base des salaires par catégories sociaux-professionnelles,
    - Base de la population, par tranche d’age, de sexe, et de mode de vie,
    - Base géographique sur les villes françaises.

    
    - L'objectif du projet French Industry est d'analyser et de conclure sur les inégalités en France, de façon factuelle et chiffrée, par le biais de graphiques, de tests, et de prédictions à l’aide de valeurs cibles et de Machine Learning, et enfin de présenter ces analyses et graphiques à l’aide de Streamlit et PowerBI.
    
    - Nous commencerons par des visualisation à travers POWER BI sur les entreprises selon leur taille, leur localisation et les salaires moyens. 
    
    - Nous nous intéresserons particulièrement aux écarts entre les sexes, les différentes catégories socioprofessionnelles et les régions.
    
    - Une analyse plus approfondie sera ensuite menée sur un panel de grandes villes pour identifier des facteurs spécifiques influençant les inégalités observées. 
    
    - Ces premières analyses serviront de base à des investigations plus poussées.
    
    - Par la suite, nous continuerons sur streamlit pour les tâches de nettoyage, pré-processing, modélisation, prédictions et conclusions.
    """)

# Page de Pré-processing
elif page == "Pré-processing":
    st.title("Pré-processing des Données")
    st.write("""
    Avant de passer à la modélisation, un travail de prétraitement des données est nécessaire.
    
    Étapes de Pré-processing :
    - **Aperçu des Données** : Observation des fichiers au niveau de la structure et du contenu.
    - **Nettoyage des Données** : Suppression des valeurs manquantes et gestion des valeurs aberrantes.
    
    Ces étapes assurent que les données sont prêtes pour l'étape suivante d'ingénierie des caractéristiques.
    """)
    
    # Chargement des images des fichiers 
    for i in range(1, 8):  # Images "df1.png" à "df7.png"
        image_path = f"df{i}.png"
        if os.path.exists(image_path):
            if i == 1:
                st.write("**Head df_population**")
            elif i == 2:
                st.write("**Head df_salary_town**")
            elif i == 3:
                st.write("**Head df_etab_effectifs**")
            elif i == 4:
                st.write("***Head df_geo_names***")
            elif i == 5:
                st.write("***Dimensions de chaque fichier***")
            elif i == 6:
                st.write("***Valeurs manquantes***")
            elif i == 7:
                st.write("***Nombre de doublons***")
            st.image(image_path, caption=f"Visualisation {i}", use_column_width=True)    
        else:
            st.warning(f"L'image de visualisation {i} est introuvable.")

    st.write("""
    - Sur le dataframe df_etab_effectifs, nous avons décidé de regrouper les tailles d'entreprises en 4 catégories selon l'exemple de l'INSEE : micro entreprise (0 à 9 salariés), petite entreprise (10 à 49 salariés), moyenne entreprise (50 à 199 salariés) et grande entreprise (plus de 200 salariés). 
    
    - Pour harmoniser nos données, nous avons constaté que tous nos dataframes partagent une donnée commune, le CODGEO, qui doit comporter 5 chiffres. Ainsi, il est nécessaire d'ajouter un "0" au début de la cellule du CODGEO sur les df_geo_names et df_population, et de renommer la colonne "code_insee" en "CODGEO" sur le df_geo_names. 
    
    - Cette uniformité permettra de fusionner nos quatre dataframes en un seul.
    
    - Nous vérifierons la création éventuelle de doublons après chaque fusion et supprimerons des colonnes si nécessaire. 
    
    - Sur le df_geo_names, nous retirerons les colonnes latitude, longitude et éloignement car elles contiennent des valeurs manquantes et sont redondantes avec d'autres données telles que le code postal, le département, et le nom de la ville. 
    
    - Nous importerons également un jeu de données de l'INSEE relatif aux diplômes pour affiner nos analyses et établir de nouvelles corrélations.
   
    - Comme avec df_etab_effectifs, nous allons agréger, supprimer et/ou renommer des colonnes pour réduire le nombre de colonnes redondantes et éviter de fausser notre modèle de machine learning. 
   
    - Enfin, nous standardiserons nos données pour la modélisation, réaliserons une matrice de corrélation, préparerons la partie Feature Engineering, l'encodage des données, et la standardisation. 
    
    - Ces étapes nous permettront de réaliser plusieurs modélisations afin de choisir celles qui s'adaptent le mieux à notre dataframe et de déterminer une ou plusieurs valeurs cibles, notamment les salaires.
    """)

# Page de Feature Engineering
elif page == "Feature Engineering":
    st.title("Feature Engineering")
    st.write("""
    - Après avoir exploré les données de manière visuelle, nous passons à une analyse plus quantitative.
    
    - En calculant des matrices de corrélation, nous visons à mettre en évidence les liens linéaires entre les différentes variables. 
    
    - Cette étape nous permettra de détecter les redondances, d'éliminer les variables peu pertinentes et de construire des combinaisons de variables plus informatives. 
    
    - En simplifiant ainsi notre jeu de données, nous favoriserons la construction de modèles plus robustes et plus interprétables.
    """)

    # Ajout d'un fichier supplémentaire pour le niveau scolaire
    image_path = "diplome.png"  # Une seule image ici
    if os.path.exists(image_path):
        st.image(image_path, caption="Niveau scolaire en France", use_column_width=True)
    else:
        st.warning("L'image 'diplome.png' est introuvable.")
        st.write("""
         Avant de passer à la création des matrices de corrélations, nous avons rajouter un dernier fichier provenant de l'INSEE, qui introduit le niveau scolaire en France, appelé df_diplomes.
         Après modification de certaines colonnes et suppression d'autres, nous avons fusionné les 5 fichiers pour créer notre dataframe.
         """)

    # Chargement des images des matrices de corrélation
    image_path = "matrice1.png"

    if os.path.exists(image_path):
        st.image(image_path, caption="Matrice 1", use_column_width=True)
    else:
        st.warning("L'image 'matrice1.png' est introuvable.")

    st.write("""
            - L'objectif de cette étape était de préparer les données pour la construction d'un modèle prédictif performant.
            - Notre but était de découvrir notre variable cible, le salaire moyen net par heure. 
            - En éliminant les colinéarités et en créant de nouvelles variables informatives, nous avons posé les bases d'une analyse robuste. 
            - La prochaine étape consistera à appliquer différents algorithmes de machine learning pour prédire le salaire net moyen par heure.
            """)
    
# Page de Modélisation
elif page == "Modélisation":
    st.title("Modélisation et Performances")
    st.write("""
    Machine Learning et Entraînement des Modèles:
    - Comparaison de plusieurs modèles (Random Forest, XGBoost, etc.) et sélection du meilleur basé sur le R².
    - Optimisation des modèles avec validation croisée et ajustement des hyperparamètres.
    """)

    image_path = "score1.png"  # Affichage d'une seule image
    if os.path.exists(image_path):
        st.image(image_path, caption="Score 1", use_column_width=True)
   
    
    st.write("""
             Le modèle Random Forest semble être le choix le plus robuste pour cet entraînement de l'ensemble de données, avec un excellent R² et des erreurs plus faibles par rapport à XG Boost et KNN.
             La régression linéaire a un score parfait, mais cela pourrait nécessiter une validation croisée plus approfondie pour vérifier sa généralisation.
             """)
             
    # Affichage des performances des modèles
    for i in range(1, 6):  # Images "model_performance1.png" à "model_performance5.png"
        image_path = f"model_performance{i}.png"
        if os.path.exists(image_path):
            st.image(image_path, caption=f"Performance du Modèle {i}", use_column_width=True)
        else:
            st.warning(f"L'image de visualisation {i} est introuvable.")
            
    st.write("""
     Les résultats de nos analyses montrent que le modèle XG Boost surpasse les autres modèles en termes de précision prédictive. 
     Bien que le modèle Random Forest offre également de bonnes performances, XG Boost semble mieux capturer la complexité des relations entre les variables de notre jeu de données.
     """)

# Page de Prédiction
elif page == "Prédiction":
    st.title("Prédiction du Salaire Net Moyen par Heure")
    st.write("Entrez les informations ci-dessous pour obtenir une estimation.")
    
    image_path = "presentation_image2.png"  # Image de présentation
    if os.path.exists(image_path):
        st.image(image_path, caption="Présentation", use_column_width=True)
    else:
        st.warning("L'image 'presentation_image2.png' est introuvable.")

   
    # Dictionnaire des régions avec leurs codes
    regions = {
        1: "Guadeloupe", 2: "Martinique", 3: "Guyane", 4: "La Réunion", 5: "Mayotte",
        6: "Saint-Pierre-et-Miquelon", 11: "Ile-de-France", 21: "Champagne", 22: "Picardie",
        23: "Haute-Normandie", 24: "Centre", 25: "Basse-Normandie", 26: "Bourgogne",
        31: "Nord", 41: "Lorraine", 42: "Alsace", 43: "Franche-Comté", 52: "Pays-de-la-Loire",
        53: "Bretagne", 54: "Poitou-Charente", 72: "Aquitaine", 73: "Midi-Pyrénées", 
        74: "Limousin", 82: "Rhône-Alpes", 83: "Auvergne", 91: "Languedoc-Roussillon",
        93: "Sud", 94: "Corse"
    }
    
    # Sélection de la région
    selected_region = st.selectbox("Sélectionnez la région", options=list(regions.keys()), format_func=lambda x: f"{x} - {regions[x]}")

    # Création des entrées pour les features
    salaire_hommes = st.number_input("Salaire moyen des hommes (€ / h)", min_value=0.0, max_value=100.0, value=20.0)
    salaire_femmes = st.number_input("Salaire moyen des femmes (€ / h)", min_value=0.0, max_value=100.0, value=18.0)
    salaire_plus_50 = st.number_input("Salaire moyen des plus de 50 ans (€ / h)", min_value=0.0, max_value=100.0, value=19.0)
    ecart_salarial_HF = st.number_input("Écart salarial Hommes/Femmes (€ / h)", min_value=-50.0, max_value=50.0, value=2.0)
    salaire_ouvriers = st.number_input("Salaire moyen des ouvriers (€ / h)", min_value=0.0, max_value=100.0, value=15.0)
    salaire_employes = st.number_input("Salaire moyen des employés (€ / h)", min_value=0.0, max_value=100.0, value=16.0)
    densite_diplomes_BAC5 = st.number_input("Densité de diplômés BAC+5 (%)", min_value=0.0, max_value=100.0, value=30.0)
    taux_emploi = st.number_input("Taux d'emploi (%)", min_value=0.0, max_value=100.0, value=70.0)
    salaire_cadres = st.number_input("Salaire moyen des cadres (€ / h)", min_value=0.0, max_value=100.0, value=30.0)

    # Moyennes et écarts-types pour la standardisation des features
    feature_means = {
        'salaire_hommes': 20.0,
        'salaire_femmes': 18.0,
        'salaire_plus_50': 19.0,
        'ecart_salarial_HF': 2.0,
        'salaire_ouvriers': 15.0,
        'salaire_employes': 16.0,
        'densite_diplomes_BAC5': 30.0,
        'taux_emploi': 70.0,
        'salaire_cadres': 30.0
    }

    feature_stds = {
        'salaire_hommes': 5.0,
        'salaire_femmes': 4.0,
        'salaire_plus_50': 5.0,
        'ecart_salarial_HF': 1.0,
        'salaire_ouvriers': 3.0,
        'salaire_employes': 3.5,
        'densite_diplomes_BAC5': 10.0,
        'taux_emploi': 5.0,
        'salaire_cadres': 10.0
    }

    # Fonction de standardisation
    def standardize_input(value, feature_name):
        return (value - feature_means[feature_name]) / feature_stds[feature_name]

    # Préparation de l'encodage de la région en One-Hot Encoding
    region_encoded = {f"region_{key}": 1 if key == selected_region else 0 for key in regions.keys()}

    if st.button("Prédire le salaire"):
        # Standardisation des autres inputs
        standardized_inputs = {
            'f0': standardize_input(salaire_hommes, 'salaire_hommes'),
            'f1': standardize_input(salaire_femmes, 'salaire_femmes'),
            'f2': standardize_input(salaire_plus_50, 'salaire_plus_50'),
            'f3': standardize_input(ecart_salarial_HF, 'ecart_salarial_HF'),
            'f4': standardize_input(salaire_ouvriers, 'salaire_ouvriers'),
            'f5': standardize_input(salaire_employes, 'salaire_employes'),
            'f6': standardize_input(densite_diplomes_BAC5, 'densite_diplomes_BAC5'),
            'f7': standardize_input(taux_emploi, 'taux_emploi'),
            'f8': standardize_input(salaire_cadres, 'salaire_cadres')
        }

        # Fusion des caractéristiques standardisées avec l'encodage one-hot des régions
        full_input = {**standardized_inputs, **region_encoded}

        # Création du DMatrix avec les valeurs standardisées et encodage des régions
        dtest = xgb.DMatrix(pd.DataFrame([full_input]))
        
        # Prédiction
        prediction = model_xgb.predict(dtest)[0]
        
        # Affichage du résultat
        st.success(f"Le salaire net moyen prédit est de {prediction:.2f} €/heure")
        
# Page de Conclusion
elif page == "Conclusions":
    st.title("Conclusions et Perspectives")
    default_image_path = "presentation_image3.png"
    
    if os.path.exists(default_image_path):
        st.image(default_image_path, caption="Image par défaut", use_column_width=True)
    else:
        st.warning("L'image par défaut est introuvable.")
        
    st.write("""
-   Dans notre analyse, l’écart salarial entre hommes et femmes se révèle être le facteur le plus influent dans la prédiction des salaires moyens, confirmant qu’il s’agit d’un déterminant majeur des inégalités salariales.

-	La densité de diplômés Bac+5 apparaît également comme un autre facteur critique, ce qui souligne l’importance du niveau d’éducation dans la détermination des salaires

-	Les autres caractéristiques, telles que le taux d'emploi, le nombre total d'entreprises ou les codes géographiques, ont un impact moins important mais contribuent néanmoins à la précision du modèle.

-	Notre modèle XGBoost accorde une importance prépondérante à l'écart salarial et au niveau d'éducation pour effectuer ses prédictions, qui constituent des leviers importants pour agir sur les inégalités

-	D’un point de vue métier, cela signifie que les politiques visant à réduire les écarts salariaux devraient se concentrer sur l’égalité des genres dans les salaires et mettre l’accent sur des politiques d’éducation et de formation.

-	En conséquence, il serait pertinent de recommander aux entreprises et aux collectivités de développer des initiatives pour améliorer l'accès à la formation supérieure et d'encourager des pratiques de rémunération équitable.

-	Nous pourrions recommander des programmes de formation spécifiques pour les femmes dans les secteurs à forte croissance, qui pourraient à la fois réduire l'écart salarial et favoriser une montée en compétences dans des domaines bien rémunérés.""")
    
add_background_color()



