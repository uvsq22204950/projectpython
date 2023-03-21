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

liste_de_mot = ['boule']
solution = random.choice(liste_de_mot)

tentative=8


affichage=""
a = (len(solution))
i = 1
while a >= i:
    affichage += "_"
    i += 1
print(affichage)

lettre = []
mauvaises_lettre = []
bonnes_lettres = []
while tentative >= 0 and "_" in affichage:
        proposition = input("entrer une lettre: ")
        x = proposition.isalpha()
        if len(proposition) > 1 and x == False:
            print("erreur, recommencer")
        
        elif len(proposition) <= 1 and x == True:
            
        
            if proposition not in solution:
                mauvaises_lettre += [proposition]
                print("mauvaises lettres: ", mauvaises_lettre)
    
            elif proposition in solution:
                bonnes_lettres +=[proposition]
                print("bonnes lettres: ", bonnes_lettres)
        
            if proposition not in solution:
                tentative -= 1
                print ("tentatives restantes", tentative)
        
            elif proposition in solution:
                affichage += proposition 
    

print(lettre) 
print("le mot est", affichage)
