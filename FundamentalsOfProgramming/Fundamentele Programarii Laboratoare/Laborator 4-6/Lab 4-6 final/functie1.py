"""
    Rolul acestui modul este de a stoca functia 1 cat si functiile auxiliare acesteia
"""

import design
import auxiliare
import globalvariable
import cmath

def functie_1_1(l,z): 
    """
        Functia ce adauga un numar complex introdus de catre utilizator la finalul listei
    """                                                 
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    l.append(z)
    return l
    
def functie_1_2(l,z,poz):            
    """
        Functia ce insereaza un numar complex introdus de catre utilizator pe o pozitie scrisa tot de catre utilizator
    """
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    l.append(0)
    for i in range(len(l)-1,poz,-1):
        l[i] = l[i-1]
    l[poz] = z
    return l

def functie_1(l):
    """
        Aceasta este functia ce adauga numere in lista
        Si uneste cele 2 subfunctii formand meniul functiei 1, interfata ce contiine 2 optiuni:
            1) Cea de a adauga un numar la sfarsitul listei
            2) Inserarea unui numar complex introdus de utilizator o pozitie introdusa tot de acesta
    """                           
    design.design_functie_1()
    a = auxiliare.functie_citire_si_verificare_comanda(1,3)
    while a != 3:
        
        if a == 1:
            z = auxiliare.functie_citire()
            functie_1_1(l,z)
            print("Numarul a fost adaugat cu succes!")

        if a == 2:
            z = auxiliare.functie_citire()
            poz = auxiliare.functie_citire_si_verificare_pozitie(0,len(l))
            functie_1_2(l,z,poz)
            print("Numarul a fost inserat cu succes!")
        
        design.design_functie_1()

        a = auxiliare.functie_citire_si_verificare_comanda(1,3)

    print('\033c')
    design.design_meniu()