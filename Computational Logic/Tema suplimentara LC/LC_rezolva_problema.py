"""
    Acest modul se ocupa cu rezolvarea urmatorului enunt:
    Se dau 2 numere, unul intr-o baza oarecare si unul intr-o baza putere a lui 2
    Sa se realizeze adunarea acestora in baza 2 si conversia rezultatului adunarii in baza 10
    
    Aceasta problema foloseste 3 modalitati de conversie:
        1) Conversia rapida - pentru al 2 lea numar
        2) Conversia prin substitutie - pentru rezultatul final
        3) Conversia folosind baza intermediara - pentru a converti primul numar
"""

from LC_conversie_baza_intermediara import rezolva_conversie_baza_intermediara
from LC_conversie_substitutie import rezolva_conversie_substitutie
from LC_conversii_rapide import rezolva_conversie_rapida

from LC_adunare import rezolva_adunare

def rezolva_problema():
    """
        Aceasta functie rezolva problema
    """

    print("Sa se citeasca pe rand baza primului numar, primul numar, baza celui de al 2 lea numar, o baza putere a lui 2 si al 2 lea numar")
    print("Problema realizeaza pe rand conversia celor 2 numere in baza 2 dupa care efectueaza adunarea acestora in baza 2 si converteste rezultatul in baza 10")
    print("")

    # primul pas: citim cele bazele si valorile celor 2 numere
    baza_a = int(input("Introduceti baza primului numar: "))
    a = input("Introduceti primul numar: ")
    baza_b = int(input("Introduceti baza celui de al doilea numar, putere a lui 2: "))
    b = input("Introduceti al doilea numar: ")

    print("Rezolvarea este:")

    # convertim primul numar in baza 2 folosind conversia prin conversia cu baza intermediara
    print("1) Convertim primul numar in baza 2:")
    a = rezolva_conversie_baza_intermediara(baza_a,a,2)
    print("")

    # convertim al doilea numarul folosind conversia rapida
    print("2) Convertim al 2-lea numar in baza 2: ")
    b = rezolva_conversie_rapida(baza_b,b,2)

    # realizam adunarea celor 2 numere in baza 2
    print("3) Realizam adunarea celor 2 numere: ")
    s = rezolva_adunare(a,b,2)
    print("")

    # realizam conversia numarului din baza 2 in baza 10 folosind metoda substitutiei
    print("4) Realizam ultima conversie din baza 2 in baza 10 a rezultatului adunarii celor 2 numere: ")
    s = rezolva_conversie_substitutie(2,s)

    print("Rezultatul final este:",s)



