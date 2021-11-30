def functie_citire():
    l = []
    n = int(input ("Introduceti numarul de numere:"))
    for i in range(0,n):
        x = input()
        l.append(x)
    return l

def functie_prim(n):
    n = int(n)
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    d = 3
    while d*d <= n:
        if n % d == 0:
            return 0
        d += 2
    return 1

def functie_2(l): # afiseaza atat lungimea maxima a secventei formata doar din numere prime, cat si elementele din ea - Proprietatea 4
    n = len (l)
    i = 0
    lungime_curenta = 0
    lungime_maxima = 0
    caz_particular = True
    
    while i < n:
        
        if lungime_curenta == 0 and functie_prim(l[i]) == 1:
            pozitie_inceput = i
            
        if functie_prim(l[i]) == 1:
            lungime_curenta += 1
             
        else:
            
            if lungime_curenta > lungime_maxima:
                lungime_maxima = lungime_curenta
                pozitie_final = i-1
                pozitie_inceput_lungime_maxima = pozitie_inceput
                pozitie_final_lungime_maxima = pozitie_final
                caz_particular = False
            lungime_curenta = 0
        i += 1
        
    if lungime_curenta > lungime_maxima:
                lungime_maxima = lungime_curenta
                pozitie_final = i-1
                pozitie_inceput_lungime_maxima = pozitie_inceput
                pozitie_final_lungime_maxima = pozitie_final
                caz_particular = False

    if caz_particular == False:    
        print("Lungimea maxima a secventei este:", lungime_maxima)
        for i in range(pozitie_inceput_lungime_maxima,pozitie_final_lungime_maxima+1):
            print(l[i],end = " ")
    else:
        print("Nu exista!")
            

def functie_3(l):   # afiseaza atat lungimea maxima a unei secvente formata din numere a caror suma = 5, cat si elementele din ea - Proprietatea 13
    n = len(l)
    lungime_maxima = 0
    suma_curenta=0
    caz_particular = True

    for i in range(0,n):
        suma_curenta = int(l[i])        
        if suma_curenta == 5:
            lungime_curenta = 1
            if lungime_curenta > lungime_maxima:
                lungime_maxima = lungime_curenta
                pozitie_inceput_lungime_maxima = i
                pozitie_final_lungime_maxima = i
                caz_particular = False
        j = i + 1
        ok = 0
        while j < n and ok == 0:

            suma_curenta += int(l[j])
            if suma_curenta == 5:
                lungime_curenta = j-i+1
                if lungime_curenta > lungime_maxima:
                    lungime_maxima = lungime_curenta
                    pozitie_inceput_lungime_maxima = i
                    pozitie_final_lungime_maxima = j
                    caz_particular = False
            else:
                if suma_curenta > 5:
                    ok = 1
            j += 1
            
    if caz_particular == False:
        print("Lungimea maxima a secventei este:", lungime_maxima)
        for i in range(pozitie_inceput_lungime_maxima,pozitie_final_lungime_maxima+1):
            print(l[i],end =" ")
    else:
        print("Nu exista!")
            

def cmmdc(a,b):
    a = int(a)
    b = int(b)
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def functie_4(l):      #prop 3
    lungime_curenta = 0
    lungime_maxima = 0
    caz_particular = True
    n = len(l)
    i = 0
    
    while i < n-1:
        if cmmdc(l[i],l[i+1]) == 1 and lungime_curenta==0:
            lungime_curenta = 1
        if cmmdc(l[i],l[i+1]) == 1:
            lungime_curenta += 1
        else:
            if lungime_curenta > lungime_maxima:
                lungime_maxima = lungime_curenta
                pozitie_inceput_lungime_maxima = i - lungime_curenta + 1
                pozitie_final_lungime_maxima = i
                caz_particular = False
            lungime_curenta = 0
        i += 1
        
    if lungime_curenta > lungime_maxima:
        lungime_maxima = lungime_curenta
        pozitie_inceput_lungime_maxima = i - lungime_curenta + 1
        pozitie_final_lungime_maxima = i
        caz_particular = False
  
    if caz_particular == False:
        print("Lungimea maxima a secventei este:", lungime_maxima)
        for i in range(pozitie_inceput_lungime_maxima,pozitie_final_lungime_maxima+1):
            print(l[i], end=" ")
    else:
        print("Nu exista!")
        

def functie_exit():
    print ("La revedere!")
    
def meniu():
    print ("                        MENIU")
    print ("       Alegeti una din comenzile de mai jos:")
    print ("1) Citeste lista")
    print ("2) Afiseaza secventa de lungime maxima formata doar din numere prime")
    print ("3) Afiseaza secventa de lungime maxima formata doar din numere a caror suma este egala cu 5")
    print ("5) Afiseaza secventa de lungime maxima formata din numere consecutive care sunt prime intre ele")
    print ("4) Exit")
    
    a = int(input("Introduceti cifra din dreptul comenzii:"))
    
    ok_citire = 0
    l = []
    while a != 4:
        
        if a == 1:
            l = functie_citire()
            ok_citire = 1 # am marcat faptul ca am citit deja lista
            print ("Lista incarcata")
            a = int(input("Introduceti cifra din dreptul comenzii:"))

        if a == 2 and len(l) != 0:
            functie_2 (l)
            print()
            a = int(input("Introduceti cifra din dreptul comenzii:"))

        if a == 3 and len(l) != 0: 
            functie_3 (l)
            print()
            a = int(input("Introduceti cifra din dreptul comenzii:"))

        if a == 5 and len(l) != 0:
            functie_4(l)
            print()
            a = int(input("Introduceti cifra din dreptul comenzii:"))

        if len(l)==0 and a != 1:
            print("Cititi lista inainte de a scrie orice alta comanda!")
            a = int(input("Introduceti cifra din dreptul comenzii:"))
        
    functie_exit()

meniu()
    
    
