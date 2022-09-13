import random
#choisir un nombre au hazard
nbr = random.randint(0, 1000)
#definir choix
choix = -1
#definir le nombre d'essai
nbrEssais = 0
#commencer le jeu
print("J'ai choisi un nombre entre 0 et 1000, essai de le trouver")
while choix != nbr:
    #demender le choix du joueur
    choix = int(input("quel est votre choix?"))
    #ajouter un essai
    nbrEssais += 1
    #definir sil est plus grand ou plus petit
    if choix < nbr:
        print("Il est plus grand")
    elif choix > nbr:
        print("Il est plus petit")
    #s'il réussit
    else:
        print("Vous avez réussits en", nbrEssais, "essais!")