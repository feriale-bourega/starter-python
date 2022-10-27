#!/usr/bin/env python3
nombre = int(input("Entrer un nombre entier:"))
with open("data.txt","r")as fichier:
    lines = fichier.read()
nb_words = 0
for element in liste:
     if len(element) == nombre:
       nb_words = nb_words + 1
print(nb_words)
