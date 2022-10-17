#!/usr/bin/env python3 
var1 = int(input('Entrez votre valeur 1 : '))

var2 = int(input('Entrez votre valeur 2 : '))
for i in range(var1, var2):
    print(i, end=", ") 

if var1 == var2:
   print("Les valeurs sont égales")
