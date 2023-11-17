import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def cleaned (files_names):
    for val in files_names:
        F=[]
        F1 = []
        with open('./speeches/{}'.format(val), 'r', encoding="utf-8") as f1:
            F = str(f1.readlines())
            F1 = [x.replace('\n','') for x in F]
            print F1
# division des mot en caractère
        for val in F:
            Z = []
            Z.append(val)
# vérification des caractèr

