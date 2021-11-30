"""
    Rolul acestui modul este de a stoca functia 5 si functiile aferente acesteia
"""

import design
import auxiliare
import globalvariable
import functie4
import cmath

def prim(n):
    """
        Functia verifica daca un numar este prim sau nu
    """
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    d = 3
    while d * d <= n:
        if n % d == 0:
            return 0
        d += 2
    return 1

def functie_5_1(l):
    """
        Functie ce elimina numerele complexe a caror parte reala este numar prim
    """
    i = 0
    ll=[]
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1                        
    while i < len(l):
        imag = l[i][0]
        if prim(imag) == 0:
            ll.append(l[i])
        i += 1
    #print("Au fost eliminate cu succes, numerele complexe a caror parte reala era numar prim!")
    return ll

def functie_5_2_1(l,numar):
    """
        Functia elimina numerele complexe din lista, al caror modul este mai mic decat un numar introdus de catre utilizator
    """
    i = 0
    ll=[]
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    while i < len(l):
        nr = complex(l[i][0],l[i][1])
        if abs(nr) >= numar:                   
            ll.append(l[i])
        i += 1
    return ll

def functie_5_2_2(l,numar):
    """
        Functia elimina numerele complexe din lista, al caror modul este egal cu un numar introdus de catre utilizator
    """
    i = 0
    ll=[]
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    while i < len(l):
        nr = complex(l[i][0],l[i][1])
        if float(abs(nr)) != numar:                                                                                                                     
            ll.append(l[i])
        i += 1
    return ll

def functie_5_2_3(l,numar):
    """
        Functia elimina numerele complexe din lista, al caror modul este mai mare decat un numar introdus de catre utilizator
    """
    i = 0
    ll=[]
    globalvariable.copie.append(list(l))
    globalvariable.contor += 1
    while i < len(l):
        nr = complex(l[i][0],l[i][1])
        if abs(nr) <= numar:
            ll.append(l[i])
        i += 1
    return ll

def functie_5_2(l):
    """
        Aceasta functie are rolul de a filtra numerele in functie de modulul lor si numarul introdus de catre utilizator si avem 3 cazuri:
            1) Elimina numerele cu modulul mai mic decat numar
            2) Elimina numerele cu modulul egal
            3) Elimina numerele cu modulul mai mare
    """
    numar = auxiliare.functie_citire_numar_intreg()
    design.design_functie_5_2(numar)
    a = auxiliare.functie_citire_si_verificare_comanda(1,4)
    while a != 4:

        lista=[]

        if a == 1:
            lista = functie_5_2_1(l,numar)
            functie4.afisare(lista)
            print("Au fost eliminate cu succes numerele cu modulul mai mic decat",numar)

        if a == 2:
            lista = functie_5_2_2(l,numar)
            functie4.afisare(lista)
            print("Au fost eliminate cu succes numerele cu modulul egal cu",numar)

        if a == 3:
            lista = functie_5_2_3(l,numar)
            functie4.afisare(lista)
            print("Au fost eliminate cu succes numerele cu modulul mai mare decat",numar)

        design.design_functie_5_2(numar)
        a = auxiliare.functie_citire_si_verificare_comanda(1,4)

def functie_5(l):
    """
        Aceasta este functia ce are rolul de a filtra numerele complexe din lista
        Si reuneste 2 subfunctii formand meniul functiei 5, interfata ce contine 2 optiuni:
            1) Elimina din lista numerele complexe ce au partea reala egala cu un numar prim
            2) Elimina din lista numerele complexe ce au modulul mai mic / egal / mai mare decat un numar introdus de catre utilizator
                Aceasta functie avand alte 3 subfunctii, fiecare fiind pentru unul din cele 3 cazuri mentionate anterior
            
    """
    design.design_functie_5()
    a = auxiliare.functie_citire_si_verificare_comanda(1,3)
    while a != 3:

        lista=[]

        if a == 1:
            lista = functie_5_1(l)
            functie4.afisare(lista)
            print("Au fost eliminate cu succes, numerele complexe a caror parte reala era numar prim!")

        if a == 2:
            functie_5_2(l)

        design.design_functie_5()
        a = auxiliare.functie_citire_si_verificare_comanda(1,3)
    #print("")
    print('\033c')
    design.design_meniu()