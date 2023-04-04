import tkinter as tk
import random

# Initialiser la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Jeu du pendu")
label = tk.Label(fenetre, text="Bienvenue dans le jeu du pendu", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget

# Définir la liste de mots pour le jeu
liste_mots = ["correction", "opportuniste", "ascenseur", "evrest", "situation", "saturation", "programmeur","aviateur","musicien"]
 

# Choisir un mot aléatoire de la liste
mot_a_deviner = random.choice(liste_mots)

# Initialiser les variables du jeu
lettres_trouvees = []
lettres_manquees = []
nb_essais = 9
 
import random

liste_de_mot = ['correction', 'opportuniste', 'ascenseur', 'evrest', 'situation', 'saturation', 'programmeur','aviateur','musicien']
solution = random.choice(liste_de_mot)

tentative=8


affichage=""
a = (len(solution))
i = 1
while a >= i:
    affichage += "_"
    i += 1
print(affichage)

#fonctoin qui dit si la lettre est bonne si erreur essai-1 si bon dit que la lettre est bonne faut juste essaiyer de la placer sur l'interface
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
fenetre.mainloop()#lancement de la fenetre 

    # Afficher les lettres correctes et incorrectes
    lettres_correctes_lbl.configure(text="Lettres correctes: " + ", ".join(lettres_correctes))
    lettres_incorrectes_lbl.configure(text="Lettres incorrectes: " + ", ".join(lettres_incorrectes))
    # Afficher les lettres du mot cachées ou dévoilées
    mot_lbl.configure(text="Mot: " + " ".join(l if l in lettres_correctes else "_" for l in mot))

# Fonction pour afficher un message de fin de jeu
def afficher_message(message):
    message_lbl.configure(text=message)
    message_lbl.pack()

# Créer la fenêtre principale
fenetre = Tk()
fenetre.title("Jeu du pendu")
    return mot_cdef maj_affichage():
    # Effacer le canevas et redessiner le pendu
    canevas.delete("all")
    if tentative > 0:
        canevas.create_line(20, 180, 100, 180)
    if tentative > 1:
        canevas.create_line(60, 180, 60, 20)
    if tentative > 2:
        canevas.create_line(60, 20, 150, 20)
    if tentative > 3:
        canevas.create_line(150, 20, 150, 40)
    if tentative > 4:
        canevas.create_oval(135, 40, 165, 70)
    if tentative > 5:
        canevas.create_line(150, 70, 150, 110)
     if tentative > 6:
       face = canvas.create_oval(50, 50, 250, 250, width=2, outline='black')
       left_eye = canvas.create_oval(90, 100, 130, 140, fill='white', outline='black')
       right_eye = canvas.create_oval(170, 100, 210, 140, fill='white', outline='black')
       mouth = canvas.create_arc(90, 150, 210, 230, start=30, extent=120, style='arc', width=2)

       # Modifier le visage pour le rendre triste
        canvas.itemconfigure(left_eye, extent=270, style='arc')
        canvas.itemconfigure(right_eye, extent=270, style='arc')
        canvas.move(mouth, 0, 20)ache
# source 
# https://github.com/codingglitch/PenduTkinter/blob/main/pendu.py
#https://www.mathweb.fr/euclide/2020/09/07/le-jeu-du-pendu-en-python/
# https://lesbricodeurs.fr/articles/jeu-du-pendu-python/
# chat gpt (annalyse fonctionel)
