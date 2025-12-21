#Dictionnaires des variables utilisées dans equipement

import pandas as pd
from IPython.display import display

tab_equipement = {
    "Variable": [
        "inst_cp", "new_name", "new_code","dep_code", "aps_name", "dens_lib", "equip_type_name", "equip_x","equip_y"
    ],
    "Description": [
        "Code postal de la commune",
        "Nom de la commune",
        "Code INSEE de la commune",
        "Code du département",
        "Sport",
        "Densité de la commune",
        "Type d'infrastructure sportive",
        "Longitude",
        "Latitude"
    ]
}

dico_vars_equipement = pd.DataFrame(tab_equipement)


#Dictionnaire des variables utilisées dans df_commune
pd.set_option("display.max_colwidth", None)

tab_communes = {
    "Variable": [
        "CODGEO", "P22_POP", "P22_MEN", "MED21", "TP6021", "P22_CHOM1564"
    ],
    "Description": [
        "Code INSEE de la commune",
        "Population en 2022",
        "Nombre de ménages en 2022",
        "Médiane du niveau de vie en 2021",
        "Taux de pauvreté en 2021",
        "Nombre de chômeurs de 15 à 64 ans en 2022"
    ]
}

dico_vars_communes = pd.DataFrame(tab_communes)


#Dictionnaire des variables utilisées dans legislatives


tab_pol = {
    "Variable": ["Code commune", "Nuance candidat", "Elu"],
    "Description": [
        "Code INSEE de la commune",
        "Parti politique du candidat",
        "Variable binaire égale à 1 si le candidat a été élu, 0 sinon"
    ]
}

dico_vars_pol = pd.DataFrame(tab_pol)

print("Dictionaire équipement:")
display(dico_vars_equipement)

print("\nDictionnaire communes:")
display(dico_vars_communes)

print("\nDictionnaire politique:") 
display(dico_vars_pol)