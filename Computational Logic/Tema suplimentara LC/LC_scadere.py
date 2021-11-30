"""
    Modulul LC_scadere se ocupa cu retinerea a 3 functii:
    1 - spargere numar
    2 - rezolva scadere
    3 - scadere
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

def rezolva_scadere(a,b,baza):
    """
        Rolul acestei functii este de a rezolva scaderea propriu zisa, programul primeste 2 string-uri dupa care
        le converteste in 2 liste dupa care realizeaza scaderea
    """

    lista_a = spargere_numar(a)
    lista_b = spargere_numar(b)

    lung_a = len(lista_a)
    lung_b = len(lista_b)

    ok_minus = 0

    # pentru a evita eroarea IndexError daca o lista are mai putine elemente, trebuie sa adaugam zero-uri pe primele
    # pozitii pana cand ajung sa aiba aceeasi lungime
    if lung_a <= lung_b:
        ok_minus = 1
        lista_a,lista_b = lista_b,lista_a
        for i in range(lung_a,lung_b):
            lista_b.insert(0,0)
        if lista_a == lista_b:
            ok_minus = 0
    elif lung_a > lung_b:
        ok_minus = 0
        for i in range(lung_b,lung_a):
            lista_b.insert(0,0)

    rezultat = []

    ok = 1

    transport = 0
    # realizam scaderea celor 2 liste, avand grija la transport in cazul in care diferenta a 2 elemente e mai mica decat 0 
    # se adauga baza destinatie si transportul devine -1 pentru ca ne-am imprumutat
    for i in range(len(lista_a)-1,-1,-1):
        diferenta = lista_a[i] - lista_b[i] - transport
        if diferenta < 0:
            rezultat.append(diferenta + baza)
            transport = 1
        else:
            rezultat.append(diferenta)
            transport = 0
        if diferenta != 0:
            ok = 0
    
    rezultat = list(reversed(rezultat))

    if ok == 0:

        i = 0
        while i < len(rezultat): 
            if rezultat[i] == 0:
                rezultat.pop(i)
                i -= 1
            else:
                break
            i += 1

    ok_verifica_cifre_zero = 0
    for i in range(0,len(rezultat)):
        if rezultat[i] != 0:
            ok_verifica_cifre_zero = 1
            break
    
    if ok_verifica_cifre_zero == 0:
        for i in range(len(rezultat) - 1,0,-1):
            rezultat.pop(i)
        rezultat[0] = 0

    if ok_minus == 1:
        print("Rezultatul scaderii dintre",a,"si",b,"in baza",baza,"este: -",end="")
        s = "-"

    else:
        print("Rezultatul scaderii dintre",a,"si",b,"in baza",baza,"este: ",end="")
        s = ""

    # afisam rezultatul scaderii celor 2 numere
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
    for i in range(0,len(rezultat)):
        if rezultat[i] <= 9:
            s += str(rezultat[i])
        elif rezultat[i] == 10:
            s += str("A")
        elif rezultat[i] == 11:
            s += str("B")
        elif rezultat[i] == 12:
            s += str("C")
        elif rezultat[i] == 13:
            s += str("D")
        elif rezultat[i] == 14:
            s += str("E")
        elif rezultat[i] == 15:
            s += str("F")

    return s

def scadere():
    """
        Aceasta este functia ce are rolul de a citi si a apela scaderea a 2 numere intr-o baza data de catre utilizator,
        functie ce este apelata in sub-meniul 1, cel corespunzator operatiilor
    """

    baza = int(input("Introduceti baza in care o sa se realizeze scaderea: "))
    a = input("Introduceti primul numar: " )
    b = input("Intoruceti al doilea numar: ")
    rezolva_scadere(a,b,baza)
    print("")
    print("")
