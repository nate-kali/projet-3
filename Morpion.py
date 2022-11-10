#######################################################################
#######################################################################
###                                                                 ###
###                                                                 ###
###                                                                 ###
###                    Jeu du Morpion crée par :                    ###
###                     Pierre, Nathan et Aurel                     ###
###                          Groupe 4.20                            ###
###                                                                 ###
###                                                                 ###
#######################################################################
#######################################################################
from tkinter import *
from tkinter import messagebox
#------------------------------------------#
cases=[ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
forme=True   #true pour les croix, false pour les ronds
n=1   #numéro du tour 
somme=0

#-----------------------------------------#
def interface(event) :                         #en entrée : événement de la souris
    global forme, cases, n                     #en sortie : affiche les coordonnées (simplifiée) de la case du clic de souris
    l = (event.y-2)//100 #ligne clic
    c = (event.x-2)//100 #colonne clic
    print(l,c)
    

    if (n < 10) and (cases[l][c]==0):
        if forme:   #forme == True
            morpion.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width=4, fill="blue")
            morpion.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width=4, fill="blue")
            cases[l][c]=1
        else:
            morpion.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width=2, fill="red")
            cases[l][c]=-1
        forme = not(forme)
        if (n >= 5) and (n <= 9):
            if somme==1 or somme==(-1):
                forme=False
        if n==9:
            bouton_estegg.config (state = NORMAL)
            egal()
            
        n=n+ 1


def rejouer():
    global forme, cases, n
    cases=[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
    forme=True  #true pour les croix, false pour les ronds
    n=1
    morpion.delete(ALL) #efface croix et rond
    lignes = []
    for i in range(4):
      lignes.append(morpion.create_line(0, 100*i+2, 303, 100*i+2, width=3))
      lignes.append(morpion.create_line(100*i+2, 0, 100*i+2, 303, width=3))
    bouton_estegg.config (state = DISABLED)   
     
def egal():
    messagebox.showinfo("", "EGALITE")      
      
def easteregg():
    messagebox.showinfo('HEY !', 'Tu as découvert un Easter Egg') 


#------------------------------------------#
jeu=Tk()
jeu.title('Morpion Groupe 4.20')


#------------------------------------------#
bouton_quitter = Button(jeu, text='Arrêter de jouer', command=jeu.destroy)
bouton_quitter.grid(row=2, column=1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(jeu, text='Rejouer', command=rejouer)
bouton_reload.grid(row=2, column=0, padx=3, pady=3, sticky = S+W+E)

bouton_estegg = Button(jeu, text="?", command=easteregg)
bouton_estegg.config (state = DISABLED)                                                                         #Easter Egg
bouton_estegg.grid(row=3, column=3, padx=1, pady=1, sticky=S+W+E)


#-------------------------------------------#
morpion=Canvas(jeu, bg="white", width=300, height=300)
morpion.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


#------------------------------------------#
lignes = []

#------------------------------------------#
morpion.bind('<Button>', interface)

#------------------------------------------#
rejouer()
jeu.mainloop()  #fin                   