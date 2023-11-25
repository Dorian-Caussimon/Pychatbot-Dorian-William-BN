from fonction import *
# Permet d'avoir la liste des fichiers
directory = "./speeches"
files_names = list_of_files(directory,'txt')

# Nettoyage des fichiers .txt
cleaned(files_names)

# TF-IDF
TF_IDF(files_names)

# Utiliser "print(Nom_président)"
print(Chirac1)