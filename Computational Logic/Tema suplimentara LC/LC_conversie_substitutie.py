"""
    Modulul LC_conversie_substitutie se ocupa cu retinerea a 3 functii:
    1 - spargere numar
    2 - rezolva conversie substitutie
    3 - conversie substitutie
"""

def spargere_numar(number):
    """
        Rolul acestei functii este de a converti un string cu numere si litere intr-o lista cu valorile ce 
        ii corespund acelui caracter, ca de ex:
        'A10' in hexazecimal => lista = [10,1,0]
    """
    
    delta = 87 
    number = list(str(number))
    for i in range(len(number)):
        if number[i].isnumeric() == False:
            number[i] = number[i].lower()
            number[i] = int(ord(number[i]) - delta)
        number[i] = int(number[i])

    return list(number)

def rezolva_conversie_substitutie(baza,nr):
    """
        Metoda conversiei prin substitutie consta intr-o formula: fie un numar c1c2c3 in baza c
        numarul in baza 10 este egal cu c3 * c^0 + c2 * c^1 + c1 * c^2 si tot asa se poate generaliza formula, aceasta este pentru un numar cu 3 cifre
    """

    lista_nr = spargere_numar(nr)
    putere = 1
    rezultat = 0
    # calculam rezultatul final in baza 10
    for i in range(len(lista_nr)-1,-1,-1):
        rezultat += lista_nr[i]*putere
        putere *= baza
    
    print("Rezultatul conversiei prin substitutie a numarului",nr,"din baza",baza,"in baza 10 este",rezultat)

    # dam return la string pentru a putea folosi rezultatul in viitoarele calcule, in cazul in care avem nevoie
    s = str(rezultat)
    return s

def conversie_substitutie():
    """
        Aceasta este functia cu rolul de a citi si apela conversia prin substitutie a unui numar primit intr-o baza n data de catre utilizator,
        totodata functia este apelata in sub-meniul 2, cel corespunzator conversiilor
    """

    baza = int(input("Introduceti baza numarului ce urmeaza sa fie citit: "))
    nr = input("Introduceti numarul: ")
    rezolva_conversie_substitutie(baza,nr)
    print("")
    print("")

