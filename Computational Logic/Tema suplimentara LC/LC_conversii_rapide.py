"""
    Modulul LC_conversii_rapide se ocupa cu retinerea a 4 functii:
    1 - spargere numar
    2 - returneaza cifra corespunzatoare
    3 - rezolva conversie rapida
    4 - conversie rapida
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

def returneaza_cifra_corespunzatoare(lista1,lista2):
    """
        Aceasta functie primeste o lista si returneaza pozitia acesteia in a 2 a lista de liste
    """

    for i in range(0,len(lista2)):

        if lista1 == lista2[i]:
            return i

def rezolva_conversie_rapida(baza1,nr,baza2):
    """
        Acest program se ocupa cu conversiile propriu-zise, daca numarul este in baza 2 si dorim
        sa il convertim intr-o baza putere a lui 2, trebuie sa grupam cifrele de la dreapta la stanga
        in grupuri de cate radical(2^putere), iar acele grupuri sunt corespunzatoare unei cifre 
        in baza respectiva.
        Daca avem cazul din baza mai mare decat 2 in baza 2, fiecare cifra inseamna radical(2^putere) cifre in baza 2,
        pe scurt o cifra in baza 16 inseamna 4 cifre in baza 2 si tot asa
    """
    lista_baza_16 = [
                        [0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],
                        [0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],
                        [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],
                        [1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]
                    ]
    lista_baza_8 =  [
                        [0,0,0],[0,0,1],[0,1,0],[0,1,1],
                        [1,0,0],[1,0,1],[1,1,0],[1,1,1]
                    ]
    lista_baza_4 =  [
                        [0,0],[0,1],[1,0],[1,1]
                    ]

    if baza1 < baza2:
        # trecem din baza mai mica in baza mai mare si stim ca suntem in cazul 1
        caz = 1
        grupari = 0
        copie = baza2
        while copie!=0:
            copie //= 2
            grupari += 1
        grupari -= 1
    else:
        # stim ca suntem in cazul in care convertim un numar dintr-o baza mai mare decat 2 in baza 2
        caz = 2
    
    lista_nr = spargere_numar(nr)   # convertim numarul

    if caz == 1:    # trecem din b2 in baza mai mare

        rest = len(lista_nr) % grupari # determinam daca mai trebuie sau nu adaugate 0 uri

        if rest != 0:
            while  len(lista_nr) % grupari != 0:
                rest -= 1
                lista_nr.insert(0,0)

        # convertim numarul
        lista_noua = []
        for i in range(len(lista_nr)-1,0,-grupari):

            lista_comp = []

            for j in range(0,grupari):
                lista_comp.append(lista_nr[i-grupari+j+1])
            if baza2 == 4:
                val = returneaza_cifra_corespunzatoare(lista_comp,lista_baza_4)

            elif baza2 == 8:
                val = returneaza_cifra_corespunzatoare(lista_comp,lista_baza_8)

            elif baza2 == 16:
                val = returneaza_cifra_corespunzatoare(lista_comp,lista_baza_16)

            lista_noua.append(val)

        lista_noua.reverse()
        # punem rezultatul final intr-un string pentru a ne fi mai usor sa-l utilizam in problemele viitoare in cazul 
        # in care avem nevoie de aceast rezultat
        s=""
        for i in range(0,len(lista_noua)):
            if lista_noua[i] <= 9:
                s += str(lista_noua[i])
            elif lista_noua[i] == 10:
                #lista_noua[i] = "A"
                s += str("A")
            elif lista_noua[i] == 11:
                #lista_noua[i] = "B"
                s += str("B")
            elif lista_noua[i] == 12:
                #lista_noua[i] = "C"
                s += str("C")
            elif lista_noua[i] == 13:
                #lista_noua[i] = "D"
                s += str("D")
            elif lista_noua[i] == 14:
                #lista_noua[i] = "E"
                s += str("E")
            elif lista_noua[i] == 15:
                #lista_noua[i] = "F"
                s += str("F")

        print("Rezultatul conversiei numarului in baza 2 ",nr," in baza ",baza2," este ",s)
        return s

    else:

        # trecem dintr-o baza mai mare in baza 2
        lista_noua = []

        for i in range(0,len(lista_nr)):
            
            l = []

            if baza1 == 16:
                l = lista_baza_16[lista_nr[i]]
            elif baza1 == 8:
                l = lista_baza_8[lista_nr[i]]
            elif baza1 == 4:
                l = lista_baza_4[lista_nr[i]]
            
            for j in range(0,len(l)):
                lista_noua.append(l[j])

        # punem rezultatul final intr-un string pentru a ne fi mai usor sa-l utilizam in problemele viitoare in cazul 
        # in care avem nevoie de aceast rezultat
        s=""

        for i in range(0,len(lista_noua)):
            s += str(lista_noua[i])

        print("Rezultatul conversiei numarului in baza",baza1,nr,"in baza 2 este",s)    
        return s


def conversie_rapida():
    """
        Aceasta este functia cu rolul de a citi si apela conversia rapida din baza 2 intr-o baza putere a lui 2, respectiv
        dintr-o baza mai mare, tot putere a lui 2 in baza 2.
        Totodata aceasta functie este apelata in sub-meniul 2, cel corespunzator conversiilor
    """

    baza1 = int(input("Introduceti baza numarului pe care doriti sa-l transformati: "))
    nr = input("Introduceti numarul: ")
    baza2 = int(input("Introduceti baza in care doriti sa fie transformat numarul: "))
    rez = rezolva_conversie_rapida(baza1,nr,baza2)
    print("")
    print("")
    return rez
