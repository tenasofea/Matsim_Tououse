# -----------------------------------------------------------------------------------------------------------
# Statitique avant (avec fichier agent_positions que ne sont pas vraies)

# import matsim
# import pandas as pd
# import geopandas as gpd
# from collections import defaultdict
# import matplotlib.pyplot as plt
# import numpy as np
# from datetime import datetime

# agents_df = pd.read_csv("agent_positions.csv")
# persons_df = pd.read_csv("C:/Users/User/IdeaProjects/matsim-example-project-modified/simulation_output_toulouse/output_persons.csv.gz", sep=';')

# # net = matsim.read_network('C:/Users/User/IdeaProjects/matsim-example-project-modified/simulation_output_toulouse/output_network.xml.gz')

# # population active et non active
# population_active = agents_df['AgentId'].nunique()
# population_nonactive = persons_df['person'].nunique()

# # nombre de points par trajet
# # nb de points (lignes dans agent_positions.csv) pour chaque agent, moyen, min et max 
# points_par_trajet = agents_df.groupby('AgentId')['X'].count()
# moyenne_points_par_trajet = points_par_trajet.mean()
# min_points_par_trajet = points_par_trajet.min()
# max_points_par_trajet = points_par_trajet.max()

# # duree moyenne des trajets
# agents_df['Temps'] = agents_df['Temps'].astype(float) 
# duree_trajet_par_agent = agents_df.groupby('AgentId')['Temps'].apply(lambda x: x.max() - x.min())
# duree_moyenne_trajet = duree_trajet_par_agent.mean()

# # nb de trajets ayant le motif
# d_t_trajets = agents_df[agents_df['Motif'] == 'work']['AgentId'].nunique()

# d_s_trajets = agents_df[agents_df['Motif'] == 'shop']['AgentId'].nunique()

# d_e_trajets = agents_df[agents_df['Motif'] == 'education']['AgentId'].nunique()

# d_l_trajets = agents_df[agents_df['Motif'] == 'leisure']['AgentId'].nunique()

# # nb total de trajets
# total_trajets = agents_df['AgentId'].nunique()

# # distribution motifs
# # compter les occurrences de chaque motif dans les trajets
# distribution_motifs = agents_df['Motif'].value_counts()

# # evolution du trafic au fil du temps
# # grouper les agents par intervalle de temps 60 min pour voir combien d'agents sont actifs
# agents_df['minute'] = (agents_df['Temps'] // 60).astype(int)
# trafic_par_minute = agents_df.groupby('minute')['AgentId'].nunique() 

# # heure debut et heure de fin de la simulation
# heure_debut_simulation = agents_df['Temps'].min() / 3600  
# heure_fin_simulation = agents_df['Temps'].max() / 3600  


# # heure_debut_trajet = agents_df.groupby('AgentId')['Temps'].min()

# # heure_fin_trajet = agents_df.groupby('AgentId')['Temps'].min()

# print(f"Population active : {population_active}")
# print(f"Population non active : {population_nonactive}")
# print(f"Nombre moyen de points par trajet : {moyenne_points_par_trajet}")
# print(f"Nombre minimum de points par trajet : {min_points_par_trajet}")
# print(f"Nombre maximum de points par trajet : {max_points_par_trajet}")
# print(f"Duree moyenne des trajets : {duree_moyenne_trajet / 3600:.2f} heures") 
# print(f"Nombre de trajets domicile-travail : {d_t_trajets}")
# print(f"Nombre de trajets domicile-marche : {d_s_trajets}")
# print(f"Nombre de trajets domicile-scolaire : {d_e_trajets}")
# print(f"Nombre de trajets domicile-leisure : {d_l_trajets}")
# print(f"Nombre total de trajets : {total_trajets}")
# print(f"Heure debut la simulation : {heure_debut_simulation}")
# print(f"Heure fin la simulation : {heure_fin_simulation}")
# print("Distribution des motifs :")
# print(distribution_motifs)


# # extraire les resultats dans un fichier CSV 
# resultats = pd.DataFrame({
#     'population_active': [population_active],
#     'population_nonactive': [population_nonactive],
#     'moyenne_points_par_trajet': [moyenne_points_par_trajet],
#     'min_points_par_trajet': [min_points_par_trajet],
#     'max_points_par_trajet': [max_points_par_trajet],
#     'duree_moyenne_trajet_heures': [duree_moyenne_trajet / 3600],
#     'domicile_travail_trajets': [d_t_trajets],
#     'domicile_shop_trajets': [d_s_trajets],
#     'domicile_education_trajets': [d_e_trajets],
#     'domicile_leisure_trajets': [d_l_trajets],
#     'total_trajets': [total_trajets],
#     'heure_debut_simulation_heures': [heure_debut_simulation],
#     'heure_fin_simulation_heures': [heure_fin_simulation]
# })
# resultats.to_csv("resultats_statistiques.csv", index=False)

# # Exporter l'évolution du trafic par minute
# trafic_par_minute.to_csv(f"evolution_trafic.csv", index=True)

# # geo = net.as_geo()
# # geo.plot()
# # plt.show()


# -----------------------------------------------------------------------------------------------------------
# Statitique reele (avec fihcier agent_positions_mtif.csv)

import pandas as pd
import numpy as np
import os
from datetime import datetime

# Charger les données
agents_df = pd.read_csv("agent_positions_motif.csv")
persons_df = pd.read_csv("C:/Users/User/IdeaProjects/matsim-example-project-modified/simulation_output_toulouse/output_persons.csv.gz", sep=';')

# Population active et non active
population_active = agents_df['AgentId'].nunique()
population_nonactive = persons_df['person'].nunique()

# Nombre de points par trajet (agent)
points_par_trajet = agents_df.groupby('AgentId')['x'].count()

# Duree moyenne des trajets
duree_trajet_par_agent = agents_df.groupby('AgentId')['Temps_minute'].apply(lambda x: x.max() - x.min())
duree_moyenne_trajet = duree_trajet_par_agent.mean()

# Nombre de trajets domicile-travail (Motif_Orig = "home", Motif_Dest = "work")
domicile_travail_trajets = agents_df[(agents_df['Motif_Orig'] == 'home') & (agents_df['Motif_Dest'] == 'work')]['AgentId'].nunique()

# Nombre total de trajets (chaque AgentId est un trajet)
total_trajets = agents_df['AgentId'].nunique()

# Nombre moyen de points par trajet
moyenne_points_par_trajet = points_par_trajet.mean()

# Nombre minimum et maximum de points par trajet
# smallest number of points recorded for a single trip (agent)
min_points_par_trajet = points_par_trajet.min()
# largest number of points recorded for a single trip (agent)
max_points_par_trajet = points_par_trajet.max()

# Distribution points des motifs (combinaisons de Motif_Orig et Motif_Dest)
distribution_motifs_points = agents_df.groupby(['Motif_Orig', 'Motif_Dest']).size()

# Nombre de trajets par motif_orig et motif_dest (nouvelle statistique pour trips)
# Cette statistique compte le nombre de trajets distincts pour chaque combinaison de Motif_Orig et Motif_Dest
nombre_trajets_par_motif = agents_df.groupby(['Motif_Orig', 'Motif_Dest'])['AgentId'].nunique().reset_index()
nombre_trajets_par_motif.columns = ['Motif_Orig', 'Motif_Dest', 'Nombre_Trajets']

# Evolution du trafic au fil du temps (grouper par minute)
trafic_par_minute = agents_df.groupby('Temps_minute')['AgentId'].nunique()

# Heure de debut et heure de fin de la simulation
heure_debut_simulation = agents_df['Temps_minute'].min()  
heure_fin_simulation = agents_df['Temps_minute'].max()  

filename = "resultats_statistiques.csv"

print("\n--- Statistiques sur Toulouse---")
print(f"Population active : {population_active}")
print(f"Population non active : {population_nonactive}")
print(f"Nombre total de trajets : {total_trajets}")
print(f"Nombre de trajets domicile-travail : {domicile_travail_trajets}")
print(f"Duree moyenne des trajets (minutes) : {duree_moyenne_trajet:.2f}")
print(f"Nombre moyen de points par trajet : {moyenne_points_par_trajet:.2f}")
print(f"Nombre minimum de points par trajet : {min_points_par_trajet}")
print(f"Nombre maximum de points par trajet : {max_points_par_trajet}")
print(f"Heure de debut de la simulation (minutes) : {heure_debut_simulation}") 
print(f"Heure de fin de la simulation (minutes) : {heure_fin_simulation}") 
print("\n--- Nombre Position par Agent---")
print(points_par_trajet)
print("\n--- Duree trajet (minute) par Agent---")
print(duree_trajet_par_agent)
print("\n--- Distribution des Point Motifs (Origine -> Destination) ---")
print(distribution_motifs_points)
print("\n--- Distribution des Trajet Motifs (Origine -> Destination) ---")
print(nombre_trajets_par_motif)
print("\n--- Evolution du trafic (agents actifs par minute) ---")
print(trafic_par_minute)    

# Exporter les resultats dans un fichier CSV
resultats = pd.DataFrame({
    'population_active': [population_active],
    'population_non_active': [population_nonactive],
    'moyenne_points_par_trajet': [moyenne_points_par_trajet],
    'duree_moyenne_trajet_minutes': [duree_moyenne_trajet],
    'domicile_travail_trajets': [domicile_travail_trajets],
    'total_trajets': [total_trajets],
    'min_points_par_trajet': [min_points_par_trajet],
    'max_points_par_trajet': [max_points_par_trajet],
    'heure_debut_simulation_minutes': [heure_debut_simulation],
    'heure_fin_simulation_minutes': [heure_fin_simulation]
})
resultats.to_csv(filename, index=False)

# Exporter la nombre points(position - lignes dans output_detailles) par agent
points_par_trajet.to_csv(f"nombre_points_agent.csv", index=True)

# Exporter la duree trajet par agents
duree_trajet_par_agent.to_csv(f"duree_trajet_agent.csv", index=True)

# Exporter la distribution points des motifs
distribution_motifs_points.to_csv(f"distribution_motifs_points.csv", index=True)

# Exporter la distribution trajet des motifs
nombre_trajets_par_motif.to_csv(f"distribution_motifs_trajet.csv", index=True)

# Exporter l'evolution du trafic par minute
trafic_par_minute.to_csv(f"evolution_trafic.csv", index=True)
