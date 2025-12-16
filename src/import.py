import io
import requests
import zipfile
import pandas as pd

#URL

url1 = "https://www.data.gouv.fr/api/1/datasets/r/ea4f5879-af40-4e3e-949d-812d6eeb5e02"
url2 = "https://www.insee.fr/fr/statistiques/fichier/2521169/base_cc_comparateur_csv.zip"
url3="https://www.data.gouv.fr/api/1/datasets/r/5a8088fd-8168-402a-9f40-c48daab88cd1"


# Importation du jeu de données principal (localisation des équipements sportifs en France)

equipement = pd.read_csv(url1, sep=";", low_memory=False)

#Importation d'un jeu de données csv sur des informations économiques et démographiques au niveau des communes

response = requests.get(url2)

with zipfile.ZipFile(io.BytesIO(response.content)) as z:                 #io.BytesIO évite de télécharger le fichier
    with z.open("base_cc_comparateur.csv") as csvfile:                   #sur le disque dur
        df_communes = pd.read_csv(csvfile, sep=";", low_memory=False)


#Importation d'un jeu de données politiques au niveau des communes: résultats des législatives 2024 (2nd tour)

legislatives2=pd.read_csv(url3, sep=";", low_memory=False)