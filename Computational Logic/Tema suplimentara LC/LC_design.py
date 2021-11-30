"""
    Modulul LC_design se ocupa cu retinerea celor 3 meniuri:
    1 -  meniul principal
    2 - meniul operatiilor
    3 - meniul conversiilor
"""

def design_meniu_operatii():
    """
        Design-ul meniului ce cuprinde toate operatiile ce pot fi realizate intre doua numere
    """
    
    print("                 Meniu operatii cu numere")
    print("")
    print("1) Adunati doua numere intr-o baza data")
    print("2) Scadeti doua numere intr-o baza data")
    print("3) Inmultiti un numar intr-o baza data cu o cifra")
    print("4) Impartiti un numar intr-o baza data cu o cifra")
    print("5) Back") 
    print("")

def design_meniu_conversii():
    """
        Design-ul meniului ce cuprinde toate modalitatile de convertire a unui numar dintr-o baza in alta
    """

    print("                 Meniu conversii de numere")
    print("")
    print("1) Conversia unui numar dintr-o baza in alta prin impartiri succesive")
    print("2) Conversia unui numar dintr-o baza in baza 10 prin substitutie")
    print("3) Conversia unui numar prin utilizarea unei baze intermediare")
    print("4) Conversia unui numar cu ajutorul conversiilor rapide")
    print("5) Back")
    print("")

def design_meniu():
    """
        Design-ul meniului principal ce reuneste optiunile pe care utilizatorul le are in meniul principal
    """

    print("                 Meniu principal")
    print("")
    print("1) Operatii cu numere")
    print("2) Conversii de numere")
    print("3) Rezolva problema")
    print("4) Exit")
    print("")