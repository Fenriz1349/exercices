#trouve le nombre aléatoire entre 1 et 100
import random
i=str(random.randint(1,100))
nb=input("saisissez un nombre entre 1 et 100 : ")
while nb != i :    
    if nb<i :
        nb=input("en dessous, retente :")
    elif nb>i :
        nb=input("au dessus, retente :")
    else:
        nb=input("nombre incorrect, saississez un nombre entre 1 et 100 :")
print("c'est gagné")