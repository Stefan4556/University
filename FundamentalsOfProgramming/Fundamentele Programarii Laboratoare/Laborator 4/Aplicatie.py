import cmath

copie = []

def design_meniu():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul principal
    """
    print("             Meniu")
    print("")
    print("1) Adauga numar in lista")
    print("2) Modifica elemente din lista")
    print("3) Cautare numere")
    print("4) Operatii cu numerele din lista")
    print("5) Filtrare")
    print("6) Undo")
    print("7) Exit")

def design_functie_1():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 1
    """
    print("1) Adauga un numar complex la sfarsitul listei")
    print("2) Insereaza un numar complex pe o pozitie data")
    print("3) Inapoi")

def design_functie_2():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 2
    """
    print("1) Sterge elementul de pe o pozitie citita")
    print("2) Sterge elementele de pe un interval de pozitii")
    print("3) Inlocuieste toate aparitiile unui numar cu alt numar")
    print("4) Inapoi")

def design_functie_3():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 3
    """
    print("1) Tipareste partea iamginara pentru numerele din interval")
    print("2) Tipareste toate numerele complexe ce au modulul mai mic decat 10")
    print("3) Tipareste toate numerele complexe ce au modulul egal cu 10")
    print("4) Inapoi")

def design_functie_4():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 4
    """
    print("1) Afiseaza suma numerelor dintr-o subsecventa data")
    print("2) Produsul numerelor dintr-o subsecventa data")
    print("3) Tipareste lista sortata descrescator dupa partea imaginara")
    print("4) Inapoi")

def design_functie_5_2(numar):
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 2 din functia 5
    """
    print("1) Elimina numerele complexe care au modulul mai mic decat ",numar)
    print("2) Elimina numerele complexe care au modulul egal cu ",numar)
    print("3) Elimina numerele complexe care au modulul mai mare decat ",numar)
    print("4) Inapoi")

def design_functie_5():
    """
        Aceasta functie se ocupa cu afisarea pe ecran a comenzilor din meniul functiei 5
    """
    print("1) Elimina din lista numerele complexe a caror parte reala este un numar prim")
    print("2) Elimina din lista numerele complexe al caror modul este mai mic / egal / mare decat un numar citit")
    print("3) Inapoi")

def functie_verificare_numar_natural(poz):          # verifica daca val introdusa este un numar natural
    """

    """
    while True:
        if poz.isdigit():
            break
        print("Valoarea introdusa este gresita, va rugam sa introduceti un numar natural!")
        poz = input("Introduceti pozitia: ")
    return int(poz)

def functie_verificare_numar(poz):                  # verifica daca val introdusa este un numar
    while True:
        try:
            nr = int(poz)
            break
        except ValueError:
            print("Valoarea introdusa este gresita, va rugam sa introduceti un numar!")
            poz = input("Introduceti un numar: ")
    return nr

def functie_citire():                                                       
    a = input("Introduceti partea reala a numarului complex: ")
    a = functie_verificare_numar(a)
    b = input("Introduceti partea imaginara a numaraului complex: ")
    b = functie_verificare_numar(b) 
    z = complex(a,b)
    return z

def functie_citire_pozitie():
    poz = input("Introduceti pozitia: ")                           
    return functie_verificare_numar_natural(poz)

def functie_citire_comanda():
    com = input("Introduceti comanda: ")
    return functie_verificare_numar_natural(com)

def functie_citire_numar_intreg():
    a = input("Introduceti numarul: ")
    a = functie_verificare_numar(a)
    return a

def functie_citire_si_verificare_pozitie(poz1,poz2):
    while True:
        val = functie_citire_pozitie()
        if poz1 <= val and val <= poz2:
            return val
        print("Va rugam sa introduceti o valoare cuprinsa intre",poz1,"si",poz2)

def functie_citire_si_verificare_comanda(com1,com2):
    while True:
        com = functie_citire_comanda()
        if com1 <= com and com <= com2:
            return com
        print("Va rugam sa introduceti o valoare cuprinsa intre",com1,"si",com2)

##########################################################################################################################
def functie_1_1(l):             # Adauga numarul complex la sfarsitul listei                                             #
    z = functie_citire()
    global copie
    copie = list(l)
    l.append(z)
    print("Numarul a fost adaugat cu succes!")

def functie_1_2(l):             # Insereaza numarul complex pe o pozitie data
    z = functie_citire()
    poz = functie_citire_si_verificare_pozitie(0,len(l))
    global copie
    copie = list(l)
    l.append(0)
    for i in range(len(l)-1,poz,-1):
        l[i] = l[i-1]
    l[poz] = z
    print("Numarul a fost inserat cu succes!")                                                                                      # - Capitolul 1 

def functie_1(l):                           
    design_functie_1()
    a = functie_citire_si_verificare_comanda(1,3)
    while a != 3:
        if a == 1:
            functie_1_1(l)
        if a == 2:
            functie_1_2(l)
        design_functie_1()
        a = functie_citire_si_verificare_comanda(1,3)
    print("")
    design_meniu()                                                                                                       #
##########################################################################################################################
                                                                                                                         #
def functie_2_1(l):
    poz = functie_citire_si_verificare_pozitie(0,len(l)-1)
    global copie
    copie = list(l)
    l.pop(poz)
    print("Numarul a fost sters cu succes!")

def functie_2_2(l):
    poz1 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    poz2 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    global copie
    copie = list(l)
    ct=0
    if poz1 > poz2:
        poz1,poz2 = poz2, poz1
    for i in range(poz2,poz1-1,-1):
        l.pop(i)
    print("Numerele din interval au fost sterse cu succes!")

def functie_2_3(l):
    print("Numarul pe care vreti sa-l inlocuiti:")
    z1 = functie_citire()                                                                                                               # - Capitolul 2 
    print("Numarul cu care vreti sa-l inlocuiti:")
    z2 = functie_citire()
    global copie
    copie = list(l)
    for i in range(0,len(l)):
        if l[i] == z1:
            l[i] = z2
    print("Numerele au fost inlocuite cu succes!")

def functie_2(l):
    design_functie_2()
    a = functie_citire_si_verificare_comanda(1,4)
    while a != 4:
        if a == 1:
            functie_2_1(l)
        if a == 2:
            functie_2_2(l)
        if a == 3:
            functie_2_3(l)
        design_functie_2()
        a = functie_citire_si_verificare_comanda(1,4)
    print("")
    design_meniu()
                                                                                                                         #
##########################################################################################################################
                                                                                                                         #
def functie_3_1(l):
    poz1 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    poz2 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    if poz1 > poz2:
        poz1,poz2 = poz2,poz1
    for i in range(poz1,poz2+1):
        print(l[i].imag,end=" ")
    print("")
        
def functie_3_2(l):
    ok = True
    for i in range (0,len(l)):
        if abs(l[i]) < 10:
            print(l[i],end=" ")
            ok = False
    if ok == True:
        print("Nu exista!")
    print("")

def functie_3_3(l):                                                                                                                         # - Capitolul 3 
    ok = True
    for i in range (0,len(l)):
        if abs(l[i]) == 10:
            print(l[i],end=" ")
            ok = False
    if ok == True:
        print("Nu exista!")
    print("")

def functie_3(l):
    design_functie_3()
    a = functie_citire_si_verificare_comanda(1,4)
    while a != 4:
        if a == 1:
            functie_3_1(l)
        if a == 2:
            functie_3_2(l)
        if a == 3:
            functie_3_3(l)
        design_functie_3()
        a = functie_citire_si_verificare_comanda(1,4)
    print("")
    design_meniu()
    
                                                                                                                         #
##########################################################################################################################
                                                                                                                         #
def afisare(l):
    for i in range(0,len(l)):
        print (l[i], end=" ")

def sortare(l):
    n = len(l)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if l[i].imag < l[j].imag:
                l[i],l[j] = l[j],l[i]
                                                                                                                         
def functie_4_1(l):
    poz1 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    poz2 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    suma = 0
    for i in range(poz1,poz2+1):
        suma += l[i]
    print("Suma numerelor din secventa este: ",suma)

def functie_4_2(l):
    poz1 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    poz2 = functie_citire_si_verificare_pozitie(0,len(l)-1)
    produs = 1
    for i in range(poz1,poz2+1):                                                                                                                # - Capitolul 4 
        produs *= l[i]
    print ("Produsul numerelor din subsecventa este: ", produs)

def functie_4_3(l):
    global copie
    copie = list(l)
    sortare(l)
    print("Lista a fost sortata descrescator!")
    afisare(l)
    print("")

def functie_4(l):
    design_functie_4()
    a = functie_citire_si_verificare_comanda(1,4)
    while a != 4:
        if a == 1:
            functie_4_1(l)
        if a == 2:
            functie_4_2(l)
        if a == 3:
            functie_4_3(l)
        design_functie_4()
        a = functie_citire_si_verificare_comanda(1,4)
    print("")
    design_meniu()
    
    
                                                                                                                         #
##########################################################################################################################
                                                                                                                         #
def prim(n):
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
    i = 0
    global copie
    copie = list(l)                         # oare trebuie facut caz daca nu exista vreun numar prim????
    while i < len(l):
        imag = int(l[i].real)
        if prim(imag) == 1:
            l.pop(i)
            i -= 1
        i += 1
    print("Au fost eliminate cu succes, numerele complexe a caror parte reala era numar prim!")

def functie_5_2_1(l,numar):
    i = 0
    global copie
    copie = list(l)
    while i < len(l):
        if abs(l[i]) < numar:                   # oare trebuie facut caz daca nu exista numere mai mici / egale / mai mari la functiile 5-2-1/2/3??
            l.pop(i)
            i -= 1
        i += 1

def functie_5_2_2(l,numar):
    i = 0
    global copie
    copie = list(l)
    while i < len(l):
        if abs(l[i]) == numar:                                                                                                                      # - Capitolul 5 
            l.pop(i)
            i -= 1
        i += 1

def functie_5_2_3(l,numar):
    i = 0
    global copie
    copie = list(l)
    while i < len(l):
        if abs(l[i]) > numar:
            l.pop(i)
            i -= 1
        i += 1

def functie_5_2(l):
    numar = functie_citire_numar_intreg()
    design_functie_5_2(numar)
    a = functie_citire_si_verificare_comanda(1,4)
    while a != 4:
        if a == 1:
            functie_5_2_1(l,numar)
            print("Au fost eliminate cu succes numerele cu modulul mai mic decat",numar)
        if a == 2:
            functie_5_2_2(l,numar)
            print("Au fost eliminate cu succes numerele cu modulul egal cu",numar)
        if a == 3:
            functie_5_2_3(l,numar)
            print("Au fost eliminate cu succes numerele cu modulul mai mare decat",numar)
        design_functie_5_2(numar)
        a = functie_citire_si_verificare_comanda(1,4)

def functie_5(l):
    design_functie_5()
    a = functie_citire_si_verificare_comanda(1,3)
    while a != 3:
        if a == 1:
            functie_5_1(l)
        if a == 2:
            functie_5_2(l)
        design_functie_5()
        a = functie_citire_si_verificare_comanda(1,3)
    print("")
    design_meniu()
                                                                                                                         #
##########################################################################################################################
                                                                                                                         #
def functie_6(l):
    lung1 = len (l)
    lung2 = len (copie)
    if lung2 == 0:
        print("Nu au fost facute operatii ce schimba lista!")
    else:
        if lung1 > lung2:
            lung2,lung1 = lung1, lung2                                                                                                                  # - Capitolul 6
        for i in range(0,lung2-lung1):
            l.pop()
        l = copie
        print("Lista a revenit la forma avuta inainte de ultima operatie!")
        print(l)
    design_meniu()
                                                                                                                         #
##########################################################################################################################
                                                                                                                         
def meniu():
    l = [1+2j,3+4j,1+2j,4+2j,5+6j,7+8j,8+6j,6+8j]
    design_meniu()
    comanda = functie_citire_si_verificare_comanda(1,7)
    print("")
    
    while comanda != 7:
        
        if comanda == 1:
            functie_1(l)
            
        if comanda == 2:
            functie_2(l)
            
        if comanda == 3:
            functie_3(l)
            
        if comanda == 4:
            functie_4(l)

        if comanda == 5:
            functie_5(l)
            
        if comanda == 6:
            functie_6(l)
        
        comanda = functie_citire_si_verificare_comanda(1,7)
        
    print("La revedere!")
    
    
meniu()
    
    
