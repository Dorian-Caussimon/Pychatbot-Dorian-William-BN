import os
ponctuation = [',','.','!','?']
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def cleaned (files_names):
    for val in files_names:
        F=[]
        with open('./speeches/{}'.format(val), 'r', encoding="utf-8") as f1:
            F = str(f1.readlines())
# division des mot en caractère
        for val in F:
            Z = []
            Z.append(val)
            for val in Z:
                caractere_ascii = ord(val)
                #majuscule --> minuscule
                if caractere_ascii >= 65 and caractere_ascii <=90:
                    caractere_ascii += 32
                    caractere = chr(caractere_ascii)