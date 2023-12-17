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
#__________________________________________________________Nettoyage__________________________________________________________
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

#__________________________________________________________Parti pour la création de la matrice TF-IDF__________________________________________________________
#TF
def TF(contenu):
    cptTF = {}
    liste_mots = contenu.split()
    for mot in liste_mots:
        if mot not in cptTF: # Calcul la fréquence TF de chaque mot
            cptTF[mot] = 1
        else:
            cptTF[mot] += 1
    return cptTF # Return la fréquence de chaque mot

#IDF
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
            for mot, val in precptIDF.items(): # Calcul l'IDF de chaque mot
                cptIDF[mot] = math.log((nb_de_fichier/val) + 1)
    return cptIDF

#TF-IDF
def TF_IDF(files_name):
    cptIDF = IDF(files_name)
    prematrice_TF_IDF = []
    for i in range (len(files_name)):
        with open('./cleaned/{}'.format(files_name[i]), 'r', encoding="utf-8") as f:
            contenu = f.read()
            cptTF = TF(contenu)

            for mot in cptTF.keys(): # Calcul de TF_IDF pour chaque mot
                cptTF[mot] = round(cptIDF[mot] * cptTF[mot], 2 )

        for mot, val in cptTF.items():
            dico_list['dico{}'.format(i + 1)][mot] = val

        cellule_matrice = []
        for mot, val in cptTF.items(): # Création de la prematrice TF IDF (nécessite une transposition)
            cellule_matrice.append(val) # (perso) uniquement val
        prematrice_TF_IDF.append(cellule_matrice)

    matrice_TF_IDF = Transposition(prematrice_TF_IDF) # Transpose en utilisant la fonction créée
    return (matrice_TF_IDF, dico_list)

#Transposition Matrice
def Transposition(matrice): # Pour transposer une matrice nécessite nb ligne == nb colonne
    longeur_max = max(len(ligne) for ligne in matrice) # Longueur max des lignes + ajustement de la matrice
    matrice_ajustement = [ligne + [''] * (longeur_max - len(ligne)) for ligne in matrice]
    # Transpose la matrice
    transpo = [[matrice_ajustement[j][i] for j in range(len(matrice_ajustement))] for i in range(longeur_max)]
    return transpo

#__________________________________________________________Generation de la question__________________________________________________________

# Nous donne la question netoyer et nous renvoie la liste de mot qu'elle compose
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
    return Q # Return la liste des mots de la question nettoy

# recherche des mot de la question dans le corpus
def comparaison_question(question): # recherche des mot de la question dans le corpus
    question_comparer = []
    corpus = [] # pour avoir tout le corpus
    for nom in files_names:
        with open ('./cleaned/{}'.format(nom),'r') as f:
            doc = f.read()
            doc = doc.split()
            for mot in doc:
                corpus.append(mot)

    for mot in question : # chercher les mot de la question dans le corpuse et ressort les mot trouver
        if mot in corpus:
            question_comparer.append(mot)
    return question_comparer

def matrice_pour_comparaison(matrice):
    new_matrice = Transposition(matrice)
    longeur_matrice = len(new_matrice[0])
    return new_matrice, longeur_matrice

def question_TF_IDF(question_comparer,longeur_new_matrice):
    # parti pour le TF de la question
    IDF_corpus = IDF(files_names)
    TF_IDF_question = {}
    for mot in question_comparer:
        if mot not in TF_IDF_question:
            TF_IDF_question[mot] = 1
        elif mot in TF_IDF_question:
            TF_IDF_question[mot] += 1

    for mot in TF_IDF_question.keys(): # calcule TF IDF
        TF_IDF_question[mot] = TF_IDF_question[mot] * IDF_corpus[mot]

    vecteur_TF_IDF = []
    cellule_vecteur = []

    for mot,val in TF_IDF_question.items(): # met le calcule dans une liste en respectant le M = 8 = le nombre de col de la matrice TF IDF = le nb de document
        cellule_vecteur.append(val) # (perso) uniquement val
        if len(cellule_vecteur) == nb_de_fichier:
            vecteur_TF_IDF.append(cellule_vecteur)
            cellule_vecteur = []
    vecteur_TF_IDF.append(cellule_vecteur)

    # (perso) si besoin faire une verification par ligne des longeur pour etre acorder au nb colonne
    return vecteur_TF_IDF

def produit_scalaire(A,B):
    somme_vecteur = 0
    for i, j in range (len(A),len(B)):
        somme_vecteur += A[i] * B[j]
    return somme_vecteur

def norme_vecteur (A):
    somme = 0
    for i in range(len(A)):
        somme += A[i]**2
    norme = math.sqrt(somme)
    return norme

def similarite (A,B):
    sim = produit_scalaire(A,B)/norme_vecteur(A)*norme_vecteur(B)
    return sim
