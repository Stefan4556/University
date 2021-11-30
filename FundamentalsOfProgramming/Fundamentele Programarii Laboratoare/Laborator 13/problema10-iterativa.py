"""
                                Problema 10

    Se dă o listă de numere întregi a1,...an, determinați toate sub-secvențele cu lungime mai
mare decât 2 cu proprietatea că: numerele sunt în ordine crescătoare şi numerele
consecutive au cel puţin o cifră în comun.

"""

# Varianta nerecursiva - cea cu liste de cel putin 3 elemente

def first(poz,l):
    
    return [l[poz],l[poz+1],l[poz+2]]

def expand(candidat,urm_poz,l):

    if urm_poz < len(l):

        candidat.append(l[urm_poz])
        return True
    
    return False

def cond_consecutiv(candidat):

    for i in range(0,len(candidat)-1):

        if candidat[i] > candidat[i+1]:

            return False

    return True

def verifica_cifre_comun(nr1,nr2):

    l1 = []
    l2 = []

    if nr1 == 0:
        l1.append(0)

    if nr2 == 0:
        l2.append(0)
    
    while nr1 != 0:

        cif = nr1 % 10

        if cif not in l1:

            l1.append(cif)
        
        nr1 //= 10
    
    while nr2 != 0:

        cif = nr2 % 10

        if cif not in l2:

            l2.append(cif)
        
        nr2 //= 10
    
    for x in l1:

        if x in l2:

            return True

    return False

def conditie_cifre(candidat):

    for i in range(0,len(candidat)-1):

        if verifica_cifre_comun(candidat[i],candidat[i+1]) == False:

            return False
    
    return True

def cond_consistent(lista):

    if conditie_cifre(lista) == True and cond_consecutiv(lista)==True:

        return True

    return False

def backtrack(poz,l):

    poz += 1

    if poz >= len(l)-2:

        return False,poz

    return True,poz

def output_solution(candidat):

    print(candidat)

def problema(lista):

    poz = 0

    ok = 0

    poz2 = poz + 3 # cu acest poz2 parcurgem lista in continuare, iar cu ajutorul lui poz retinem de unde am inceput secventa curenta

    candidat = first(poz,lista)

    while True:

        while cond_consistent(candidat):

                output_solution(candidat)
                ok = 1

                if expand(candidat,poz2,lista) == False:
                    break

                poz2 += 1
        
        adevar, poz = backtrack(poz,lista)

        poz2 = poz + 3

        if adevar == False:
            
            if ok == 0:

                print("Nu au fost gasite solutii!")
            
            else:

                print("A terminat de generat!")

            return

        else:
        
            candidat = first(poz,lista)

def main():

    ok = False
    
    while ok == False:

        try:

            n = int(input("Introduceti numarul de elemente din lista: "))
            ok = True

        except ValueError:
            
            print("Date de intrare invalide!")
    
    lista = []

    for i in range(0,n):

        x = int(input())

        lista.append(x)

    if n < 3:

        print("Lista introdusa contine prea putine numere!")
        return
    
    problema(lista)

main()