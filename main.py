from fonction import *
# Permet d'avoir la liste des fichiers
directory = "./speeches"
files_names = list_of_files(directory,'txt')

# Nettoyage des fichiers .txt
cleaned(files_names)

# méthode TF_IDF
TF_IDF(files_names)
IDF(files_names)