"""
    Modulul LC_inmultire se ocupa cu retinerea a 3 functii:
    1 - spargere numar
    2 - rezolva inmultire
    3 - inmultire
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

def rezolva_inmultire(a,b,baza):
    """
        Rolul acestei functii este de a rezolva scaderea propriu zisa, programul primeste 2 string-uri dupa care
        le converteste in 2 liste dupa care realizeaza scaderea
    """

    lista_a = spargere_numar(a)
    bb = spargere_numar(b)
    transport = 0
    lista = []
    
    # realizam inmultirea listei cu cifra pe care o primeste avand grija la transport sa nu il uitam
    for i in range(len(lista_a)-1,-1,-1):
        prod = lista_a[i] * bb[0] + transport
        if prod >= baza:
            lista.append(prod % baza)
            transport = prod // baza
        else:
            lista.append(prod)
            transport = 0
    
    if transport != 0:
        lista.append(transport)
    
    lista = list(reversed(lista))

    print("Rezultatul inmultirii dintre",a,"si",b,"in baza",baza,"este: ",end="")

    # afisam rezultatul inmultirii
    for i in range(0,len(lista)):
        if lista[i]<=9:
            print(lista[i],end="")
        elif lista[i] == 10:
            print("A",end="")
        elif lista[i] == 11:
            print("B",end="")
        elif lista[i] == 12:
            print("C",end="")
        elif lista[i] == 13:
            print("D",end="")
        elif lista[i] == 14:
            print("E",end="")
        elif lista[i] == 15:
            print("F",end="")

    # cu ajutorul urmatoarelor randuri returnam rezultatul sub forma de string pentru a ne fi mai usor sa-l folosim in 
    # viitoarele calcule, daca avem nevoie de rezultat bineinteles   
    s = ""
    for i in range(0,len(lista)):
        if lista[i] <= 9:
            s += str(lista[i])
        elif lista[i] == 10:
            s += str("A")
        elif lista[i] == 11:
            s += str("B")
        elif lista[i] == 12:
            s += str("C")
        elif lista[i] == 13:
            s += str("D")
        elif lista[i] == 14:
            s += str("E")
        elif lista[i] == 15:
            s += str("F")
    
    return s

def inmultire():
    """
        Aceasta este functia ce are rolul de a citi si a apela inmultirea unui numar cu o cifra intr-o baza data de catre utilizator
        functie ce e apelata in sub-meniul 1, cel corespunzator operatiilor
    """

    baza = int(input("Introduceti baza in care o sa se realizeze inmultirea: "))
    a = input("Introduceti primul numar: " )
    b = input("Intoruceti al doilea numar: ")
    rezolva_inmultire(a,b,baza)
    print("")
    print("")
