"""
    Rolul acestui modul este de a stoca functia 2 cat si functiile aferente acesteia
"""

import design
import auxiliare
import globalvariable
import cmath

def functie_2_1(l,poz):
    """
        Functia sterge elmentul situat pe pozitia poz, introdusa de catre utilizator, adica elementul l[i]
    """
    #poz = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    l.pop(poz)
    #print("Numarul a fost sters cu succes!")
    #return l
    return l

def functie_2_2(l,poz1,poz2):
    """
        Functia sterge elementele situate intre pozitiile min(poz1,poz2) si max(poz1,poz2), introduse de catre utilizator
        adica elementele l[poz1],l[poz1+1],...,l[poz2]
    """
    #poz1 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
    #poz2 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    if poz1 > poz2:
        poz1,poz2 = poz2, poz1
    for i in range(poz2,poz1-1,-1):
        l.pop(i)
    #print("Numerele din interval au fost sterse cu succes!")
    return l
    

def functie_2_3(l,z1,z2):
    """
        Functia inlocuieste aparitiile primului numar complex introdus de catre utilizator, cu cel de al doilea numar complex
    """
    #print("Numarul pe care vreti sa-l inlocuiti:")
    #z1 = auxiliare.functie_citire()                                                                                                               
    #print("Numarul cu care vreti sa-l inlocuiti:")
    #z2 = auxiliare.functie_citire()
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    lista_1 = []
    lista_1.append(z1.real)
    lista_1.append(z1.imag)
    lista_2 = []
    lista_2.append(z2.real)
    lista_2.append(z2.imag)
    for i in range(0,len(l)):
        #if l[i] == z1:
        if l[i] == lista_1: 
            l[i] = lista_2
    #print("Numerele au fost inlocuite cu succes!")
    return l

def functie_2(l):
    """
        Aceasta este functia de modifica elemente din lista
        Si uneste cele 3 subfunctii formand meniul functiei 2, interfata ce contine 3 optiuni:
            1) Sterge elementul de pe o pozitie data de catre utilizator
            2) Sterge elementele de pe un interval de pozitii date de catre utilizator
            3) Inlocuieste aparitiile unui numar complex, cu alt numar complex, ambele numere fiind introduse de catre utilizator
    """
    design.design_functie_2()
    a = auxiliare.functie_citire_si_verificare_comanda(1,4)
    while a != 4:

        if a == 1:
            poz = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            functie_2_1(l,poz)
            print("Numarul a fost sters cu succes!")
        
        if a == 2:
            poz1 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            poz2 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            functie_2_2(l,poz1,poz2)
            print("Numerele din interval au fost sterse cu succes!")

        if a == 3:
            print("Numarul pe care vreti sa-l inlocuiti:")
            z1 = auxiliare.functie_citire()                                                                                                               
            print("Numarul cu care vreti sa-l inlocuiti:")
            z2 = auxiliare.functie_citire()
            functie_2_3(l,z1,z2)
            print("Numerele au fost inlocuite cu succes!")

        design.design_functie_2()
        a = auxiliare.functie_citire_si_verificare_comanda(1,4)
    #print("")
    print('\033c')
    design.design_meniu()