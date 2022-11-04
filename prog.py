import random

choixjoueur=0
choixordi=0
u=0
mylist=["1", "2", "3"]
n=0

while u!=1:
    choixjoueur=input("Faites un choix pierre(1), feuille(2) ou ciseaux(3) ?", )
    n=random.choice(mylist)
    choixordi=n
    print("choixordi = ", n)
    if choixjoueur=="1":
        if choixordi=="1":
            print("EGALITE")
        else:
            if choixordi=="2":
                print("ordi gagne")
            else:
                if choixordi=="3":
                    print("joueur1 gagne")
                else:
                    print("error")

    else:
        if choixjoueur=="2":
            if choixordi=="1":
                print("joueur1 gagne")
            else:
                if choixordi=="2":
                    print("EGALITE")
                else:
                    if choixordi=="3":
                        print("ordi gagne")
                    else:
                        print("error")
        else:
            if choixjoueur=="3":
                if choixordi=="1":
                    print("ordi gagne")
                else:
                    if choixordi=="2":
                        print("joueur1 gagne")
                    else:
                        if choixordi=="3":
                            print("EGALITE")
                        else:
                            print("error")
            else:
                if choixjoueur=="4":
                    u=1
                else:
                    print("error")
                    
    


