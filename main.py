from fonction import *
# permet d'avoir la liste des fichier
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

#netoyage
for val in files_names:
    with open ('./speeches/{}'.format(val),'r',encoding="utf-8" ) as f1:
        F  = str(f1.readlines())
