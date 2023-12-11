#trouver la bonne case entre 0 et 49, on triple la mise si on trouve, la moitié si c'est la même couleur(paire ou impaire), on perd la mise sinon
import random
import math

def pairImpaire(x):
    if x % 2 ==0:
        return "pair"
    else:
        return "impair"
    
caseRoulette=random.randint(0,49)
#print(caseRoulette)
cagnotte = int (input("entrez votre cagnotte de départ "))
while input("jouer encore ? (oui ou non)")=="oui":
    if cagnotte <= 0 :
        print("vous avez perdu toute votre cagnotte")
    else:
        mise = int (input("entrez votre mise "))
        choixCase=int (input("entrez votre case (entre 0 et 49)"))
        if choixCase ==caseRoulette:
            gain=mise*3
            cagnotte+=gain
            print ("bravo même case! Vous avez gagnez ",gain," votre cagnotte et de ",cagnotte)
        elif pairImpaire(choixCase)==pairImpaire(caseRoulette):
            gain=math.ceil(mise/2)
            cagnotte +=gain
            print ("bravo même couleur! Vous avez gagnez ",gain," votre cagnotte et de ",cagnotte)
        else :
            cagnotte-=mise
            print("perdu, vous avez perdu ",mise," votre cagnotte et de ",cagnotte)
        
