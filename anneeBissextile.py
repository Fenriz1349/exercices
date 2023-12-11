# test de la fonction input
année = input("saissis l'année : ")
année = int(année)
if année % 400 == 0 or (année % 4 == 0 and année %100 !=0 ):
    print("l'année est bissextile")
else :
    print ("l'année n'est pas bissextile")
