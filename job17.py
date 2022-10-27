#!/usr/bin/env python3
def myFunction(*params):
    mylist = []
    for param in params:
        if isinstance(param,(int)):
           mylist.append(param)
        else:
            print("Attention un de mes paramètres n'est pas numérique)
        for element in mylist:
            if element%2 == 0:
                 print(element)
myFunction(3,6,89,78,66,"kJHJH",2)
