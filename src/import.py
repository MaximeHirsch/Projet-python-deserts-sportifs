import io
import requests
import zipfile
import pandas as pd

# Importation du jeu de données principal (localisation des équipements sportifs en France)

url = "https://data.sports.gouv.fr/api/explore/v2.1/catalog/datasets/equipements-sportifs/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
url1 = "https://www.data.gouv.fr/api/1/datasets/r/ea4f5879-af40-4e3e-949d-812d6eeb5e02"
equipement = pd.read_csv(url1, sep=";", low_memory=False)

#Importation d'un jeu de données csv sur des informations économiques et démographiques au niveau des communes

urlpop = "https://www.insee.fr/fr/statistiques/fichier/2521169/base_cc_comparateur_csv.zip"
response = requests.get(urlpop)

with zipfile.ZipFile(io.BytesIO(response.content)) as z:                 #io.BytesIO évite de télécharger le fichier
    with z.open("base_cc_comparateur.csv") as csvfile:                   #sur le disque dur
        df_communes = pd.read_csv(csvfile, sep=";", low_memory=False)


#Importation d'un jeu de données politiques au niveau des communes: résultats des législatives 2024 (2nd tour)

url2="https://www.data.gouv.fr/api/1/datasets/r/5a8088fd-8168-402a-9f40-c48daab88cd1"
legislatives2=pd.read_csv(url2, sep=";", low_memory=False)