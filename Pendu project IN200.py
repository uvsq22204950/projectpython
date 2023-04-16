import tkinter as tk
from tkinter import *
import tkinter.messagebox
import random
import copy

frequence = ["e", "s", "a", "r", "t", "i", "n", "u", "l", "o", "d", "c", "j", "b", "m", "p", "v", "q", "f", "g", "h", "x", "y", "z", "w", "k" ]
mot = 'boulet'
liste_de_mot = [mot]
tentative=8

solution = random.choice(liste_de_mot)
mot_tab=[]
for i in solution:
    mot_tab.append(i)

mauvaises_lettres = []
bonnes_lettres = []
tentative = 8
affichage=[]
for i in range(len(mot_tab)):
    affichage.append("_")

def indication():
    entry_letter.delete(0,tk.END)
    entry_letter.insert(0,frequence[0])

def aide():
    aides =tk.Tk()
    label = tk.Label(aides, text="Le but du jeu est simple : deviner toutes les lettres qui doivent composer un mot, éventuellement avec un nombre limité de tentatives et des thèmes fixés à l'avance.\n" + "A chaque fois que le joueur devine une lettre, celle-ci est affichée. Dans le cas contraire, le dessin d'un pendu se met à apparaître", font=("Helvetica", 9))
    label.pack()
    aides.mainloop()

def valider(event):
    global bonnes_lettres
    global mauvaises_lettres
    global affichage
    global tentative
    proposition=entry_letter.get()
    entry_letter.delete(0,tk.END)
    proposition = proposition.lower()
    x = proposition.isalpha()
    if len(proposition) > 1 or x == False:
        label_error.config(text="erreur, recommencer")

    if len(proposition) <= 1 and x == True:
        if proposition in bonnes_lettres or proposition in mauvaises_lettres:
            label_error.config(text=proposition + " a déjà été proposé!")
            return
        frequence.remove(proposition)

        for i in range(len(mot_tab)):
            if proposition == mot_tab[i]:
                if proposition not in bonnes_lettres:
                    bonnes_lettres += [proposition]
                label_tab[i].config(text=str(proposition))
                affichage.pop()

        if proposition not in mot:
            mauvaises_lettres += [proposition]
            label_F.config(text="mauvaises lettres: " + str(mauvaises_lettres))
            tentative -= 1
            label_T.config(text="tentatives restantes: " + str(tentative))
        if tentative <= 0:
            tkinter.messagebox.showinfo("GAME OVER", "le mot est " + mot)
            root.destroy()
        elif "_" not in affichage:
            tkinter.messagebox.showinfo("CONGRATULATIONS", "le mot est " + mot)
            root.destroy()
root = tk.Tk()
root.title("PENDU")

label_tab = []
for i in range(len(mot_tab)):
    label = tk.Label(root, text="_", font=("Helvetica", 30))
    label.grid(row=2, column=i)
    label_tab.append(label)

label_error = tk.Label(root, text="")
label_error.grid(row=3,column=97)
label_F = tk.Label(root, text="")
label_F.grid(row=3,column=98)
label_T = tk.Label(root, text="nombre de tentatives restantes: " + str(tentative))
label_T.grid(row=20,column=600)

entry_letter = tk.Entry(root, width=2, font=("Helvetica", 30), justify= CENTER)
entry_letter.grid(row=20,column=700)

bouton_V= tk.Button(root, text="valider", bg="green", relief="groove", borderwidth=5, command=lambda : valider(any))
bouton_V.grid(row=20,column=1000)

ButtonI = tk.Button(root, width=8, height=1, bg="grey", relief="groove", borderwidth=5, text="indication", command=indication)
ButtonI.grid(row=0, column=700)

ButtonA = tk.Button(root, width=5, height=1, bg="red", relief="groove", borderwidth=5, text="aide", command=aide)
ButtonA.grid(row=0, column=1000)


root.bind("<Button-3>",valider)

root.mainloop()
