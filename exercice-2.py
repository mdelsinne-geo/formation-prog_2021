# -*- coding: utf-8 -*- 
# Exercice sur les formulaires
from tkinter import *

# Nouveau formulaire
fenetre = Tk()

## Exemple 1
## label
# label = Label(fenetre, text="Hello World")
# label.pack()
# fenetre.mainloop()

## Exemple 2
## label
#label = Label(fenetre, text="Hello World")
#label.pack()
## liste
#liste = Listbox(fenetre)
#liste.insert(1, "Python")
#liste.insert(2, "PHP")
#liste.insert(3, "jQuery")
#liste.insert(4, "CSS")
#liste.insert(5, "Javascript")
#liste.pack()
## boutonchk
#boutonchk = Checkbutton(fenetre, text="Nouveau?")
#boutonchk.pack()
## bouton
#bouton=Button(fenetre, text="Message", command=fenetre.quit)
#bouton.pack()
#fenetre.mainloop()

# Attributs de l'objet fenetre
fenetre.title("Intégration du cadastre")
fenetre.geometry("500x300")

# label
label = Label(fenetre, text="Choisir une commune")
label.pack()
# liste constituée à partir d'une requête SQL (liste.insert(code_insee,"code_insee - nom_commune")
liste = Listbox(fenetre,width=100)
liste.insert(85001,"85001 - L'AIGUILLON-SUR-MER")
liste.insert(85002,"85002 - L'AIGUILLON-SUR-VIE")
liste.insert(85003,"85003 - AIZENAY")
liste.insert(85004,"85004 - ANGLES")
liste.insert(85005,"85005 - ANTIGNY")
liste.pack()

def recupcommune():
    if len(liste.curselection()) > 0:
        print(liste.get(liste.curselection()))
    else:
        print("Aucune sélection trouvée")

# bouton
bouton=Button(fenetre, text="Intégrer", command= recupcommune)
bouton.pack()

# afficher
fenetre.mainloop()
