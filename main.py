from fonction import *
# Permet d'avoir la liste des fichiers
directory = "./speeches"
files_names = list_of_files(directory,'txt')

# Nettoyage des .txt
cleaned(files_names)
# Matrice
matrice_TF_IDF, dico_list = TF_IDF(files_names)

# Menu d'accès aux fonctionnalités
x = 0
print("1 - clean files \n"
      "2 - TF Term Frequency \n"
      "3 - IDF Inverse Document frequency \n"
      "4 - Matrice TF-IDF \n")
while x <= 0 or x > 4:
      x = int(input("Enter the desired functionality number: "))
      if x <= 0 or x > 4:
            print("This functionality does not exist.")

# Nettoyage des .txt
if x == 1:
      cleaned(files_names)
      print("Files has been cleaned")

# Accès au TF des .txt
elif x == 2:
      print("Dictionary 1: Chirac #1 \n"
            "Dictionary 2: Chirac #2 \n"
            "Dictionary 3: Giscard d'Estaing \n"
            "Dictionary 4: Hollande \n"
            "Dictionary 5: Macron \n"
            "Dictionary 6: Mitterand #1 \n"
            "Dictionary 7: Mitterand #2 \n"
            "Dictionary 8: Sarkozy \n")
      d = 0
      while d <= 0 or x > 8:
            d = int(input("Enter the desired dictionary: "))
            if d <= 0 or x > 8:
                  print("This dictionary does not exist")
            if d == 1:
                  print(Chirac1)
            elif d == 2:
                  print(Chirac2)
            elif d == 3:
                  print(Giscard_dEstaing)
            elif d == 4:
                  print(Hollande)
            elif d == 5:
                  print(Macron)
            elif d == 6:
                  print(Mitterrand)
            elif d == 7:
                  print(Mitterrand2)
            elif d == 8:
                  print(Sarkozy)

# Accès à l'IDF des .txt
elif x == 3:
    IDF = IDF(files_names)
    for motidf, validf in IDF.items():
        print("mot : {} \n score IDF : {} \n ".format(motidf,validf))

# Accès à la Matrice TF-IDF
elif x == 4:
    for ligne in matrice_TF_IDF:
        print(ligne)