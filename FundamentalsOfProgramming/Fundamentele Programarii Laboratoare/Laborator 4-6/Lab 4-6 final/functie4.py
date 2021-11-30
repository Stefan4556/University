"""
    Rolul acestui modul este de a stoca functia 4 cat si functiile aferente acesteia
"""

import design
import auxiliare
import globalvariable
import cmath

def afisare(l):
    """
        Functie de afisare a listei
    """
    #for i in range(0,len(l)):
        #print (l[i], end=" ")
    print(l)

def sortare(l):
    """
        Functia se ocupa cu sortarea descrescatoare a listei dupa partea imaginara
    """
    n = len(l)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if l[i].imag < l[j].imag:
                l[i],l[j] = l[j],l[i]

    return l
                                                                                                                         
def functie_4_1(l,poz1,poz2):
    """
        Afiseaza suma elementelor din intervalul inchis [l[poz1],l[poz2]]
    """
    if poz1 > poz2:
        poz1,poz2 = poz2,poz1

    suma = 0

    for i in range(poz1,poz2+1):
        suma += l[i]
    
    return suma

def functie_4_2(l,poz1,poz2):
    """
        Afiseaza produsul elementelor din intervalul inchis [l[poz1],l[poz2]]
    """
    if poz1 > poz2:
        poz1,poz2 = poz2,poz1

    produs = 1

    for i in range(poz1,poz2+1):                                                                                                               
        produs *= l[i]
   
    return produs

def functie_4_3(l):
    """
        Aceasta functie apeleaza 2 functii ajutatoare, rolul ei fiind de a sorta elementele descrescator dupa partea imaginara
        si de a afisa lista sortata
    """
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    sortare(l)
    return l

def functie_4(l):
    """
        Aceasta este functia ce are rolul de a realiza diferite operatii cu numerele din lista
        Si reuneste 3 subfunctii formand meniul functiei 4, interfata ce contine 3 optiuni:
            1) Tipareste suma numerelor dintr-o secventa data de catre utilizator cu ajutorul a 2 pozitii introduse de acesta
            2) Tipareste produsul numerelor dintr-o subsecventa data de catre utilizator cu ajutorul a 2 pozitii introduse de acesta
            3) Tipareste toate numerele complexe ce au modulul egal cu 10
    """
    design.design_functie_4()
    a = auxiliare.functie_citire_si_verificare_comanda(1,4)
    while a != 4:

        if a == 1:
            poz1 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            poz2 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            suma = functie_4_1(l,poz1,poz2)
            print("Suma numerelor din secventa este: ",suma)
            
        if a == 2:
            poz1 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            poz2 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            produs = functie_4_2(l,poz1,poz2)
            print ("Produsul numerelor din subsecventa este: ", produs)

        if a == 3:
            functie_4_3(l)
            print("Lista a fost sortata descrescator!")
            afisare(l)

        design.design_functie_4()
        a = auxiliare.functie_citire_si_verificare_comanda(1,4)
   
    print('\033c')
    design.design_meniu()