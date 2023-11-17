import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def cleen (files_names):
    for val in files_names:
        F=[]
        with open('./speeches/{}'.format(val), 'r', encoding="utf-8") as f1:
            F = str(f1.readlines())
# Division des mots en caractères
        for val in F:
            Z = []
            Z.append(val)
            print(Z,end='')

# Vérification des caractères