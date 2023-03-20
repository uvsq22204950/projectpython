import tkinter as tk
import random

# Initialiser la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Jeu du pendu")

# Définir la liste de mots pour le jeu
liste_mots = ["correction", "opportuniste", "ascenseur", "evrest", "situation", "saturation", "programmeur","aviateur","musicien"]

# Choisir un mot aléatoire de la liste
mot_a_deviner = random.choice(liste_mots)

# Initialiser les variables du jeu
lettres_trouvees = []
lettres_manquees = []
nb_essais = 9

# Fonction pour afficher le mot caché avec les lettres déjà trouvées

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

import random

liste_de_mot = ['boule', 'noisette', 'vache', 'secret', 'sauterelle', 'feu', "hippocampe"]
solution = random.choice(liste_de_mot)


affichage=""
a=(len(solution))
i=0
while a>=i:
    affichage+="_"
    i+=1
print(affichage)

tentative=8

while tentative >= 0:
    proposition = input("entrer une lettre: ")
    x = proposition.isalpha()
    if len(proposition) <= 1 and x == True:
          break
    else:
          print("erreur, recommencer")

lettre=""
while tentative >= 0:
     if proposition not in solution:
          tentative -= 1
          print(tentative)
          if proposition in solution:
              break
