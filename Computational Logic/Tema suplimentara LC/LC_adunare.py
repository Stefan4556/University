"""
    Modulul LC_adunare se ocupa cu retinerea a 3 functii:
    1 - spargere numar
    2 - rezolva adunare
    3 - adunare
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

def rezolva_adunare(a,b,baza):
    """
        Rolul acestei functii este de a rezolva adunarea propriu zisa, programul primeste 2 string-uri dupa care
        le converteste in 2 liste dupa care realizeaza adunarea
    """

    lista_a = spargere_numar(a)
    lista_b = spargere_numar(b)

    lung_a = len(lista_a)
    lung_b = len(lista_b)

    # pentru a evita eroarea IndexError daca o lista are mai putine elemente, trebuie sa adaugam zero-uri pe primele
    # pozitii pana cand ajung sa aiba aceeasi lungime
    if(lung_a < lung_b):
        for i in range(lung_a,lung_b):
            lista_a.insert(0,0)
    elif lung_a > lung_b:
        for i in range(lung_b,lung_a):
            lista_b.insert(0,0)

    rezultat = []

    transport = 0

    # realizam adunarea celor 2 liste, avand grija la transport in cazul in care suma a 2 elemente din lista depasesc baza
    # in care este realizata adunarea 
    for i in range(len(lista_a) - 1,-1,-1):
        suma = lista_a[i] + lista_b[i] + transport
        if suma >= baza:
            rezultat.append(suma - baza)
            transport = 1
        else:
            rezultat.append(suma)
            transport = 0
    if transport == 1:
        rezultat.append(1)
    
    rezultat = list(reversed(rezultat))

    print("Rezultatul adunarii dintre",a,"si",b,"in baza",baza,"este: ",end="")
    # afisam rezultatul adunarii celor 2 numere
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
    s = ""
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

def adunare():
    """
        Aceasta este functia ce are rolul de a citi si a apela adunarea a 2 numere intr-o baza data de catre utilizator,
        functie ce este apelata in sub-meniul 1, cel corespunzator operatiilor
    """
    
    baza = int(input("Introduceti baza in care o sa se realizeze adunarea: "))
    a = input("Introduceti primul numar: " )
    b = input("Intoruceti al doilea numar: ")
    rezolva_adunare(a,b,baza)
    print("")
    print("")
