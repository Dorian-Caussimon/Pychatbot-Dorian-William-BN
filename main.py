# "My first chatBot" - Projet semestriel TI101 (Programmation Python)
# [L1 - BN]
# KUANG William - CAUSSIMON Dorian
# Fichier main.py : Contient le menu et permet l'appel des fonctionnalités réalisées dans function.py

from fonction import *
# Permet d'avoir la liste des fichiers
directory = "./speeches"
files_names = list_of_files(directory,'txt')

# Nettoyage des .txt
cleaned(files_names)
matrice_TF_IDF, dico_list = TF_IDF(files_names)


# Menu d'accès aux fonctionnalités
fin = 0
while fin == 0:
    x = 0
    print("1 - Les mots les moins important du corpus \n"
          "2 - Les mots avec le TF-IDF le plus élevé \n"
          "3 - Les mots les plus répétés par un président \n"
          "4 - Qui a parlé de... \n"
          "5 - Accès au chatBot \n"
          "6 - Sortir du programme \n")

    while x <= 0 or x > 7:
          x = int(input("Entrez la fonctionnalité désirée : "))
          if x <= 0 or x > 7:
                print("Cette fonctionnalité n'existe pas. \n")

    if x == 1:
        mot_pas_important = []
        for i in range (1,len(files_names)+1):
            dico = dico_list["dico{}".format(i)]
            for mot, val in dico.items():
                if val == 0:
                    mot_pas_important.append(mot)
        print(mot_pas_important)

    elif x == 2:
        mot_important = 0
        cpt = 0
        for i in range (1,len(files_names)+1):
            dico = dico_list["dico{}".format(i)]
            for mot, val in dico.items():
                if val > cpt:
                    cpt = val
                    mot_important = mot
        print(mot_important)

    elif x == 3:
        print("1 - Chirac \n"
              "2 - Chirac 2 \n"
              "3 - Giscard d'Estaing \n"
              "4 - Hollande \n"
              "5 - Macron \n"
              "6 - Mitterand \n"
              "7 - Mitterand \n"
              "8 - Sarkozy \n")
        X = int(input("Sélectionnez un président : "))
        Mot_repete = 0
        cpt = 0
        dico = dico_list["dico{}".format(X)]
        for mot, val in dico.items():
            if val > cpt:
                cpt = val
                Mot_repete = mot
        print("Le mot le plus répété est : {}".format(Mot_repete))

    elif x == 4:
        print('Donnez un mot à rechercher : ')
        mot_recherche = str(input())
        premier = []
        for D in files_names:
            with open('./cleaned/{}'.format(D),"r") as d:
                texte = d.readlines()
                for ligne in texte:
                    if (" {} ".format(mot_recherche) or '{} '.format(mot_recherche) or ' {}'.format(mot_recherche)) in ligne:
                        premier.append(D)
        premier = set(premier) # supprimer les doublon
        print('Le premier president à avoir parlé de {} est {}'.format(mot_recherche,premier))
    elif x == 5:
        new_matrice, lng = matrice_pour_comparaison(matrice_TF_IDF)
        print("Posez une question : ")
        question = str(input())
        Q = clean_question(question)
        QC = comparaison_question(Q)
        TFIDFQ_veteur, TFIDFQ_dico = question_TF_IDF(QC, lng)
        sim,doc = pertinence(new_matrice, TFIDFQ_veteur)
        mot_retourner = MAX_TF_IDF(TFIDFQ_dico)
        print(doc)
        print(reponse(question,mot_retourner,doc))
    elif x == 6:
        fin = 1

# STOP