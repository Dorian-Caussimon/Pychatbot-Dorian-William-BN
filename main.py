from fonction import *
# Permet d'avoir la liste des fichiers
directory = "./speeches"
files_names = list_of_files(directory,'txt')

# Nettoyage des fichiers .txt
cleaned(files_names)

# Recherche de la fréquence de chaque mot dans le .txt
TF(files_names)