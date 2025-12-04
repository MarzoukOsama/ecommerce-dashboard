&nbsp;📊 E-commerce Analytics Dashboard



Dashboard interactif de visualisation et analyse de données e-commerce construit avec Streamlit et Plotly.



&nbsp;🎯 Description



Application web interactive permettant d'analyser les performances d'une plateforme e-commerce en temps réel. Le dashboard offre des visualisations dynamiques et des filtres pour explorer les données sous différents angles.

⚠️ Note sur les données

Ce repository contient un **échantillon de 100 transactions** pour permettre le déploiement sur Streamlit Cloud. 

Pour utiliser le dataset complet (5000 transactions) :
1. Clonez le [projet ETL](https://github.com/MarzoukOsama/etl-ecommerce-pipeline)
2. Exécutez le pipeline pour générer les données complètes
3. Copiez les fichiers vers le dossier `data/`


&nbsp;✨ Fonctionnalités



&nbsp;📈 Vue d'ensemble KPIs

\- Chiffre d'affaires total

\- Nombre de commandes

\- Panier moyen

\- Nombre de clients uniques



&nbsp;📅 Analyses temporelles

\- Évolution du CA mensuel

\- Distribution des ventes par jour de la semaine

\- Tendances et saisonnalité



&nbsp;🏆 Performance produits

\- Top 10 produits par chiffre d'affaires

\- Répartition par catégorie (graphique en donut)

\- Analyse comparative



&nbsp;🌍 Analyse géographique

\- Ventes par pays

\- Répartition géographique du CA

\- Performance par région



&nbsp;💎 Segmentation clients

\- Classification VIP / Premium / Standard

\- Comportement d'achat par segment

\- Analyse de la valeur client



&nbsp;🔍 Filtres interactifs

\- Filtre par pays

\- Filtre par catégorie produit

\- Sélection de période personnalisée

\- Mise à jour temps réel des graphiques



&nbsp;🛠️ Technologies utilisées



\- \*\*Streamlit\*\* : Framework d'application web pour la data science

\- \*\*Plotly\*\* : Graphiques interactifs et visualisations avancées

\- \*\*Pandas\*\* : Manipulation et analyse de données

\- \*\*Python 3.x\*\*



&nbsp;📁 Structure du projet



ecommerce-dashboard/

│

├── data/

│ ├── README.md  Instructions données

│ └── \*.csv  Fichiers CSV (non versionnés)

│

├── app.py  Application principale

├── requirements.txt  Dépendances Python

├── .gitignore

└── README.md







&nbsp;🚀 Installation et Utilisation



&nbsp;Prérequis



\- Python 3.8+

\- Données générées depuis le \[projet ETL E-commerce](https://github.com/MarzoukOsama/etl-ecommerce-pipeline)



&nbsp;Installation locale



1\. \*\*Cloner le repository\*\*

git clone https://github.com/MarzoukOsama/ecommerce-dashboard.git

cd ecommerce-dashboard







2\. \*\*Créer un environnement virtuel\*\*

python -m venv venv

venv\\Scripts\\activate  Windows

source venv/bin/activate  Linux/Mac







3\. \*\*Installer les dépendances\*\*

pip install -r requirements.txt







4\. \*\*Copier les données\*\*



Copiez les fichiers CSV depuis le projet ETL :

Depuis etl-ecommerce-pipeline/data/processed/

cp ../etl-ecommerce-pipeline/data/processed/\*.csv data/







Ou générez-les en exécutant le pipeline ETL.



5\. \*\*Lancer le dashboard\*\*

streamlit run app.py







Le dashboard s'ouvrira automatiquement dans votre navigateur à `http://localhost:8501`



&nbsp;📊 Captures d'écran



&nbsp;Vue d'ensemble

Dashboard présentant les KPIs principaux et graphiques d'évolution



&nbsp;Analyse produits

Visualisation des top produits et répartition par catégorie



&nbsp;Filtres interactifs

Sélection dynamique par pays, catégorie et période



&nbsp;🌐 Déploiement



&nbsp;Streamlit Cloud (Gratuit)



Ce dashboard peut être déployé gratuitement sur Streamlit Cloud :



1\. Fork ce repository

2\. Connectez-vous sur \[share.streamlit.io](https://share.streamlit.io)

3\. Déployez depuis votre repository GitHub

4\. Ajoutez les fichiers CSV via les secrets Streamlit



\*\*Note\*\* : Pour le déploiement public, utilisez des données anonymisées ou synthétiques.



&nbsp;📈 Métriques et Insights



Le dashboard permet de répondre à des questions business clés :



\- Quel est le produit le plus rentable ?

\- Quelle catégorie génère le plus de CA ?

\- Quels sont les jours de pic de ventes ?

\- Quelle est la répartition géographique des clients ?

\- Combien de clients VIP génèrent du CA ?



&nbsp;🔄 Intégration avec les projets existants



Ce dashboard fait partie d'un écosystème de projets data :



1\. \*\*\[ETL Pipeline](https://github.com/MarzoukOsama/etl-ecommerce-pipeline)\*\* : Génère et transforme les données

2\. \*\*\[Data Quality Monitoring](https://github.com/MarzoukOsama/data-quality-monitoring)\*\* : Valide la qualité

3\. \*\*Dashboard Analytics\*\* (ce projet) : Visualise les insights



&nbsp;🎯 Cas d'usage



\- \*\*Analyse business\*\* : Monitoring des KPIs en temps réel

\- \*\*Reporting\*\* : Génération de rapports visuels pour stakeholders

\- \*\*Data exploration\*\* : Exploration interactive des données

\- \*\*Démo portfolio\*\* : Démonstration de compétences en visualisation



&nbsp;🚀 Évolutions futures



\- \[ ] Ajout de prédictions ML (forecasting)

\- \[ ] Export PDF des rapports

\- \[ ] Alertes automatiques sur seuils KPIs

\- \[ ] Comparaison période N vs N-1

\- \[ ] Analyse de cohortes clients

\- \[ ] Intégration API temps réel



&nbsp;👨‍💻 Auteur



\*\*Oussama Marzouk\*\*  

Data Analyst | Python Developer  

\[GitHub](https://github.com/MarzoukOsama) | \[LinkedIn]()



&nbsp;📝 Licence



Ce projet est développé à des fins de portfolio et d'apprentissage.



---



⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !

