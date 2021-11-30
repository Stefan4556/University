"""
    Acesta este modulul ce gestioneaza meniul principal si functiile aferente acestuia, de asemenea
    in acest modul sunt realizate toate importurile pentru a putea fi utilizate toate celelalte functii
"""

from LC_adunare import adunare
from LC_scadere import scadere
from LC_inmultire import inmultire
from LC_impartire import impartire

from LC_conversie_substitutie import conversie_substitutie
from LC_conversie_baza_intermediara import conversie_baza_intermediara
from LC_conversii_rapide import conversie_rapida
from LC_conversie_impartiri import conversie_impartiri

from LC_rezolva_problema import rezolva_problema

from LC_design import design_meniu,design_meniu_conversii,design_meniu_operatii

def meniu_operatii():
    """
        Acesta functie reprezinta functia ce se ocupa de sub-meniul 1, iar acesta cuprinde:
        1 - Adunarea a 2 numere intr-o baza n
        2 - Scadarea a 2 numere intr-o baza n
        3 - Inmultirea unui numar in baza n cu o cifra
        4 - Impartirea unui numar in baza n la o cifra
        5 - Back
    """
    
    design_meniu_operatii()

    cmd = int(input("Introduceti comanda: "))

    while cmd != 5:

        if cmd == 1:
            """
                Daca utilizatorul introduce comanda 1, acesta apeleaza functia adunare, functie ce este definita
                in modulul LC_adunare
            """

            adunare()
        
        elif cmd == 2:
            """
                Daca utilizatorul introduce comanda 2, acesta apeleaza functia scadere, functie definita in modulul
                LC_scadere
            """

            scadere() 
        
        elif cmd == 3:
            """
                Daca utilizatorul introduce comanda 3, acesta apeleaza functia inmultire, functie definita in modulul
                LC_inmultire
            """

            inmultire()
        
        elif cmd == 4:
            """
                Daca utilizatorul introduce comanda 4, acesta apeleaza functia impartire ce e definita in modulul LC_impartire
            """

            impartire()
        
        else:

            print("Comanda invalida!")
        
        design_meniu_operatii()
        cmd = int(input("Introduceti comanda: "))
    
    print("")
    design_meniu()
        
def meniu_conversii():
    """
        Acesta functie reprezinta functia ce se ocupa de sub-meniul 2, iar acesta cuprinde:
        1 - Conversia unui numar dintr-o baza in alta prin impartiri repetate
        2 - Conversia unui numar dintr-o baza in alta prin metoda substitutiei
        3 - Conversia unui numar dintr-o baza in alta printr-o baza intermediara
        4 - Conversia unui numar dintr-o baza in alta prin conversii rapide din 2->4,8,16 sau 16->2,4,8
        5 - Back
    """

    design_meniu_conversii()

    cmd = int(input("Introduceti comanda: "))

    while cmd != 5:

        if cmd == 1:
            """
                Daca utilizatorul introduce comanda 1, acesta apeleaza functia conversie_impartiri, functie ce este definita
                in modulul LC_conversie_impartiri
            """

            conversie_impartiri()
            #merge partial de uitat peste ea

        elif cmd == 2:
            """
                Daca utilizatorul introduce comanda 2, acesta apeleaza functia conversie_substitutie, functie ce este definita
                in modulul LC_conversie_substitutie
            """

            conversie_substitutie()
        
        elif cmd == 3:
            """
                Daca utilizatorul introduce comanda 3, acesta apeleaza functia conversie_baza_intermediara, functie ce este definita
                in modulul LC_conversie_baza_intermediara
            """

            conversie_baza_intermediara()

        elif cmd == 4:
            """
                Daca utilizatorul introduce comanda 4, acesta apeleaza functia conversie_rapida, functie ce este definita in modulul 
                LC_conversii_rapide
            """

            conversie_rapida()

        else:

            print("Comanda invalida!")
        
        design_meniu_conversii()
        cmd = int(input("Introduceti comanda: "))
    
    print("")
    design_meniu()

def meniu_principal():
    """
        Aceasta functie reprezinta meniul principal, meniu ce are 3 obtiuni:
        1 - Operatii cu numere
        2 - Conversii cu numere
        3 - Rezovla problema
        4 - Exit
    """

    design_meniu()

    cmd = int(input("Introduceti comanda: "))

    while(cmd != 4):

        if cmd == 1:
            """
                Pentru comanda 1, programul se duce in meniul cu operatii
            """

            meniu_operatii()
        
        elif cmd == 2:
            """
                Pentru comanda 2, programul se duce in meniul cu conversii
            """

            meniu_conversii()
        
        elif cmd == 3:
            """
                Enuntul problemei:
                Sa se dea un numar a intr-o baza oarecare si un numar b intr-o baza putere a lui 2, dupa care cele 2 numere 
                sunt convertite in baza 2 si adunate, dupa ce sunt adunate rezultatul este convertit in baza 2.
                Pe parcursul acestei probleme am optat pentru varianta cu afisari multiple pentru a face mult mai usor problema
                de inteles.
            """

            rezolva_problema()
            design_meniu()

        else:

            print("Comanda invalida!")
        
        cmd = int(input("Introduceti comanda: "))
    
    print("La revedere!")

meniu_principal()

"""
    Cu ajutorul acestei comenzi programul meu o sa porneasca
"""
