import os
import math
# Liste des ponctuations
ponctuation = [",", ".", "!", ":", "?", ";"]

Chirac1 = {}
Chirac2 = {}
Giscard_dEstaing = {}
Holland = {}
Macron = {}
Mitterrand = {}
Mitterrand2 = {}
Sarkozy = {}
dico_list = {'dico1': Chirac1,
             'dico2': Chirac2,
             'dico3': Giscard_dEstaing,
             'dico4': Holland,
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

def TF(chaine_de_caractere):
    cptTF = {}
    liste_mots = chaine_de_caractere.split()
    for mot in liste_mots:
        if mot not in cptTF:
            cptTF[mot] = 1
        else:
            cptTF[mot] += 1
    return cptTF
def IDF(files_names):
    cptIDF = {}
    for val in files_names:
        with open('./cleaned/{}'.format(val), 'r', encoding="utf-8") as f:
            contenu = f.read()
            cptTF = TF(contenu)
            for mot, val in cptTF.items():
                cptIDF[mot] = math.log(1/val)
    return print (cptIDF)



def TF_IDF (files_names):
    for i in range(len(files_names)):

        # Ouvre le fichier "cleaned" pour le calcul du TF
        with open('./cleaned/{}'.format(files_names[i]), 'r', encoding="utf-8") as f:
            contenu = f.read()
            # Compte la fréquence de chaque mot
            cptTF = {}
            liste_mots = contenu.split()
            for mot in liste_mots:
                if mot not in cptTF:
                    cptTF[mot] = 1
                else:
                    cptTF[mot] += 1

            # ouverture du dico pour ranger les valeur TF trouver
            for mot, val in cptTF.items():
                dico_list['dico{}'.format(i+1)][mot] = val
    return
