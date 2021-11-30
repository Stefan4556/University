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
    if len(globalvariable.copie) == 0:
        print("Nu au fost facute operatii ce schimba lista!")
        globalvariable.contor = 0
    else:
        pozitie = globalvariable.contor
        l = globalvariable.copie[pozitie-1]
        globalvariable.contor -= 1
        globalvariable.copie.pop()
        #print("Lista a revenit la forma avuta inainte de ultima operatie!")
    
    return l
