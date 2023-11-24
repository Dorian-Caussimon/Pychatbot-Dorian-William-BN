import os
# Liste des ponctuations
ponctuation = ["," , "." , "!" , ":" , "?", ";"]

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
#TF
def TF (files_names):
    for nom in files_names:
        # Ouvre le fichier "cleaned" pour le calcul du TF
        with open('./cleaned/{}'.format(nom), 'r', encoding="utf-8") as f:
            contenu = f.read()

            # Compte la fréquence de chaque mot
            cptTF = {}
            mots = contenu.split()
            for mot in mots:
                if mot not in cptTF:
                    cptTF[mot] = 1
                else:
                    cptTF[mot] += 1

            # Calcule le TF pour chaque mot
            motTot = len(mots)
            tf = {}
            for mot, cpt in cptTF.items():
                tf[mot] = (cpt / motTot)

            # Affiche les résultats du TF
            print("TF du fichier {} :".format(nom))
            for mot, tf_val in tf.items():
                print("{}: {}".format(mot, tf_val))
            print("\n")