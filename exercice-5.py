# -*- coding: utf-8 -*- 
# Exercie: les conditions / les boucles / Gestion des listes
import os

chemin = "C:\\FORMATION"

# les fonctions + Les conditions
# --------------------------------
def testchemin(arg):
    if os.path.exists(arg):
        if os.path.isdir(arg):
            return "Le chemin est un répertoire."
        else:
            return "Le chemin est un fichier."
    else:
        return "Le chemin n'existe pas"
    
print(testchemin(chemin))
print(testchemin("C:\\FORMATION\\20210201"))

# les boucles
# --------------------------------
maListe = os.listdir("C:\\FORMATION")
print(maListe)
monFichier = open(r"C:\FORMATION\listerep.txt","w")
for elementdemaliste in maListe:
    monFichier.write(elementdemaliste + "\n")
monFichier.close()

# Gestion des listes
# --------------------------------
v = [0,3,25,624]
print (v)
v.append(2365)
print(v)
for element in v:
    print(element)
# retourne l'élément pour l'index 4
print("Dernier élément : " + str(v[4]))