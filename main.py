from fonction import *
# permet d'avoir la liste des fichier
directory = "./speeches"
files_names = list_of_files(directory, "txt")

#netoyage
cleen(files_names)
