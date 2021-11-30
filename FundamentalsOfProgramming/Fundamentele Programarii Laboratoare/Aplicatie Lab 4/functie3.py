"""
    Rolul acestui modul este de a stoca functia 3 cat si functiile aferente acesteia
"""

import design
import auxiliare
import globalvariable
import cmath

def functie_3_1(l):
    """
        Functia tipareste pe ecran partea imaginara a numerelor complexe ce se situeaza intre poz1 si poz2
        pozitii introduse de catre utilizator
        In cazul in care trebuie sa facem assert trebuie facuti urmatorii pasi:
        1) Se creeaza o lista auxiliara in functie vida
        2) Poz1 si poz2 sunt mutati in functia principala
        3) De fiecare data cand dam print la ceva incarcam lista auxiliara cu ceea ce afisam
        4) Dam return la final pentru a realiza assert-ul
        Acesti pasi se pot aplica la: functie_3_2(mai putin cel cu pozitia), functie_3_3(mai putin cel cu pozitia)
    """
    poz1 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
    poz2 = auxiliare.functie_citire_si_verificare_pozitie(0,len(l)-1)
    if poz1 > poz2:
        poz1,poz2 = poz2,poz1
    for i in range(poz1,poz2+1):
        #print(l[i].imag,end=" ")
        print(l[i][1],end=" ")
    print("")
        
def functie_3_2(l):
    """
        Functia tipareste toate numerele complexe ce au modulul mai mic decat 10
        In cazul in care nu exista numere cu modulul mai mic decat 10, este afisat nu exista
    """
    ok = True
    for i in range (0,len(l)):
        nr = complex(l[i][0],l[i][1])
        if abs(nr) < 10:
            #print(l[i],end=" ")
            print(nr,end=" ")
            ok = False
    if ok == True:
        print("Nu exista!")
    print("")

def functie_3_3(l):                                                       
    """
        Rolul acestei functii este de a tipari pe ecran numerele al caror modul este egal cu 10
        In cazul in care nu exista numere cu modulul egal cu 10, este afisat nu exista
    """                                                                 
    ok = True
    for i in range (0,len(l)):
        nr = complex(l[i][0],l[i][1])
        if abs(nr) == 10:
            #print(l[i],end=" ")
            print(nr,end=" ")
            ok = False
    if ok == True:
        print("Nu exista!")
    print("")

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
            functie_3_1(l)

        if a == 2:
            functie_3_2(l)

        if a == 3:
            functie_3_3(l)

        design.design_functie_3()
        a = auxiliare.functie_citire_si_verificare_comanda(1,4)
    #print("")
    print('\033c')
    design.design_meniu()