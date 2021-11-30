"""
    Modulul LC_conversie_impartiri se ocupa cu retinerea a 4 functii:
    1 - spargere numar
    2 - converteste_litere_valoare
    3 - rezolva_conversie_impartire
    4 - conversie impartiri
"""

from LC_impartire import rezolva_impartire

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

def converteste_litera_valoare(litera):
    """
        Aceasta functie converteste un string format dintr-o cifra intr-o baza de numeratie pana la baza 16, in cifra corespunzatoare
        bazei respective (ex: B este 11 in orice baza >= 12)
    """

    if litera.isnumeric() == True:
        return int(litera)
    elif litera == "A":
        return 10
    elif litera == "B":
        return 11
    elif litera == "C":
        return 12
    elif litera == "D":
        return 13
    elif litera == "E":
        return 14
    elif litera == "F":
        return 15

def rezolva_conversie_impartiri(baza1,nr,baza2):
    """
        Metoda conversiei prin impartiri consta in mai multe impartiri repetate pana cand catul ajunge 0, moment in
        care rezultatul este format din toate resturile luate de la cap la coada
    """

    c = "1"
    r = "1"
    # convertim a 2 a baza pentru a putea folosi functia ce realizeaza impartirea unui numar cu altul
    if baza2 == 10:
        baza2 = "A"
    elif baza2 == 11:
        baza2 = "B"
    elif baza2 == 12:
        baza2 = "C"
    elif baza2 == 13:
        baza2 = "D"
    elif baza2 == 14:
        baza2 = "E"
    elif baza2 == 15:
        baza2 ="F"
    rezultat = []

    # formam numarul din resturile impartirilor 
    while nr != "0":
        c,r = rezolva_impartire(nr,baza2,baza1)
        r = converteste_litera_valoare(r)
        rezultat.append(r)
        nr = c
    
    # intoarcem lista deoarece resturile erau puse in ordine inversa
    rezultat = list(reversed(rezultat))

    # pregatim numarul sub forma de string pentru a il putea folosi in problemele viitoare
    s = ""
    for i in range(0,len(rezultat)):
        if int(rezultat[i]) <= 9:
            s += str(rezultat[i])
        elif int(rezultat[i]) == 10:
            s += str("A")
        elif int(rezultat[i]) == 11:
            s += str("B")
        elif int(rezultat[i]) == 12:
            s += str("C")
        elif int(rezultat[i]) == 13:
            s += str("D")
        elif int(rezultat[i]) == 14:
            s += str("E")
        elif int(rezultat[i]) == 15:
            s += str("F")
    return s

def conversie_impartiri():
    """
        Aceasta functie are rolul de a citi, apela si afisa rezultatul conversiei prin impartiri repetate a unui numar 
        dintr-o baza in alta baza. Totodata functia este apelata in sub-meniul 2, cel corespunzator conversiilor 
    """

    baza1 = int(input("Introduceti baza numarului pe care doriti sa-l transformati: "))
    nr = input("Introduceti numarul: ")
    baza2 = int(input("Introduceti baza in care doriti sa fie transformat numarul: "))
    s = rezolva_conversie_impartiri(baza1,nr,baza2)
    print("Rezultatul final este:",s)
    print("")
    print("")