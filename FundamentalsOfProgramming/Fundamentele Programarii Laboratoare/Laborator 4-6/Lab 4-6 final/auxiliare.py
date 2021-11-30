"""
    Rolul acestui modul este de a stoca functiile de citire si verificare a valoriilor introduse de catre utilizator
"""

def functie_verificare_numar_natural(poz):          
    """
        Aceasta functie verifica daca valoarea introdusa este un numar natural
    """
    while True:
        if poz.isdigit():
            break
        print("Valoarea introdusa este gresita, va rugam sa introduceti un numar natural!")
        poz = input("Introduceti pozitia: ")
    return int(poz)

def functie_verificare_numar(poz):                 
    """
        Aceasta functie verifica daca valoarea introdusa este un numar intreg
    """
    while True:
        try:
            nr = int(poz)
            break
        except ValueError:
            print("Valoarea introdusa este gresita, va rugam sa introduceti un numar!")
            poz = input("Introduceti un numar: ")
    return nr

def functie_citire(): 
    """
        Aceasta functie citeste un numar complex, citind pe rand partea reala, respectiv partea imaginara 
    """                                                      
    a = input("Introduceti partea reala a numarului complex: ")
    a = functie_verificare_numar(a)
    b = input("Introduceti partea imaginara a numaraului complex: ")
    b = functie_verificare_numar(b) 
    z = complex(a,b)
    return z

def functie_citire_pozitie():
    """
        Aceasta functie citeste pozitia si verifica in acealsi timp daca valoarea introdusa este una pozitiva pentru ca o pozitie nu poate sa fie negativa
    """
    poz = input("Introduceti pozitia: ")                           
    return functie_verificare_numar_natural(poz)

def functie_citire_comanda():
    """
        Aceasta functie citeste comanda si verifica daca valoarea introdusa este un numar natural
    """
    com = input("Introduceti comanda: ")
    return functie_verificare_numar_natural(com)

def functie_citire_numar_intreg():
    """
        Aceasta functie citeste numere intregi si verifica daca valoarea introdusa este una corecta
    """
    a = input("Introduceti numarul: ")
    a = functie_verificare_numar(a)
    return a

def functie_citire_si_verificare_pozitie(poz1,poz2):
    """
        Aceasta functie citeste o pozitie si verifica daca aceasta este corecta
        Ex: avem o lista de la 0 la 7, aceasta functie verifica daca valoarea citita apartine intervalului inchis [0,7] 
        daca e buna, o returneaza, daca nu o sa l puna pe utilizator sa introduca alta valoare
    """
    while True:
        val = functie_citire_pozitie()
        if poz1 <= val and val <= poz2:
            return val
        print("Va rugam sa introduceti o valoare cuprinsa intre",poz1,"si",poz2)

def functie_citire_si_verificare_comanda(com1,com2):
    """
        Aceasta functie citeste o comanda si verifica daca aceasta este corecta
        Ex: avem comenzi de la 1 la 7, iar ea verifica daca valoarea apartine intervalului inchis
        daca e buna o returneaza, altfel il pune pe utilizator sa introduca alta valoare
    """
    while True:
        com = functie_citire_comanda()
        if com1 <= com and com <= com2:
            return com
        print("Va rugam sa introduceti o valoare cuprinsa intre",com1,"si",com2)