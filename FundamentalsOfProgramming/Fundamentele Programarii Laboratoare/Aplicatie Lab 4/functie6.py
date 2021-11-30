"""
    Rolul acestui modul este de a stoca functia 6, adica functia undo
"""

import design
import globalvariable

def functie_6(l):
    """
        Aceasta este functia undo, ce are rolul de a readuce lista la forma ei dinaintea ultimei operatii
        Ex: daca la lista s-a adaugat un numar, aceasta functie aduce lista la forma ei fara numarul adaugat in cadrul ultimei operatii
    """
    #lung1 = len (l)
    #lung2 = len (globalvariable.copie)
    if len(globalvariable.copie) == 0:
        print("Nu au fost facute operatii ce schimba lista!")
    else:
        """
        if lung1 > lung2:
            lung2,lung1 = lung1, lung2                                                                                                                  
        for i in range(0,lung2-lung1):
            l.pop()
        """
        pozitie = globalvariable.contor
        l = globalvariable.copie[pozitie-1]
        globalvariable.contor = 0
        globalvariable.copie.pop()
        print("Lista a revenit la forma avuta inainte de ultima operatie!")
        print(l)
        
    return l
    