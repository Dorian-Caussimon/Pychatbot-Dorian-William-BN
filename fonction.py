# "My first chatBot" - Projet semestriel TI101 (Programmation Python)
# [L1 - BN]
# KUANG William - CAUSSIMON Dorian
# Fichier function.py : Contient les fonctionnalités réalisées

import os
import math

# Liste des ponctuations
ponctuation = [",", ".", "!", ":", "?", ";"]

# Liste des dictionnaires
Chirac1 = {}
Chirac2 = {}
Giscard_dEstaing = {}
Hollande = {}
Macron = {}
Mitterrand = {}
Mitterrand2 = {}
Sarkozy = {}
dico_list = {'dico1': Chirac1,
             'dico2': Chirac2,
             'dico3': Giscard_dEstaing,
             'dico4': Hollande,
             'dico5': Macron,
             'dico6': Mitterrand,
             'dico7': Mitterrand2,
             'dico8': Sarkozy}

# Fonction 'list_of_files'
# Liste les fichiers avec l'extension (.txt)
# Retourne la liste des noms des fichiers correspondant aux critères
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Permet d'avoir la liste des fichiers
directory = "./speeches"
files_names = list_of_files(directory, 'txt')
nb_de_fichier = len(files_names)

# Fonction 'cleaned'
# Nettoie le contenu des fichiers .txt en effectuant plusieurs opérations
# Ajoute les .txt nettoyés dans le fichier 'cleaned'
def cleaned (files_names):
    for nom in files_names:
        # Ouvre les fichers .txt à nettoyer
        with open('./speeches/{}'.format(nom), 'r', encoding="utf-8") as f1:
            F = f1.readlines()

            # Nouveau fichier "cleaned" pour les .txt traités
            with open('./cleaned/{}'.format(nom), 'w', encoding="utf-8") as f2:

                # Divise les .txt en lignes
                for ligne in F:

                    # Divise les lignes en lettres
                    for lettre in ligne:
                        l_ascii = ord(lettre)

                        # Converti les majuscules en miniscules
                        if l_ascii >= 65 and l_ascii <= 90:
                            l_ascii += 32
                            new_lettre = chr(l_ascii)
                            f2.write(new_lettre)

                        # Miniscules
                        elif l_ascii >=97 and l_ascii <= 122:
                            f2.write(lettre)

                        # Cas particulier  (è ; é ; ê)
                        elif l_ascii >= 232 and l_ascii <= 234:
                            f2.write('e')

                        # Cas particulier (â ; à)
                        elif l_ascii == 224 or l_ascii == 226:
                            f2.write('a')

                        # Cas particulier (û ; ù)
                        elif l_ascii == 251 or l_ascii == 249:
                            f2.write('u')

                        # Cas particulier (ç)
                        elif l_ascii == 231:
                            f2.write('c')

                        # Cas particulier (" " ; "-")
                        elif lettre == " " or lettre == "-":
                            f2.write(" ")

                        # Cas particulier ("'")
                        elif lettre == "'":
                            f2.write("e ")

                        # Cas particulier ("ô")
                        elif lettre == "ô":
                            f2.write('o')

                        # Cas particulier ('œ')
                        elif lettre == 'œ':
                            f2.write("o")
                            f2.write('e')

                        # Ponctuations
                        else:
                            for ponct in ponctuation:
                                if ponct == lettre:
                                    f2.write('')
                    f2.write("\n")
    return

# Fonction 'TF'
# Calcule la fréquence d'apparition de chaque mot d'un .txt
# Retourne le dictionnaire 'cptTF' contenant la fréquence de chaque mot
def TF(contenu):
    cptTF = {}
    liste_mots = contenu.split()
    for mot in liste_mots:
        if mot not in cptTF: # Calcule la fréquence TF de chaque mot
            cptTF[mot] = 1
        else:
            cptTF[mot] += 1
    return cptTF # Retourne la fréquence de chaque mot

# Fonction 'IDF'
# Calcule le score IDF de chaque .txt
# Retourne le dictionnaire 'cptIDF' contenant le score IDF de chaque mot
def IDF(files_names):
    precptIDF = {}
    cptIDF = {}
    for val in files_names:
        with open('./cleaned/{}'.format(val), 'r', encoding="utf-8") as f:
            contenu = f.read()
            cptTF = TF(contenu) # Utilisation de la fonction TF pour le calcul de l'IDF
            for mot, val in cptTF.items():
                if mot not in precptIDF: # Nombre de .txt contenant chaque mot (1 à 8)
                    precptIDF[mot] = 1
                else:
                    precptIDF[mot] += 1
            for mot, val in precptIDF.items(): # Calcule l'IDF de chaque mot
                cptIDF[mot] = math.log((nb_de_fichier/val))
    return cptIDF

# Fonction 'TF_IDF'
# Calcule la matrice TF-IDF avec les fonctions 'TF' et 'IDF'
# Retourne la matrice contenant les valeurs TF-IDF de chaque mot du corpus
def TF_IDF(files_name):
    cptIDF = IDF(files_name)
    prematrice_TF_IDF = []
    for i in range (len(files_name)):
        with open('./cleaned/{}'.format(files_name[i]), 'r', encoding="utf-8") as f:
            contenu = f.read()
            cptTF = TF(contenu)

            for mot in cptTF.keys(): # Calcule de TF_IDF pour chaque mot
                cptTF[mot] = round(cptIDF[mot] * cptTF[mot], 2 )

        for mot, val in cptTF.items():
            dico_list['dico{}'.format(i + 1)][mot] = val

        cellule_matrice = []
        for mot, val in cptTF.items(): # Création de la prematrice TF IDF (nécessite une transposition)
            cellule_matrice.append(val)
        prematrice_TF_IDF.append(cellule_matrice)

    matrice_TF_IDF = Transposition(prematrice_TF_IDF) # Transposition en utilisant la fonction créée
    return (matrice_TF_IDF, dico_list)

# Fonction 'Transposition'
# Transpose la matrice retourné par la fonction 'TF_IDF'
# Retourne la matrice transposée
def Transposition(matrice): # Transposer une matrice nécessite nb ligne == nb colonne
    longeur_max = max(len(ligne) for ligne in matrice) # Longueur max des lignes + ajustement de la matrice
    matrice_ajustement = [ligne + [0] * (longeur_max - len(ligne)) for ligne in matrice]
    # Transpose la matrice
    transpo = [[matrice_ajustement[j][i] for j in range(len(matrice_ajustement))] for i in range(longeur_max)]
    return transpo

# Fonction 'clean_question'
# Réalise la tokenisation de la question posée par l'utilisateur
# Retourne la liste des mots nettoyés de la question posée par l'utilisateur
def clean_question(question):
    L = list(question)
    if L [-1] != " " :
        L.append(" ")
    Q=[]
    MOT = ""
    for lettre in L:
        l_ascii = ord(lettre)

        # Converti les majuscules en miniscules
        if l_ascii >= 65 and l_ascii <= 90:
            l_ascii += 32
            new_lettre = chr(l_ascii)
            MOT += new_lettre

        # Miniscules
        elif l_ascii >= 97 and l_ascii <= 122:
            MOT += lettre

        # Cas particulier (è ; é ; ê)
        elif l_ascii >= 232 and l_ascii <= 234:
            MOT += 'e'

        # Cas particulier (â ; à)
        elif l_ascii == 224 or l_ascii == 226:
            MOT += 'a'

        # Cas particulier (û ; ù)
        elif l_ascii == 251 or l_ascii == 249:
            MOT += 'u'

        # Cas particulier (ç)
        elif l_ascii == 231:
            MOT += 'c'

        # Cas particulier (" " ; "-")
        elif lettre == " " or lettre == "" or lettre == "-":
            Q.append(MOT)
            MOT = ""

        # Cas particulier ("ô")
        elif lettre == "ô":
            MOT += 'o'

        # Cas particulier ('œ')
        elif lettre == 'œ':
            MOT += "o"
            MOT += 'e'

        # Cas particulier ("'")
        elif lettre == "'":
            MOT += "e "

        # Ponctuations
        else:
            for ponct in ponctuation:
                if ponct == lettre:
                    MOT += ''
    return Q # Retourne la liste des mots de la question nettoyé

# Fonction 'comparaison_question'
# Recherche les mots de la question posée dans le corpus
# Retourne la liste des mots de la question posée présents dans le corpus
def comparaison_question(question): # recherche des mot de la question dans le corpus
    question_comparer = []
    corpus = []
    for nom in files_names:
        with open ('./cleaned/{}'.format(nom),'r') as f:
            doc = f.read()
            doc = doc.split()
            for mot in doc:
                corpus.append(mot)

    for mot in question : # Cherche les mots de la question dans le corpus et renvoi les mots trouvés
        if mot in corpus:
            question_comparer.append(mot)
    return question_comparer

# Fonction 'matrice_pour_comparaison'
# Retranspose la matrice pour une utilisation dans la fonction 'pertinence'
# Retourne la matrice TF-IDF retransposée
def matrice_pour_comparaison(matrice):
    nouvelle_matrice = Transposition(matrice)
    longeur_matrice = len(nouvelle_matrice[0])
    return nouvelle_matrice, longeur_matrice

# Fonction 'question_TF_IDF'
# Calcule le TF-IDF des mots de la question posée
# Retourne le score TF-IDF des mots de la question posée
def question_TF_IDF(question_comparer,longeur_new_matrice):
    IDF_corpus = IDF(files_names)
    TF_IDF_question = {}
    # TF de la question
    for mot in question_comparer:
        if mot not in TF_IDF_question:
            TF_IDF_question[mot] = 1
        elif mot in TF_IDF_question:
            TF_IDF_question[mot] += 1

    for mot in TF_IDF_question.keys(): # Calcule du TF-IDF
        TF_IDF_question[mot] = TF_IDF_question[mot] * IDF_corpus[mot]

    vecteur_TF_IDF = []

    for mot,val in TF_IDF_question.items(): # Le résultat dans une liste (M = le nombre de colonnes) de la matrice TF-IDF
        vecteur_TF_IDF.append(round(val,2))

    if len(vecteur_TF_IDF) < longeur_new_matrice:
        for w in range(longeur_new_matrice - len(vecteur_TF_IDF)):
            vecteur_TF_IDF.append(1)
    return vecteur_TF_IDF, TF_IDF_question

# Fonction 'produit_scalaire'
# Calcule le produit scalaire de deux vecteurs
# Retourne le produit scalaire des deux vecteurs
def produit_scalaire(A,B):
    somme_vecteur = 0
    for i in range(len(A)):
        somme_vecteur += A[i] * B[i]
    return somme_vecteur # Produit scalaire des deux vecteurs

# Fonction 'norme_vecteur'
# Calcule la norme vectorielle des vecteurs de la fonction 'produit_scalaire'
# Retourne la norme vectorielle
def norme_vecteur (A):
    somme = 0
    for i in range(len(A)):
        somme += A[i]**2
    norme = math.sqrt(somme)
    return norme # Norme des deux vecteurs

# Fonction 'similarite'
# Calcule la similarité entre les deux vecteurs
# Retourne la similarité
def similarite (A,B): #pareille
    simil = produit_scalaire(A, B) / norme_vecteur(A) * norme_vecteur(B)
    return simil # Similarité entre les deux vecteurs

# Fonction 'pertinence'
# Relèves les mots les plus pertinents par rapport à la question (Utilisateur)
# Retourne la liste des termes les plus pertinents
def pertinence(matrice,vecteur): # Utilisation de la fonction 'similarite' pour calculer le document le plus pertinent
    docu = 0
    sim = 0
    for i in range(nb_de_fichier):
        if sim < similarite(matrice[i], vecteur):
            sim = similarite(matrice[i], vecteur)
            docu = files_names[i]
    return sim, docu

# Fonction 'MAX_TF_IDF'
# Trouve le mot le plus important de la question (Utilisateur)
# Retourne le mot le plus important
def MAX_TF_IDF(TFIDF_dico):
    X = 0
    for mot, val in TFIDF_dico.items():
        if X <= val:
            X = val
            M = mot
    return M

# Fonction 'reponse'
# Identifie le terme interrogatif de la question (Utilisateur) et répond en conséquence
# Retourne la réponse adaptée à la question (Utilisateur)
def reponse (question,mot_importan_question,doc):
    # Liste de propositions non exhaustives
    start = 0
    fin_reponse = 0
    question_starters = {
        "comment" : "Après analyse, ",
        "Comment": "Après analyse, ",
        "pourquoi": "Car, ",
        "Pourquoi": "Car, ",
        "peux-tu": "Oui, bien sûr!",
        "Peux-tu": "Oui, bien sûr!"
    }
    mot = question_starters.keys()
    for i in mot:
        if i in question:
            start = question_starters[i]

    with open('./speeches/{}'.format(doc),encoding="utf8") as f:
        L = f.readlines()
        for ligne in L:
            if " {}".format(mot_importan_question) in str(ligne):
                fin_reponse = str(ligne)

    rep = ("{} {}".format(start, fin_reponse))
    return rep

# STOP