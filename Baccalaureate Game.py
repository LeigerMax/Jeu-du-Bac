from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from random import *
#--------------------fenetre--------------------
main = Tk()
main.title("Baccalaureate game ")
main.geometry("1200x950+300+10")
main.resizable(width=False,height=False)
canvas = Canvas(main, width=1200, height=950, background='black')
img_fond = PhotoImage(file='Images/tableau_fond.png')
image_fond = canvas.create_image(600,475,image=img_fond)
img_menu_petit = PhotoImage(file='Images/menu_petit.png')
img_menu_grand = PhotoImage(file='Images/menu_grand.png')
canvas.pack()
mot = ' '
sup = 0
score = 0
bonus = 0
texte_bonus = ' '
fin = 0
nom = ' '
#--------------------Menu --------------------
def bouton_jeu_event(event):
    print("game")
    main.withdraw()
    jeu = tk.Toplevel()
    jeu.title("Baccalaureate game ")
    jeu.geometry("1200x950+300+10")
    jeu.resizable(width=False,height=False)
    canvas = Canvas(jeu, width=1200, height=950,background='black')
    image_fond = canvas.create_image(600,475,image=img_fond)
    canvas.pack()
    img_monde = PhotoImage(file='Images/monde.png')
    img_metiers = PhotoImage(file='Images/metiers.png')
    img_animaux = PhotoImage(file='Images/animaux.png')
    img_sciences = PhotoImage(file='Images/sciences.png')
    img_couleurs = PhotoImage(file='Images/couleurs.png')
    img_musiques = PhotoImage(file='Images/musiques.png')


    def bouton_menu_event(event):
          print("menu")
          image_menu_grand = canvas.create_image(600,500,image=img_menu_grand)
          texte_menu = canvas.create_text(600, 400, text='Menu',font="Arial 50 ",fill="black")
          rect_retour = canvas.create_rectangle(700, 450, 500, 550, width=1, tags="obj1Tag",fill ="blue")
          texte_retour = canvas.create_text(600, 500, text='Back to menu',font="Arial 25 ", tags='texte_retour',fill="white")
          rect_quitter = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
          texte_quitter = canvas.create_text(600, 600, text='Quit',font="Arial 25 ", tags='texte_quitter',fill="white")
          canvas.tag_bind(rect_retour, '<ButtonPress-1>', bouton_retour)
          canvas.tag_bind('texte_retour', '<ButtonPress-1>', bouton_retour)
          canvas.tag_bind(rect_quitter, '<ButtonPress-1>', bouton_exit_menu)
          canvas.tag_bind('texte_quitter', '<ButtonPress-1>', bouton_exit_menu)

    def bouton_exit_menu(event):
        print("Quit")
        main.destroy()
        jeu.destroy()

    def bouton_retour(event):
        print("Back")
        jeu.destroy()
        main.deiconify()

    def bouton_enregistrer(event):
        global nom,score
        fi = open('Score/Score.txt','a')
        fi.write(str(score)) #Enregistre le score
        fi.write(' ')
        nom = nom.get()
        fi.write(nom) #Enregistre le nom
        fi.write('\n')
        print('score save')
        fi.close
        print("back")
        jeu.destroy()
        main.deiconify()

    #Bouton leaderscore et menu
    image_score = canvas.create_image(1150,50,image=img_score)
    canvas.tag_bind(image_score, '<ButtonPress-1>', bouton_score_event)
    image_menu_petit = canvas.create_image(1100,960,image=img_menu_petit)
    texte_menu = canvas.create_text(1100,910, text='Menu',font="Arial 25 ", tags='texte_menu',fill="black")
    canvas.tag_bind(image_menu_petit, '<ButtonPress-1>', bouton_menu_event)
    canvas.tag_bind('texte_menu', '<ButtonPress-1>', bouton_menu_event)
    texte_Maj = canvas.create_text(750, 750, text="The first letter need to be in capital letters ! ", font="Arial 24 italic",tags='texte_Maj', fill="white")


    def bouton_sciences(event):
        global mot,score,texte_entrez,image_1,texte_score,choix,bonus,fin,texte_bonus
        canvas.delete(jeu,texte_entrez)
        canvas.delete(jeu,image_1)
        canvas.delete(jeu,texte_score)
        canvas.delete(jeu,texte_bonus)
        fin = fin + 1
        print(mot.get())
        fi = open('Words/Science.txt','r')
        for i in fi: #chaque ligne du fichier
            if (i==mot.get()+"\n"):
                if mot.get()[0]  == choix:
                 print("+10")
                 score += 10
                 bonus = bonus + 1
                elif mot.get()[0] != choix:
                 print("Fail")
        if (bonus == 5) :
            print('bonus')
            texte_bonus = canvas.create_text(950,210, text='Bonus !',font="Arial 25 ", tags='texte_bonus',fill="red")
            bonus1 =  randint(0, 20)
            score += bonus1
            bonus = 0
        lettre= ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","R","S","T","U","V","X","Y","Z"]
        choix=choice(lettre)
        print(choix)
        texte_entrez = canvas.create_text(390, 200, text=' Enter a chemical element with the letter : '+choix,font="Arial 25 ",fill="white")
        image_1 = canvas.create_image(850,450,image=img_sciences)
        mot = Entry(canvas)
        canvas.create_window(250, 400, window=mot, height=50, width=200)
        mot.focus_set()
        #Bouton Suivant
        rect_suivant = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
        texte_suivant = canvas.create_text(600, 600, text='Next',font="Arial 25 ", tags='texte_suivant',fill="white")
        canvas.tag_bind(rect_suivant, '<ButtonPress-1>', bouton_pays)
        canvas.tag_bind('texte_suivant', '<ButtonPress-1>', bouton_pays)
        texte_score = canvas.create_text(950,150, text='Your score is : '+str(score),font="Arial 25 ", tags='texte_score',fill="white")
        fi.close()
    def bouton_metiers(event):
        global mot,score,texte_entrez,image_1,texte_score,choix,bonus,fin,texte_bonus
        canvas.delete(jeu,texte_entrez)
        canvas.delete(jeu,image_1)
        canvas.delete(jeu,texte_score)
        canvas.delete(jeu,texte_bonus)
        fin = fin + 1
        print(mot.get())
        fi = open('Words/Colors.txt','r')
        for i in fi: #chaque ligne du fichier
            if (i==mot.get()+"\n"):
                if mot.get()[0]  == choix:
                 print("+10")
                 score += 10
                 bonus = bonus + 1
                elif mot.get()[0] != choix:
                 print("Fail")
        if (bonus == 5) :
            print('bonus')
            texte_bonus = canvas.create_text(950,210, text='Bonus !',font="Arial 25 ", tags='texte_bonus',fill="red")
            bonus1 = randint(0, 20)
            score += bonus1
            bonus = 0
        lettre= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z"]
        choix=choice(lettre)
        print(choix)
        texte_entrez = canvas.create_text(310, 200, text='Enter a job with the letter : '+choix,font="Arial 25 ",fill="white")
        image_1 = canvas.create_image(850,450,image=img_metiers)
        mot = Entry(canvas)
        canvas.create_window(250, 400, window=mot, height=50, width=200)
        mot.focus_set()
        #Bouton Suivant
        rect_suivant = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
        texte_suivant = canvas.create_text(600, 600, text='Next',font="Arial 25 ", tags='texte_suivant',fill="white")
        canvas.tag_bind(rect_suivant, '<ButtonPress-1>', bouton_sciences)
        canvas.tag_bind('texte_suivant', '<ButtonPress-1>', bouton_sciences)
        texte_score = canvas.create_text(950,150, text='Your score is : '+str(score),font="Arial 25 ", tags='texte_score',fill="white")
        fi.close()
    def bouton_couleur(event):
        global mot,score,texte_entrez,image_1,texte_score,choix,bonus,fin,texte_bonus
        canvas.delete(jeu,texte_entrez)
        canvas.delete(jeu,image_1)
        canvas.delete(jeu,texte_score)
        canvas.delete(jeu,texte_bonus)
        fin = fin + 1
        print(mot.get())
        fi = open('Words/Capitals.txt','r')
        for i in fi: #chaque ligne du fichier
            if (i==mot.get()+"\n"):
                if mot.get()[0]  == choix:
                 print("+10")
                 score += 10
                 bonus = bonus + 1
                elif mot.get()[0] != choix:
                 print("Fail")
        if (bonus == 5) :
            print('bonus')
            texte_bonus = canvas.create_text(950,210, text='Bonus !',font="Arial 25 ", tags='texte_bonus',fill="red")
            bonus1 =  randint(0, 20)
            score += bonus1
            bonus = 0
        lettre= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z"]
        choix=choice(lettre)
        print(choix)
        texte_entrez = canvas.create_text(320, 200, text='Enter a color with the letter : '+choix,font="Arial 25 ",fill="white")
        image_1 = canvas.create_image(850,450,image=img_couleurs)
        mot = Entry(canvas)
        canvas.create_window(250, 400, window=mot, height=50, width=200)
        mot.focus_set()
        #Bouton Suivant
        rect_suivant = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
        texte_suivant = canvas.create_text(600, 600, text='Next',font="Arial 25 ", tags='texte_suivant',fill="white")
        canvas.tag_bind(rect_suivant, '<ButtonPress-1>', bouton_metiers)
        canvas.tag_bind('texte_suivant', '<ButtonPress-1>', bouton_metiers)
        texte_score = canvas.create_text(950,150, text='Your score is : '+str(score),font="Arial 25 ", tags='texte_score',fill="white")
        fi.close()
    def bouton_capitales(event):
        global mot,score,texte_entrez,image_1,texte_score,choix,bonus,fin,texte_bonus
        canvas.delete(jeu,texte_entrez)
        canvas.delete(jeu,image_1)
        canvas.delete(jeu,texte_score)
        canvas.delete(jeu,texte_bonus)
        fin = fin + 1
        print(mot.get())
        fi = open('Words/Musics.txt','r')
        for i in fi: #chaque ligne du fichier
            if (i==mot.get()+"\n"):
                if mot.get()[0]  == choix:
                 print("+10")
                 score += 10
                 bonus = bonus + 1
                elif mot.get()[0] != choix:
                 print("Fail")
        if (bonus == 5) :
            print('bonus')
            texte_bonus = canvas.create_text(950,210, text='Bonus !',font="Arial 25 ", tags='texte_bonus',fill="red")
            bonus1 =  randint(0, 20)
            score += bonus1
            bonus = 0
        lettre= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","Y","Z"]
        choix=choice(lettre)
        print(choix)
        texte_entrez = canvas.create_text(325, 200, text='Enter a capital with the letter : '+choix,font="Arial 25 ",fill="white")
        image_1 = canvas.create_image(850,450,image=img_monde)
        mot = Entry(canvas)
        canvas.create_window(250, 400, window=mot, height=50, width=200)
        mot.focus_set()
        #Bouton Suivant
        rect_suivant = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
        texte_suivant = canvas.create_text(600, 600, text='Next',font="Arial 25 ", tags='texte_suivant',fill="white")
        canvas.tag_bind(rect_suivant, '<ButtonPress-1>', bouton_couleur)
        canvas.tag_bind('texte_suivant', '<ButtonPress-1>', bouton_couleur)
        texte_score = canvas.create_text(950,150, text='Your score is : '+str(score),font="Arial 25 ", tags='texte_score',fill="white")
        fi.close()
    def bouton_musiques(event):
        global mot,score,texte_entrez,image_1,texte_score,choix,bonus,fin,texte_bonus
        canvas.delete(jeu,texte_entrez)
        canvas.delete(jeu,image_1)
        canvas.delete(jeu,texte_score)
        canvas.delete(jeu,texte_bonus)
        fin = fin + 1
        print(mot.get())
        fi = open('Words/Animals.txt','r')
        for i in fi: #chaque ligne du fichier
            if (i==mot.get()+"\n"):
                if mot.get()[0]  == choix:
                 print("+10")
                 score += 10
                 bonus = bonus + 1
                elif mot.get()[0] != choix:
                 print("Fail")
        if (bonus == 5) :
            print('bonus')
            texte_bonus = canvas.create_text(950,210, text='Bonus !',font="Arial 25 ", tags='texte_bonus',fill="red")
            bonus1 = randint(0, 20)
            score += bonus1
            bonus = 0
        lettre= ["A","B","C","F","G","H","M","O","P","S","T","V","X"]
        choix=choice(lettre)
        print(choix)
        texte_entrez= canvas.create_text(340, 200, text='Enter an instrument with the letter : '+choix,font="Arial 25 ",fill="white")
        image_1 = canvas.create_image(850,450,image=img_musiques)
        mot = Entry(canvas)
        canvas.create_window(250, 400, window=mot, height=50, width=200)
        mot.focus_set()
        #Bouton Suivant
        rect_suivant = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
        texte_suivant = canvas.create_text(600, 600, text='Next',font="Arial 25 ", tags='texte_suivant',fill="white")
        canvas.tag_bind(rect_suivant, '<ButtonPress-1>', bouton_capitales)
        canvas.tag_bind('texte_suivant', '<ButtonPress-1>', bouton_capitales)
        texte_score = canvas.create_text(950,150, text='Your score is : '+str(score),font="Arial 25 ", tags='texte_score',fill="white")
        fi.close()
    def bouton_animaux(event):
        global mot,score,texte_entrez,image_1,sup,texte_score,choix,bonus,texte_bonus,fin,nom
        canvas.delete(jeu,texte_bonus)
        canvas.delete(jeu,texte_entrez)
        canvas.delete(jeu,image_1)
        canvas.delete(jeu,texte_score)
        sup = 1
        fin = fin + 1
        print(mot.get())
        fi = open('Words/Country.txt','r')
        for i in fi: #chaque ligne du fichier
            if (i==mot.get()+"\n"):
                if mot.get()[0]  == choix:
                 print("+10")
                 score += 10
                 bonus = bonus + 1
                elif mot.get()[0] != choix:
                 print("Fail")
        if (bonus == 5) :
            print('bonus')
            texte_bonus = canvas.create_text(950,210, text='Bonus !',font="Arial 25 ", tags='texte_bonus',fill="red")
            bonus1 = randint(0, 20)
            score += bonus1
            bonus = 0
        if (fin == 16) : #Fin programme
            print('End')
            canvas.delete(jeu,ALL)
            image_fond = canvas.create_image(600,475,image=img_fond)
            texte_score = canvas.create_text(500,350, text='Your score is : '+str(score),font="Arial 50 ", tags='texte_score',fill="white")
            nom = Entry(canvas)
            canvas.create_window(600, 500, window=nom, height=50, width=200)
            nom.focus_set()
            rect_save = canvas.create_rectangle(750, 550, 450, 650, width=1, tags="obj1Tag",fill ="green")
            texte_save = canvas.create_text(600, 600, text='Save score',font="Arial 25 ", tags='texte_save',fill="white")
            texte_nom = canvas.create_text(600, 450, text='Name :',font="Arial 25 ", tags='texte_save',fill="white")
            canvas.tag_bind(rect_save, '<ButtonPress-1>', bouton_enregistrer)
            canvas.tag_bind('texte_save', '<ButtonPress-1>', bouton_enregistrer)
            print("End")
        else :
            lettre= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            choix=choice(lettre)
            print(choix)
            texte_entrez = canvas.create_text(310, 200, text='Enter an animal with the letter : '+choix,font="Arial 25 ",fill="white")
            image_1 = canvas.create_image(850,450,image=img_animaux)
            mot = Entry(canvas)
            canvas.create_window(250, 400, window=mot, height=50, width=200)
            mot.focus_set()
            #Bouton Suivant
            rect_suivant2 = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
            texte_suivant2 = canvas.create_text(600, 600, text='Next',font="Arial 25 ", tags='texte_suivant2',fill="white")
            canvas.tag_bind(rect_suivant2, '<ButtonPress-1>', bouton_musiques)
            canvas.tag_bind('texte_suivant2', '<ButtonPress-1>', bouton_musiques)
            texte_score = canvas.create_text(950,150, text='Your score is : '+str(score),font="Arial 25 ", tags='texte_score',fill="white")
            fi.close()
    def bouton_pays(event):
        global mot,score,texte_entrez,image_1,sup,texte_score,choix,bonus,texte_bonus,fin #le mot est repris
        fin = fin + 1
        if sup == 1 :
         canvas.delete(jeu,texte_entrez)
         canvas.delete(jeu,image_1)
         canvas.delete(jeu,texte_score)
         canvas.delete(jeu,texte_bonus)
         print(bonus)
         print(mot.get())
         fi = open('Words/Science.txt','r') #on ouvre le fichier qui permet de vérifier le mot entrez avant.
         for i in fi: #chaque ligne du fichier
            if (i==mot.get()+"\n"):
                if mot.get()[0]  == choix:
                 print("+10")
                 score += 10
                 bonus = bonus + 1
                elif mot.get()[0] != choix:
                 print("Fail")
         if (bonus == 5) :
            print('bonus')
            texte_bonus = canvas.create_text(950,210, text='Bonus !',font="Arial 25 ", tags='texte_bonus',fill="red")
            bonus1 = randint(0, 20)
            score += bonus1
            fin +=1
            bonus = 0
        lettre= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Y","Z"] #Lance une nouvelle recherche parmi les lettres
        choix=choice(lettre) #prend une lettre
        print(choix)
        texte_entrez = canvas.create_text(300, 200, text='Enter a country with the letter: : '+choix,font="Arial 25 ",fill="white") #affiche le texte avec la lettre
        image_1 = canvas.create_image(850,450,image=img_monde)
        mot = Entry(canvas)
        canvas.create_window(250, 400, window=mot, height=50, width=200)
        mot.focus_set()
        #Bouton Suivant et score
        rect_suivant = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
        texte_suivant = canvas.create_text(600, 600, text='Next',font="Arial 25 ", tags='texte_suivant',fill="white")
        canvas.tag_bind(rect_suivant, '<ButtonPress-1>', bouton_animaux) #Envoie l'utilisateur dans def bouton_animaux, le mot sera vérifier là-bas
        canvas.tag_bind('texte_suivant', '<ButtonPress-1>', bouton_animaux)
        texte_score = canvas.create_text(950,150, text='Your score is : '+str(score),font="Arial 25 ", tags='texte_score',fill="white")
        fi.close() #ferme le fichier
    #Bouton Lancer
    rect_lancer = canvas.create_rectangle(700, 550, 500, 650, width=1, tags="obj1Tag",fill ="green")
    texte_lancer = canvas.create_text(600, 600, text='Play',font="Arial 25 ", tags='texte_lancer',fill="white")
    canvas.tag_bind(rect_lancer, '<ButtonPress-1>', bouton_pays) #Le bouton lancer envoie au def bouton_pays
    canvas.tag_bind('texte_lancer', '<ButtonPress-1>', bouton_pays)

def bouton_regle_event(event):
    print("Rules")
    main.withdraw()
    regle = tk.Toplevel()
    regle.title("Baccalaureate game - Rules")
    regle.geometry("1200x950+300+10")
    regle.resizable(width=False,height=False)
    canvas = Canvas(regle, width=1200, height=950)
    image = canvas.create_image(600,475,image=img_fond)
    regle_titre = canvas.create_text(120, 200, text="Rules", font="Arial 38 italic", fill="white")
    relge_1 = canvas.create_text(600, 250, text="The game of the baccalaureate or bac game, more familiarly small bac, is a board game and letters, the goal is to find, in writing ", font="Arial 13 italic", fill="white")
    regle_2 = canvas.create_text(600, 300, text="and with a limited number of hits, a series of words belong to categories predefined by the players and starting with the given letter", font="Arial 13 italic", fill="white")
    relge_4 = canvas.create_text(600, 350, text="The game will allow students to learn geography or even chemical elements for science, capitals, animals.", font="Arial 13 italic", fill="white")
    relge_4 = canvas.create_text(600, 400, text="The goal ? do as many points as you can! Each good answer is worth one point and sometimes bonuses between 1 to 20 points appear", font="Arial 13 italic", fill="white")
    relge_5 = canvas.create_text(600, 450, text="Do not put a word in front of the answers' for example 'giraffe' instead of 'a giraffe'", font="Arial 13 italic", fill="white")
    canvas.pack()

    def bouton_retour(event):
        print("Back")
        regle.destroy()
        main.deiconify()

    #Bouton retour
    image_menu_petit = canvas.create_image(1100,960,image=img_menu_petit)
    texte_retour = canvas.create_text(1100,910, text='Back',font="Arial 25 ", tags='texte_retour',fill="black")
    canvas.tag_bind(image_menu_petit, '<ButtonPress-1>', bouton_retour)
    canvas.tag_bind('texte_retour', '<ButtonPress-1>', bouton_retour)



def bouton_parametre_event(event):
    print("Settings")


def bouton_exit_event(event):
    print("Quit")
    main.destroy()


def bouton_score_event(event):
    print("score")
    main.withdraw()
    score = tk.Toplevel()
    score.title("Baccalaureate game - Score")
    score.geometry("1200x950+300+10")
    score.resizable(width=False,height=False)
    canvas = Canvas(score, width=1200, height=950)
    image = canvas.create_image(600,475,image=img_fond)
    titre = canvas.create_text(150, 200, text="Score", font="Arial 38 italic", fill="white")
    canvas.pack()
    fi = open('Score/Score.txt','r')
    texte_score = canvas.create_text(550, 400, text=fi.read(), font="Arial 20 italic", fill="white")
    fi.close()

    def bouton_retour(event):
        print("Back")
        score.destroy()
        main.deiconify()

    image_menu_petit = canvas.create_image(1100,960,image=img_menu_petit)
    texte_retour = canvas.create_text(1100,910, text='Back',font="Arial 25 ", tags='texte_retour',fill="black")
    canvas.tag_bind(image_menu_petit, '<ButtonPress-1>', bouton_retour)
    canvas.tag_bind('texte_retour', '<ButtonPress-1>', bouton_retour)


def bouton_info_event(event):
    showinfo("Credits", "Game develloped by : Allemeersch Maxime , Juwé Arthur , Kahvecioglu Adem, Lallemand Manuel")



#--------------------Menu interface--------------------

#Interface et titre
img_fond_mots = PhotoImage(file='Images/anglais.png')
image_fond_menu = canvas.create_image(850,325,image=img_fond_mots)
titre = canvas.create_text(360, 200, text="Baccalaureate game", font="Arial 38 italic", fill="white")
canvas.pack()

#lancer
img_lancer = PhotoImage(file='Images/lancer.png')
image_lancer = canvas.create_image(450,400,image=img_lancer)
texte_lancer = canvas.create_text(450, 400, text='Play',font="Arial 30 ", tags='texte_lancer',fill="white")
canvas.tag_bind(image_lancer, '<ButtonPress-1>', bouton_jeu_event)
canvas.tag_bind('texte_lancer', '<ButtonPress-1>', bouton_jeu_event)

#Règle
img_regle = PhotoImage(file='Images/regle.png')
image_regle = canvas.create_image(550,500,image=img_regle)
texte_regle = canvas.create_text(550, 500, text='Rules',font="Arial 30 ", tags='texte_regle',fill="white")
canvas.tag_bind(image_regle, '<ButtonPress-1>', bouton_regle_event)
canvas.tag_bind('texte_regle', '<ButtonPress-1>', bouton_regle_event)

#Quitter
img_quitter = PhotoImage(file='Images/quitter.png')
image_quitter = canvas.create_image(680,590,image=img_quitter)
texte_quitter = canvas.create_text(680, 590, text='Quit',font="Arial 30 ", tags='texte_quitter',fill="white")
canvas.tag_bind(image_quitter, '<ButtonPress-1>', bouton_exit_event)
canvas.tag_bind('texte_quitter', '<ButtonPress-1>', bouton_exit_event)

#score
img_score = PhotoImage(file='Images/score.png')
image_score = canvas.create_image(1150,50,image=img_score)
canvas.tag_bind(image_score, '<ButtonPress-1>', bouton_score_event)

#Info
img_info = PhotoImage(file='Images/info.png')
img_info.size = 10, 10
image_info = canvas.create_image(1150,900,image=img_info)
canvas.tag_bind(image_info, '<ButtonPress-1>', bouton_info_event)

main.mainloop()

