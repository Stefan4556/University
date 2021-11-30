"""
                                Problema 10

    Se dă o listă de numere întregi a1,...an, determinați toate sub-secvențele cu lungime mai
mare decât 2 cu proprietatea că: numerele sunt în ordine crescătoare şi numerele
consecutive au cel puţin o cifră în comun.

"""

# Varianta 2 de rezolvare a problemei cea cu elementele luate random din multimea primita, problema rezumandu-se la o simpla problema de combinari

def verifica_ordonare_crescatoare(l):

    for i in range(0,len(l)-1):

        if l[i] >= l[i+1]:

            return False
    
    return True

def verifica_indici_cosn(l):

    for i in range(0,len(l)-1):
        if abs(l[i]-l[i+1]) != 1:
            return False
    return True

def verificare_suplimentara(l,lista):

    lista_poz = []

    for i in range(0,len(l)):

        for j in range(0,len(lista)):
            
            if lista[j] == l[i]:

                lista_poz.append(j)
                break
    
    return verifica_indici_cosn(lista_poz)

def verifica_cifre_comune_doua_numere(x,y):

    lista_x = []
    lista_y = []

    if x != 0:

        while x != 0:

            cif = x % 10

            if cif not in lista_x:
                lista_x.append(cif)
            
            x = x // 10
    
    else:

        lista_x.append(0)
    
    if y != 0:
    
        while y != 0:

            cif = y % 10

            if cif not in lista_y:
                lista_y.append(cif)
            
            y = y // 10
    
    else:

        lista_y.append(0)
    
    for el in lista_x:

        if el in lista_y:

            return True

    return False

def verifica_au_cifre_comune(l):

    for i in range(0,len(l)-1):

        if verifica_cifre_comune_doua_numere(l[i],l[i+1]) == False:

            return False
    
    return True

def consistent(l):

    if verifica_au_cifre_comune(l) == True and verifica_ordonare_crescatoare(l) == True:

        return True

    return False

def solution(l):

    if len(l) >= 3:

        return True
    
    return False

def outputSolution(candidate):

    print(candidate)

def BacktrackRecursiv(lista,candidate):     # varianta recursiva

    poz = 0
    candidate.append(lista[poz])
    while poz < len(lista):
        candidate[-1] = lista[poz]
        if consistent(candidate) == True and verificare_suplimentara(candidate,lista) == True:
            if solution(candidate) == True:
                outputSolution(candidate)
            candidate_copy = list(candidate)
            BacktrackRecursiv(lista,candidate_copy)
        poz += 1
        
BacktrackRecursiv([11,12,13,14,15],[])

print("-------------------------------------")

def BacktrackIterativ(lista):   # varianta iterativa
    
    candidate = [None]

    lista_pozitii = [-1]

    while len(candidate) > 0:
        
        choosed = False

        while choosed == False and lista_pozitii[-1] < len(lista) - 1:

            lista_pozitii[-1] = lista_pozitii[-1] + 1
            candidate[-1] = lista[lista_pozitii[-1]]
            choosed = consistent(candidate)
        
        if choosed == True:

            if solution(candidate) == True and verifica_indici_cosn(lista_pozitii) == True:

                outputSolution(candidate)
        
            lista_pozitii.append(-1)

            candidate.append(-1)
        
        else:

            lista_pozitii.pop()
            candidate.pop()

BacktrackIterativ([11,12,13,14,15])