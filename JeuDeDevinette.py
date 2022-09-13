import random
nbr = random.randint(0, 1000)
choix = -1
nbrEssais = 0
print("J'ai choisi un nombre entre 0 et 1000, essai de le trouver")
while choix != nbr:
    choix = int(input("quel est votre choix?"))
    nbrEssais += 1
    if choix < nbr:
        print("Il est plus grand")
    elif choix > nbr:
        print("Il est plus petit")
    else:
        print("Vous avez réussits en", nbrEssais, "essais!")