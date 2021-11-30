"""
    Aceasta este functia principala ce apleaza toate celelalte functii din celelalte module si le leaga intre ele
"""

"""
    Mai jos importam toate fisierele in care avem functii ce le folosim in cadrul programului principal
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
import teste
                                                                                                                      
def meniu():
    """
        Acesta este meniul principal, loc din care sunt apelate toate celelalte functii din celelalte fisiere
        In functie de comanda introdusa este apelata functia
        Meniul contine 7 comenzi:
            1) Adauga numar in lista
            2) Modifica elemente din lista
            3) Cautare numere
            4) Operatii cu numerele din lista
            5) Filtrare
            6) Undo
            7) Afiseaza lista curenta
            8) Exit
    """
    print('\033c')
    l = [[1,2],[3,4],[1,2],[4,2],[5,6],[7,8],[8,6],[6,8]]
    design.design_meniu()
    comanda = auxiliare.functie_citire_si_verificare_comanda(1,8)
    print("")
    
    while comanda != 8:
        
        if comanda == 1:
            print('\033c')
            functie1.functie_1(l)
            
        if comanda == 2:
            print('\033c')
            functie2.functie_2(l)
            
        if comanda == 3:
            print('\033c')
            functie3.functie_3(l)
            
        if comanda == 4:
            print('\033c')
            functie4.functie_4(l)

        if comanda == 5:
            print('\033c')
            functie5.functie_5(l)
            
        if comanda == 6:
            print('\033c')
            l = functie6.functie_6(l)
            design.design_meniu()

        if comanda == 7:
            print('\033c')
            functie4.afisare(l)
            print("")
            design.design_meniu()
        
        comanda = auxiliare.functie_citire_si_verificare_comanda(1,9)
        
    print("La revedere!")
    
teste.rulare_teste()
meniu()