"""
    Rolul acestui modul este de a stoca functia 3 cat si functiile aferente acesteia
"""

import design
import auxiliare
import globalvariable
import cmath

def functie_3_1(l,poz1,poz2):
    """
        Functia tipareste pe ecran partea imaginara a numerelor complexe ce se situeaza intre poz1 si poz2
        pozitii introduse de catre utilizator
    """
    ll = []
    
    if poz1 > poz2:
        poz1,poz2 = poz2,poz1

    for i in range(poz1,poz2+1):
        ll.append(int(l[i].imag))

    return ll
        
def functie_3_2(l):
    """
        Functia tipareste toate numerele complexe ce au modulul mai mic decat 10
        In cazul in care nu exista numere cu modulul mai mic decat 10, este afisat nu exista
    """
    ll =[]

    for i in range (0,len(l)):

        if abs(l[i]) < 10:
            ll.append(l[i])
    
    return ll

def functie_3_3(l):                                                       
    """
        Rolul acestei functii este de a tipari pe ecran numerele al caror modul este egal cu 10
        In cazul in care nu exista numere cu modulul egal cu 10, este afisat nu exista
    """   
    ll = []                                                              

    for i in range (0,len(l)):
        if abs(l[i]) == 10:
            ll.append(l[i])

    return ll

def functie_3(l):
    """
        Aceasta este functia ce are rolul de a cauta numerele in program
        Si reuneste 3 subfunctii formand meniul functiei 3, interfata ce contine 3 optiuni:
            1) Tipareste partea imaginara pentru numerele din lista, programul primind 2 pozitii introduse de catre utilizator
            2) Tipareste toate numerele complexe care au modulul mai mic decat 10
            3) Tipareste toate numerele complexe ce au modulul egal cu 10
    """
    design.design_functie_3()
    a = auxiliare.functie_citire_si_verificare_comanda(1,4)
    while a != 4:
        
        if a == 1:
            poz1 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            poz2 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
            ll = []
            ll = functie_3_1(l,poz1,poz2)
            print(ll)

        if a == 2:
            ll = []
            ll = functie_3_2(l)
            if len(ll) > 0:
                print(ll)
            else:
                print("Nu exista")

        if a == 3:
            ll = []
            ll = functie_3_3(l)
            if len(ll) > 0:
                print (ll)
            else:
                print("Nu exista")

        design.design_functie_3()
        a = auxiliare.functie_citire_si_verificare_comanda(1,4)
    
    print('\033c')
    design.design_meniu()