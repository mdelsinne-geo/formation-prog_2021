# -*- coding: utf-8 -*- 
# Manipulation des fichiers

# importer le module os permettant la manipulation de dossiers et fichiers
import os

# tester la présence d'un fichier et/ou repertoire
print(os.path.exists("C:\\FORMATION"))

# tester si le chemin est un fichier ou un répertoire
print(os.path.isfile("C:\\FORMATION"))
print(os.path.isdir("C:\\FORMATION"))

# créer un répertoire
print(os.path.exists("C:\\FORMATION\\20210125"))
if os.path.exists("C:\\FORMATION\\20210125") == False:
   os.mkdir(r"C:\FORMATION\20210125")

# lister le contenu du répertoire
print(os.listdir("C:\\FORMATION"))

# créer un fichier log.txt
fw = open(r"C:\FORMATION\20210125\log.txt","w")

# intégrer la valeur "Bonjour tout le monde"
fw.write("Bonjour tout le monde\n")
fw.write("Au revoir")
fw.close()

# lire le contenu d'un fichier
fr = open(r"C:\\FORMATION\\20210125\\log.txt","r")
print(fr.readline())