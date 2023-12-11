import random
vie=int(input("nombre de tentatives ? "))
N = random.randint(0,100)
for i in range(vie,0,-1):
    print("il vous reste ",i," vies")
    test=int(input("saisissez un nombre entre 0 et 100 "))
    if test==N:
        print("vous avez gagné !")
        break
    elif test>N:
        vie=-1
        print("au dessus")
        continue
    else :
        vie=-1
        print("en dessous")
        continue
else :print("vous avez perdu !")