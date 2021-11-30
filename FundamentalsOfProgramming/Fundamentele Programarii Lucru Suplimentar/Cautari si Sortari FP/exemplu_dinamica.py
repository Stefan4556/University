"""
        Gasirea subsecventei cu suma maxima. Dintr-o lista(secventa) data

    a = 1,-2,3,4,-5,-6,1,1,4,7,-4,3
    n = 12

                                Structura Solutiei Optime

    Construim doua siruri:

        S = <s0,s2,...,sn-1> - suma maxima
        L = <l0,l2,...,ln-1> - lungimea
    
    S - o lista ce retine sume, unde sk retine suma maxima dintr-o subsecventa care se termina <ai,...,ak>, 
        0<=i<=k, oricare ar fi k = 0,...,n-1
    
    L - lungimea secventei maxime care se termina in k(k-i+1, daca <ai,...,ak> e subsecventa cu suma maxima) 

    Definitia recursiva:

    s0 = a0; l0 = 1

    sk = max(s(k-1)+ak,ak)

    lk = { 1, sk = ak
         { l(k-1) + 1, altfel
    
    Testam:
        a = 1,-2,3,4,-5,-6,1,1,4,7,-4,3
        n = 12
        
"""

def suma_max(a):

    if len(a) == 0: # tratam cazul in care este vida
        print("Lista introdusa este vida!")
        return
    s = [a[0]]
    l = [1]
    for i in range(1,len(a)):

        if s[i-1] + a[i] >= a[i]:

            s.append(s[i-1]+a[i])
            l.append(l[-1] + 1)
        
        else:

            s.append(a[i])
            l.append(1)
    
    m = a[0]    # maxim
    k = [0]       # lista unde retinem indicii
    for i in range(0,len(s)):
        if s[i] > m:
            m = s[i]
            k = [i]
        elif m == s[i]:
            k.append(i)
    
    for elem in k:
        for i in range(elem - l[elem] + 1, elem + 1):
            print(a[i],end=" ")
        print("")

suma_max([-2,1,2,-1,1,-3,3])