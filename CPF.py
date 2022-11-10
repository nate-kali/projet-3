import random

choixjoueur=00
choixordi=0
u=0
mylist=["pierre", "feuille", "ciseaux"]
n=0
joueur1=0
joueur1 = input("Quel est ton pseudo ? ")

while u!=1:
    choixjoueur=input("Faites un choix pierre, feuille, ciseaux ou quitter ? ", )
    n=random.choice(mylist)
    choixordi=n
    print("Ordinateur = ", n)
    if choixjoueur=="pierre":
        if choixordi=="pierre":
            print("EGALITE")
        else:
            if choixordi=="feuille":
                print("ordi gagne")
            else:
                if choixordi=="ciseaux":
                    print(joueur1, "gagne")
                else:
                    print("error")

    else:
        if choixjoueur=="feuille":
            if choixordi=="pierre":
                print(joueur1, "gagne")
            else:
                if choixordi=="feuille":
                    print("EGALITE")
                else:
                    if choixordi=="ciseaux":
                        print("ordi gagne")
                    else:
                        print("error")
        else:
            if choixjoueur=="ciseaux":
                if choixordi=="pierre":
                    print("ordi gagne")
                else:
                    if choixordi=="feuille":
                        print(joueur1, "gagne")
                    else:
                        if choixordi=="ciseaux":
                            print("EGALITE")
                        else:
                            print("error")
            else:
                if choixjoueur=="puits":
                    if choixordi=="pierre":
                        print(joueur1, "t'as utilisé la carte de l'ancien ! T'as gagné")
                    else:
                        if choixordi=="feuille":
                            print("ordi gagne")
                        else:
                            if choixordi=="ciseaux":
                                print(joueur1, "t'as utilisé la carte de l'ancien ! T'as gagné")
                            else:
                                print("error")
                else:
                    if choixjoueur==("quitter"):
                        u=1
                    else:
                        print("error")