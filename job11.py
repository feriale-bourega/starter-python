#!/usr/bin/env python3
import requests

def make_request():
    res = requests.get('https://reqres.in/api/users')

    print(res.json())


make_request()
pip install domain
fichier = open("domains.xml","r")
fichier.read()
from domains.xml import doc 
ldomaines = doc.getElementsByTagName("column name=domain")
print( len(ldomaines) ) 

