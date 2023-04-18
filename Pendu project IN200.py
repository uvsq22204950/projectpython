import tkinter as tk
from tkinter import *
import tkinter.messagebox
import random
import copy

frequence = ["e", "s", "a", "r", "t", "i", "n", "u", "l", "o", "d", "c", "j", "b", "m", "p", "v", "q", "f", "g", "h", "x", "y", "z", "w", "k" ]
liste_de_mot = ["doublure","plongeur","prisonnier","ivoire","juteux","gencives","incliner","toast","sommeil","fondre","cadeau","mot","blouse","nourriture","saison","contagieux","cognitif","condamne","ennui","goutte","albinos","claustrophobie","lame","python","descente","construction","masseuse","guerison","suicide","lyncher","valise","meurtrier","pyjamas","extension","harpon","phylogenetique","fourmi","siamois","ion","anion","cation","fourgonette","joie","bonheur","mongofier","liquide","solide","gazeux","aliteration","prosodit","renaisance","recommencer","phenix","metaphore","surmoi","astronaute","lune","soleile","blanc","creme","pluie","ciel","meteo","meteorite","gamette"]# liste de mots

solution = random.choice(liste_de_mot) #celection du mot caché dans la liste de mots préalablement définie
mot_tab=[]
for i in solution:
    mot_tab.append(i)
#definnition variables
mauvaises_lettres = []
bonnes_lettres = []
tentative = 9
affichage=[]
for i in range(len(mot_tab)):#met le nombre de lettre du mot en étoile dans la fenetre
    affichage.append("*")

def indication(): #donne une lettre qui a un haut to de fréquance dans la langue française
    entry_letter.delete(0,tk.END) # supprime l'intérieur de la case à écrire (de 0 jusqu'à la fin)
    entry_letter.insert(0,frequence[0])

def aide(): #fonction aide qui nous donne les règles
    aides =tk.Tk()
    label = tk.Label(aides, text="Le but du jeu est simple : deviner toutes les lettres qui doivent composer un mot, éventuellement avec un nombre limité de tentatives et des thèmes fixés à l'avance.\n" + "A chaque fois que le joueur devine une lettre, celle-ci est affichée. Dans le cas contraire, le dessin d'un pendu se met à apparaître", font=("Helvetica", 9))
    label.pack()  #afficher le label, sans choisir ou c'est
    aides.mainloop()
#fonction qui s'occupe de gerer comment le jeu fonctionne le nb de lettre les proposition si c deja proposé si c gagné ou non
def valider(event):
    global bonnes_lettres  # variable que l'on utilise en dehors de la fonction
    global mauvaises_lettres
    global affichage
    global tentative
    proposition=entry_letter.get()  # récupère ce qu'il y a dans entry letter
    entry_letter.delete(0,tk.END)   # clear la case pour écrire
    proposition = proposition.lower()
    x = proposition.isalpha()
    if len(proposition) > 1 or x == False:
        label_error.config(text="erreur, recommencer")

    if len(proposition) <= 1 and x == True:  # vérifie si le mot est valide
        if proposition in bonnes_lettres or proposition in mauvaises_lettres: #vérifie si la lettre à déjà été proposé
            label_error.config(text=proposition + " a déjà été proposé!")
            return
        frequence.remove(proposition)  # enlève la proposition de la fréquence des lettres car elle a déjà été dite

        for i in range(len(mot_tab)):
            if proposition == mot_tab[i]:  # détermine si la lettre est dans le mot
                if proposition not in bonnes_lettres:
                    bonnes_lettres += [proposition]
                label_tab[i].config(text=str(proposition))   # configure l'astérix pour qu'il devienne la lettre déterminé à l'indice i
                affichage.pop()

        if proposition not in solution :#pour les tentative et la victoire
            mauvaises_lettres += [proposition]
            label_Faux.config(text="mauvaises lettres: " + str(mauvaises_lettres))
            tentative -= 1
            dessin()
            label_True.config(text="tentatives restantes: " + str(tentative))
        if tentative <= 0:
            tkinter.messagebox.showinfo("GAME OVER", "le mot est " + solution)
            reset()
        elif "*" not in affichage:
            tkinter.messagebox.showinfo("CONGRATULATIONS", "le mot est " + solution)
            reset()
root = tk.Tk()
root.title("PENDU")

label_tab = []
for i in range(len(mot_tab)):
    label = tk.Label(root, text="*", font=("Helvetica", 30))   # chaque étoiles = un label
    label.grid(row=2, column=i)
    label_tab.append(label)

label_error = tk.Label(root, text="")
label_error.grid(row=3,column=97)
label_Faux = tk.Label(root, text="")  # label mauvaises lettres
label_Faux.grid(row=3,column=98)
label_True = tk.Label(root, text="nombre de tentatives restantes: " + str(tentative))   # label tentative
label_True.grid(row=20,column=600)
label_True.grid(row=20,column=600)

entry_letter = tk.Entry(root, width=2, font=("Helvetica", 30), justify= CENTER)   # texte écrit au centre de la case
entry_letter.grid(row=20,column=700)
#programmation des boutons de tout les boutons
bouton_Valider= tk.Button(root, text="valider", bg="green", relief="groove", borderwidth=5, command=lambda : valider(any))   # lambda pour ajouter des paramètres/ any paramètre on met ce qu'on veut dedans
bouton_Valider.grid(row=20,column=1000)

Button_Indication = tk.Button(root, width=8, height=1, bg="grey", relief="groove", borderwidth=5, text="indication", command=indication)
Button_Indication.grid(row=0, column=700)

Button_Aide = tk.Button(root, width=5, height=1, bg="red", relief="groove", borderwidth=5, text="aide", command=aide)
Button_Aide.grid(row=0, column=1000)

canvas = tk.Canvas(root, bg="black", height=600, width=900)
canvas.grid(row= 600, column=1400)

def dessin():  #affichage du pendu en fonction des tentavives restante
    barres = []
    if tentative <=0:
        barres.append(canvas.create_line((220, 260), (180, 280), (220, 260), (260, 280), fill="white", width=3))
    if tentative <=1:
        barres.append(canvas.create_line((220, 210), (180, 230), (220, 210), (260, 230), fill="white", width=3))
    if tentative <=2:
        barres.append(canvas.create_line((220, 190), (220, 260), fill="white", width=3))
    if tentative <=3:
        barres.append(canvas.create_oval((200, 150), (240, 190), fill="black", outline= "white", width=3 ))
    if tentative <=4 :
        barres.append(canvas.create_line((220, 100), (220, 150), fill="white", width=5))
    if tentative <=5 :
        barres.append(canvas.create_line((20, 150), (50, 100), fill="white", width=5))
    if tentative <= 6 :
        barres.append(canvas.create_line((20, 100), (250, 100), fill="white", width=5))
    if tentative <=7 :
        barres.append(canvas.create_line((20, 98), (20, 353), fill="white", width=5))
    if tentative <=8:
        barres.append(canvas.create_line((20, 350), (200, 350), fill="white", width=5))

root.bind("<Return>",valider) # cliquer sur entré pour valider # # La méthode bind() permet de lier un événement avec une fonction 

def reset():
    rejouer = tk.Tk()
    rejouer.geometry("400x100")
    rejouer.title("Fin")

    def recommencer():
        dessin.suppu
        
        
    def quitter():
        root.destroy()
        rejouer.destroy()

    Button_Recommencer = tk.Button(rejouer, width=10, height=3, bg="green", relief="groove", borderwidth=5, text="rejouer", command=recommencer)
    Button_Recommencer.grid(row=400, column=1 )

    Button_Quitter = tk.Button(rejouer, width=10, height=3, bg="red", relief="groove", borderwidth=5, text="quitter", command=quitter)
    Button_Quitter.grid(row=400, column=100)

    rejouer.mainloop()

root.mainloop()


              
