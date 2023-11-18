import os
#
# Liste pour les ponctuation
ponctuation = ["," , "." , "!" , ":" , "?", ";"]

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def cleaned (files_names):
    for nom in files_names:
        # ouvre le ficher texte a nétoyer
        with open('./speeches/{}'.format(nom), 'r', encoding="utf-8") as f1:
            F = f1.readlines()

            # crée le nouveaux ficher pour le texte netoyer
            with open('./cleaned/{}'.format(nom), 'w', encoding="utf-8") as f2:

                # divise les txt en ligne
                for ligne in F:

                    # divise les ligne en lettre
                    for lettre in ligne:
                        l_ascii = ord(lettre)

                        # majuscule --> minuscule
                        if l_ascii >= 65 and l_ascii <= 90:
                            l_ascii += 32
                            new_lettre = chr(l_ascii)
                            f2.write(new_lettre)
                        # pour les minuscule
                        elif l_ascii >=97 and l_ascii <= 122:
                            f2.write(lettre)
                        # cas particuler pour les è ; é ; ê
                        elif l_ascii >= 232 and l_ascii <= 234:
                            f2.write('e')

                        # cas particulier â et à
                        elif l_ascii == 224 or l_ascii == 226:
                            f2.write('a')

                        # cas particulier û et ù
                        elif l_ascii == 251 or l_ascii == 249:
                            f2.write('u')

                        # pour les espace tiret et apostroph
                        elif lettre == " " or lettre == "-" or lettre == "'" :
                            f2.write(" ")
                        # pour la pnctuation
                        else:
                            for ponct in ponctuation:
                                if ponct == lettre:
                                    f2.write('')
                    f2.write("\n")