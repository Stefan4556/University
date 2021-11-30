"""
    Modulul LC_impartire se ocupa cu retinerea a 3 functii:
    1 - spargere numar
    2 - converteste_valoare_litera
    3 - rezolva impartire
    4 - impartire
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

def converteste_valoare_litera(rest):
    """
        Aceasta functie converteste un string format dintr-o cifra intr-o baza pana la baza 16 in litera corespunzatoare
        de exemplu daca valoarea este 10, acestei valori ii este corespunzatoare litera A in orice baza >= 11
    """
    
    if rest < 10:
        r = str(rest)
    elif rest == 10:
        r = "A"
    elif rest == 11:
        r = "B"
    elif rest == 12:
        r = "C"
    elif rest == 13:
        r = "D"
    elif rest == 14:
        r = "E"
    elif rest == 15:
        r = "F"
    
    return r

def rezolva_impartire(a,b,baza):
    """
        Rolul acestei functii este de a rezolva impartirea propriu zisa, programul primeste 2 string-uri dupa care
        le converteste in 2 liste, a 2 a lista avand un singur element, dupa care se realizeaza impartirea
    """

    lista_a = spargere_numar(a)
    bb = spargere_numar(b)

    rest = 0
    rezultat = []

    # realizam impartirea listei cu cifra pe care o primeste avand grija sa retinem caturile corect si ultimul rest
    for i in range(0,len(lista_a)):
        imp = rest * baza + lista_a[i]
        cat = imp // bb[0]
        rezultat.append(cat)
        rest = imp % bb[0]
    
    while len(rezultat) > 0 and rezultat[0] == 0:
        rezultat.pop(0)
    
    if len(rezultat) == 0:
        rezultat.append(0)

    print("Rezultatul impartirii dintre",a,"si",b,"in baza",baza,"este: cat = ",end="")

    # afisam rezultatul impartirii
    for i in range(0,len(rezultat)):
        if rezultat[i]<=9:
            print(rezultat[i],end="")
        elif rezultat[i] == 10:
            print("A",end="")
        elif rezultat[i] == 11:
            print("B",end="")
        elif rezultat[i] == 12:
            print("C",end="")
        elif rezultat[i] == 13:
            print("D",end="")
        elif rezultat[i] == 14:
            print("E",end="")
        elif rezultat[i] == 15:
            print("F",end="")

    # cu ajutorul urmatoarelor randuri returnam rezultatul sub forma de string pentru a ne fi mai usor sa-l folosim in 
    # viitoarele calcule, daca avem nevoie de rezultat bineinteles 
    c=""
    for i in range(0,len(rezultat)):
        if rezultat[i] < 10:
            c += str(rezultat[i])
        elif rezultat[i] == 10:
            c += str("A")
        elif rezultat[i] == 11:
            c += str("B")
        elif rezultat[i] == 12:
            c += str("C")
        elif rezultat[i] == 13:
            c += str("D")
        elif rezultat[i] == 14:
            c += str("E")
        elif rezultat[i] == 15:
            c += str("F")   

    r = converteste_valoare_litera(rest)

    print(" si rest =",r)

    return c,r


def impartire():
    """
        Aceasta este functia ce are rolul de a citi si a apela impartirea unui numar cu o cifra intr-o baza data de catre utilizator
        functie ce e apelata in sub-meniul 1, cel corespunzator operatiilor
    """

    baza = int(input("Introduceti baza in care o sa se realizeze impartirea: "))
    a = input("Introduceti primul numar: " )
    b = input("Intoruceti al doilea numar: ")
    rezolva_impartire(a,b,baza)
    print("")
    print("")