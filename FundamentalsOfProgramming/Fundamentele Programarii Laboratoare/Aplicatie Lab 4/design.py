"""
    Rolul acestui modul este de a stoca functiile ce tiparesc meniurile functiilor din program
"""

def design_meniu():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul principal
    """
    print("             Meniu")
    print("")
    print("1) Adauga numar in lista")
    print("2) Modifica elemente din lista")
    print("3) Cautare numere")
    print("4) Operatii cu numerele din lista")
    print("5) Filtrare")
    print("6) Undo")
    print("7) Afisare lista")
    print("8) Exit")

def design_functie_1():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 1
    """
    print("1) Adauga un numar complex la sfarsitul listei")
    print("2) Insereaza un numar complex pe o pozitie data")
    print("3) Inapoi")

def design_functie_2():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 2
    """
    print("1) Sterge elementul de pe o pozitie citita")
    print("2) Sterge elementele de pe un interval de pozitii")
    print("3) Inlocuieste toate aparitiile unui numar cu alt numar")
    print("4) Inapoi")

def design_functie_3():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 3
    """
    print("1) Tipareste partea iamginara pentru numerele din interval")
    print("2) Tipareste toate numerele complexe ce au modulul mai mic decat 10")
    print("3) Tipareste toate numerele complexe ce au modulul egal cu 10")
    print("4) Inapoi")

def design_functie_4():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 4
    """
    print("1) Afiseaza suma numerelor dintr-o subsecventa data")
    print("2) Produsul numerelor dintr-o subsecventa data")
    print("3) Tipareste lista sortata descrescator dupa partea imaginara")
    print("4) Inapoi")

def design_functie_5_2(numar):
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 2 din functia 5
    """
    print("1) Elimina numerele complexe care au modulul mai mic decat ",numar)
    print("2) Elimina numerele complexe care au modulul egal cu ",numar)
    print("3) Elimina numerele complexe care au modulul mai mare decat ",numar)
    print("4) Inapoi")

def design_functie_5():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 5
    """
    print("1) Elimina din lista numerele complexe a caror parte reala este un numar prim")
    print("2) Elimina din lista numerele complexe al caror modul este mai mic / egal / mare decat un numar citit")
    print("3) Inapoi")