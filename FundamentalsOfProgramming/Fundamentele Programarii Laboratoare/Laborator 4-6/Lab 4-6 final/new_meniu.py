"""
    Cerinta laboratorului 6: Adaugare 1, Stergere 1, Suma, Afisare, Undo
"""

import cmath
import design
import auxiliare
import globalvariable
import functie1
import functie2
import functie3
import functie4
import functie5
import functie6

def functie_noua(l):

    lista_comenzi = input("Dati o lista de comenzi separate prin caracterul virgula(,), iar parametrii se scriu dupa comanda separati prin spatiu\n")

    lista_comenzi = lista_comenzi.split(',') # separam comenzile prin caracterul virgula
    
    for comanda in lista_comenzi:

        comanda = comanda.split() # separam parametrii prin spatiu de numele comenzii
        
        if comanda[0] == 'adaugare': # functia ce adauga un numar complex la finalul listei , numarul trebuie sa fie de tipul a + bj - maxim 1 parametru

            try:
                if len(comanda) <= 2:    
                    nr_complex = complex(comanda[1])
                    functie1.functie_1_1(l,nr_complex)
            except (ValueError, IndexError):
                pass
        
        elif comanda[0] == 'stergere': # functia ce sterge un numar de pe o pozitie data - maxim 1 parametru

            try:
                if len(comanda) <= 2:
                    poz = int(comanda[1])
                    functie2.functie_2_1(l,poz)
            except (ValueError, IndexError):
                pass
        
        elif comanda[0] == 'suma': # functia ce calculeaza suma elementelor dintre 2 pozitii - maxim 2 parametrii

            try:
                if len(comanda) <= 3:
                    poz1 = int(comanda[1])
                    poz2 = int(comanda[2])
                    print(functie4.functie_4_1(l,poz1,poz2))
            except (ValueError,IndexError):
                pass

        elif comanda[0] == 'afisare': # functia ce se ocupa cu afisarea listei - doar comanda

            if len(comanda) <= 1:
                functie4.afisare(l) 

        elif comanda[0] == 'undo': # functia ce se ocupa cu undo - doar comanda
            
            if len(comanda) <= 1: 
                l = functie6.functie_6(l)

def meniu_nou():

    l = [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j]

    functie_noua(l)

meniu_nou()