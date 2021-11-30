"""
    Modulul LC_conversie_baza_intermediara se ocupa cu retinerea a 3 functii:
    1 - spargere numar
    2 - rezolva conversie baza intermediara
    3 - conversie baza intermediara
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

def rezolva_conversie_baza_intermediara(baza1,nr,baza2):
    """
        Metoda conversiei prin intermediul unei baze intermediare este urmatoarea:
        1 - numarul primit in baza1 este trecuta in baza 10
        2 - numarul din baza 10 este trecut in baza2, primita in enunt dupa care este returnat
    """

    lista_nr = spargere_numar(nr)
    putere = 1
    rezultat = 0
    # etapa 1
    for i in range(len(lista_nr)-1,-1,-1):
        rezultat += lista_nr[i]*putere
        putere *= baza1
    lista_rezultat = []

    # etapa 2
    cat = rezultat // baza2
    rest = rezultat % baza2 
    if cat == 0:
        lista_rezultat.append(rest)
    else:
        while cat != 0:
           lista_rezultat.append(rest)
           rezultat = cat
           cat = rezultat // baza2
           rest = rezultat % baza2 
        lista_rezultat.append(rest)
    
    # afisam rezultatul
    print("Rezultatul conversiei numarului",nr,"din baza",baza1,"in baza",baza2,"cu ajutorul metodei bazei intermediare este ",end="")
    for i in range(len(lista_rezultat)-1,-1,-1):
        if lista_rezultat[i]<=9:
            print(lista_rezultat[i],end="")
        elif lista_rezultat[i] == 10:
            print("A",end="")
        elif lista_rezultat[i] == 11:
            print("B",end="")
        elif lista_rezultat[i] == 12:
            print("C",end="")
        elif lista_rezultat[i] == 13:
            print("D",end="")
        elif lista_rezultat[i] == 14:
            print("E",end="")
        elif lista_rezultat[i] == 15:
            print("F",end="")

    # dam return la string pentru a putea folosi rezultatul in viitoarele calcule, in cazul in care avem nevoie
    s = ""
    for i in range(len(lista_rezultat)-1,-1,-1):
        if lista_rezultat[i] <= 9:
            s += str(lista_rezultat[i])
        elif lista_rezultat[i] == 10:
            s += str("A")
        elif lista_rezultat[i] == 11:
            s += str("B")
        elif lista_rezultat[i] == 12:
            s += str("C")
        elif lista_rezultat[i] == 13:
            s += str("D")
        elif lista_rezultat[i] == 14:
            s += str("E")
        elif lista_rezultat[i] == 15:
            s += str("F")
    
    return s
    

def conversie_baza_intermediara():
    """
        Aceasta este functia cu rolul de a citi si apela conversia prin baza intermediara a unui numar primt intr-o baza baza1 in alta baza baza2,
        iar aceasta functie este apelata in sub-meniul 2, cel corespunzator conversiilor
    """

    baza1 = int(input("Introduceti baza numarului ce urmeaza sa fie citit: "))
    nr = input("Introduceti numarul: ")
    baza2 = int(input("Introduceti baza in care doriti sa convertiti numarul citit: "))
    rezolva_conversie_baza_intermediara(baza1,nr,baza2)
    print("")
    print("")
