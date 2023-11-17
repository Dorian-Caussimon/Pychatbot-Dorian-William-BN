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
# division des mot en caractère
        for val in F:
            Z = []
            v = list(val)
            Z.append(v)
# vérification des caractère
            for val in Z:
                caract = ord(val)
                if caract <= 90 and caract >= 65:
