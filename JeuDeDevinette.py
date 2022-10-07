import random
nbr = 99999
#definir choix
choix = -1
#definir le nombre d'essai
nbrEssais = 0
play_again = "y"
#definir les varables de choix
x = 0
y = 1000
def choice():
    global x
    global y
    global play_again
    global nbrEssais
    global nbr
    global choix
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
        nbrEssais = 0
    #demander a l'usager s'il veut rejouer
        play_again = input("voulez vous rejouer? y/n")

        return play_again

while play_again != "n":
    print("je choisi un nombre entre", x, "et", y,)
    #demander s'il veut changer les limites du nombre au hazard
    changement_nombre = input("voulez vous changer les limites du nombre? y/n")
    if changement_nombre == "y":
        #s'il veut, les changer
        x = int(input("vous voulez un chiffre entre"))
        y = int(input("et"))
    else:
        nbr = random.randint(x, y)
        # commencer le jeu
        print("J'ai choisi un nombre entre", x, "et", y, "essai de le trouver")
        choix = -1
        while choix != nbr:
            choice()
