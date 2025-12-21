import pandas as pd

def nettoyer_donnees(equipement, df_communes, legislatives2):
    # 1. Traitement Equipement
    new_cols = ["inst_cp", "new_name", "new_code", "dep_code", "aps_name", 
                "dens_lib", "equip_type_name", "equip_x", "equip_y"]
    equipement = equipement[new_cols].copy()

    # 2. Traitement Communes
    cols_com = ["CODGEO", "P22_POP", "P22_MEN", "MED21", "TP6021", "P22_CHOM1564"]
    df_communes = df_communes[cols_com].copy()

    # 3. Traitement Législatives
    cols_leg = ["Code commune", "Libellé commune"]
    cols_leg += [f"Nuance candidat {i}" for i in range(1, 5)]
    elu_cols = [f"Elu {i}" for i in range(1, 5)]
    cols_leg += elu_cols

    legislatives2 = legislatives2[cols_leg].copy()

    # Transformation de la variable élu en binaire
    for col in elu_cols:
        legislatives2[col] = legislatives2[col].notna().astype(int)
    
    print("Nettoyage terminé : colonnes filtrées et variables binaires créées.")
    
    return equipement, df_communes, legislatives2