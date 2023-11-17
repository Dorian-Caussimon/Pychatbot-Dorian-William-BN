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
            Z.append(val)
            print(Z,end='')

# vérification des caractèr
            for val in Z:
                print(val)
                caract = ord(val)
                if caract <= 90 and caract >= 65:
                    caract =+ 32
                    caract = chr(caract)
                    with open('./clened/{}'.format(vil), 'w', encoding="utf-8") as f1:
                        f1.write(caract)