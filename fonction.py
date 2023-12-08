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

#Clean
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

                        # Ponctuations
                        else:
                            for ponct in ponctuation:
                                if ponct == lettre:
                                    f2.write('')
                    f2.write("\n")
    return

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
                cptIDF[mot] = math.log((8/val) + 1)
    return cptIDF

#TF-IDF
def TF_IDF(files_name):
    cptIDF = IDF(files_name)
    prematrice_TF_IDF = []
    for i in range (len(files_name)):
        with open('./cleaned/{}'.format(files_name[i]), 'r', encoding="utf-8") as f:
            contenu = f.read()
            cptTF = TF(contenu)

            for mot, val in cptTF.items(): # Calcul de TF_IDF pour chaque mot
                cptTF[mot] = math.floor(cptIDF[mot] * cptTF[mot])

        for mot, val in cptTF.items():
            dico_list['dico{}'.format(i + 1)][mot] = val

        cellule_matrice = []
        for mot, val in cptTF.items(): # Création de la prematrice TF IDF (nécessite une transposition)
            cellule_matrice.append(mot + " : " + str(val))
        prematrice_TF_IDF.append(cellule_matrice)

    matrice_TF_IDF = Transposition(prematrice_TF_IDF) # Transpose en utilisant la fonction créée
    return (matrice_TF_IDF, dico_list)

#Transposition Matrice
def Transposition(matrice): # Pour transposer une matrice nécessite nb ligne == nb colonne
    longeur_max = max(len(ligne) for ligne in matrice) # Longueur max des lignes + ajustement de la matrice
    matrice_d_ajustement = [ligne + [''] * (longeur_max - len(ligne)) for ligne in matrice]
    # Transpose la matrice
    transpo = [[matrice_d_ajustement[j][i] for j in range(len(matrice_d_ajustement))] for i in range (longeur_max)]
    return transpo

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

        # Cas particulier  (è ; é ; ê)
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

        # Cas particulier (" ")
        elif lettre == " " or lettre == "":
            Q.append(MOT)
            MOT = ""

        # Cas particulier ("'")
        elif lettre == "'":
            MOT += "e "

        # Ponctuations
        else:
            for ponct in ponctuation:
                if ponct == lettre:
                    MOT += ''

    # supprimer les doublon
    Q = set(Q)
    Q = list(Q)
    return Q
