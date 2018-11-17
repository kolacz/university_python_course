from random import random
from math import floor

def rzut_kostka():
    return int(random()*6+1)

def tura():
    x = rzut_kostka() + rzut_kostka()
    y = rzut_kostka() + rzut_kostka()
    print("Komputer: ",x,", przeciwnik: ",y)
    return x-y 

def gra(n):
    z1=0 
    z2=0
    #n-rundowa rozgrywka
    for i in range(1,n+1):
        print("--- Runda nr:",i," ---")
        x = tura()
        if x>0:
            z1+=1
        elif x<0:
            z2+=1
        else: pass
        print("Wygrane : przegrane komputera: ",z1,":",z2,"\n")
    #jeśli remis
    while(z1==z2):
        i+=1
        print("--- Runda nr:",i," ---")
        x = tura()
        if x>0:
            z1+=1
        elif x<0:
            z2+=1
        else: pass
        print("Wygrane : przegrane komputera: ",z1,":",z2,"\n")

    res = "Komputer wygrał." if z1>z2 else "Przeciwnik wygrał."
    print(res)
                

