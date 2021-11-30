from domain_clienti import Client

def cmp_lista_de_liste(l1,l2,rev):
    """
        Acest comparator este realizat pentru cazul in care avem o lista de liste si dorim sa sortam lista de liste dupa elementul ce se afla pe pozitia 1 in lista curenta
    """

    if rev == False: # sortam crescator
        if l1[1] < l2[1]:

            return 1
        
        elif l1[1] == l2[1]:

            return 0
        
        else:

            return -1

    else:

        if l1[1] < l2[1]:

            return -1
        
        elif l1[1] == l2[1]:

            return 0
        
        else:

            return 1

def cmp_nume_clienti(c1,c2,rev):
    """
        Acest comparator este realizat pentru cazul in care dorim sa sortam o lista dupa numele unui client, acesta realizand comparatia intre 2 stringuri ce reprezinta 2 nume de clienti
    """

    if rev == False: # sortam crescator

        if c1.getNume() < c2.getNume():

            return 1
        
        elif c1.getNume() == c2.getNume():

            return 0
        
        else:

            return -1
    
    else:

        if c1.getNume() < c2.getNume():

            return -1
        
        elif c1.getNume() == c2.getNume():

            return 0
        
        else:

            return 1

def cmp_nume_nr_carti(l1,l2,rev):
    """
        Acest comparator este o combinatie intre cele 2 comparatoare de mai sus, acesta sortand o lista de liste dupa elementul din lista curenta de pe pozitia 1, iar daca acestea sunt egale, 
        sorteaza crescator dupa nume
    """

    if rev == False: # sortam crescator

        if l1[1] < l2[1]:

            return 1
        
        elif l1[1] > l2[1]:

            return -1
        
        else: # suntem pe cazul cand numarul de carti este egal

            if l1[0].getNume() < l2[0].getNume(): # numele sunt sortate crescator

                return 1
            
            elif l1[0].getNume() == l2[0].getNume():

                return 0
            
            else: # numele nu sunt sortate crescator
                
                return -1
    
    else:

        if l1[1] < l2[1]:

            return -1
        
        elif l1[1] > l2[1]:

            return 1
        
        else:

            if l1[0].getNume() < l2[0].getNume():

                return -1 # daca vrei sa se sorteze si numele crescator aici trb sa fie 1
            
            elif l1[0].getNume() == l2[0].getNume():

                return 0
            
            else:

                return 1 # daca vrei sa se sorteze si numele crescator aici trb sa fie -1

def BubbleSort(l,cmp=cmp_lista_de_liste,rev = False):
    """
        Sortarea cu bule, denumită uneori sortare de scufundare, este un algoritm simplu de sortare care parcurge în mod repetat lista, 
        compară elementele adiacente și le schimbă dacă acestea sunt în ordinea greșită. Trecerea prin listă se repetă până când lista este sortată.
    """

    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if cmp(l[j],l[j+1],rev) == -1:
                l[j+1],l[j] = l[j],l[j+1]
    
    return l

def ShellSort(l,cmp=cmp_nume_clienti,rev = False):
    """
        Shell sort este o generalizare a algoritmului insertion sort, doar ca in acest nu sunt deplasate elementele doar cu o pozitie, ci cu mai multe de o pozitie,
        aceasta valoare fiind diferita la fiecare iteratie, la un moment dat ajungandu-se chiar la valoarea 1
    """

    n = len(l)

    gap = n // 2

    while gap > 0:

        for i in range(gap,n):

            temp = l[i]

            j = i

            while j >= gap and cmp(l[j-gap],temp,rev) == -1:

                l[j] = l[j-gap]
                j -= gap
            
            l[j] = temp
        
        gap //= 2
    
    return l

def BubbleSortCopie(l,cmp1=cmp_lista_de_liste,cmp2=cmp_nume_clienti,rev=False):
    """
        Cerinta lab
    """

    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if cmp1(l[j],l[j+1],rev) == -1:
                l[j+1],l[j] = l[j],l[j+1]
            elif cmp1(l[j],l[j+1],rev) == 0: # intram pe cazul in care sunt egale dupa primul criteriu
                if cmp2(l[j][0],l[j+1][0],rev) == -1:
                    l[j+1],l[j] = l[j],l[j+1]

    return l

def Test_sortari():

    # testam Bubble Sort si Shell Sort cu cmp_lista_de_liste
    l = [[0,1],[1,2],[2,-3],[3,-4]]

    l = BubbleSort(l,cmp_lista_de_liste)
    assert l[0] == [3,-4]
    assert l[1] == [2,-3]
    assert l[2] == [0,1]
    assert l[3] == [1,2]

    l = BubbleSort(l,cmp_lista_de_liste,rev=True)
    assert l[3] == [3,-4]
    assert l[2] == [2,-3]
    assert l[1] == [0,1]
    assert l[0] == [1,2]

    l = ShellSort(l,cmp_lista_de_liste)
    assert l[0] == [3,-4]
    assert l[1] == [2,-3]
    assert l[2] == [0,1]
    assert l[3] == [1,2]

    l = ShellSort(l,cmp_lista_de_liste,rev=True)
    assert l[3] == [3,-4]
    assert l[2] == [2,-3]
    assert l[1] == [0,1]
    assert l[0] == [1,2]

    # testam Bubble Sort si Shell Sort cu cmp_nume_clienti
    l = []
    l.append(Client(1,"Salut",1231231231231))
    l.append(Client(2,"Hei",1231231231231))
    l.append(Client(3,"Abc",1231231231231))

    l = BubbleSort(l,cmp_nume_clienti)
    assert str(l[0]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert str(l[1]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert str(l[2]) == "Id: 1, Nume: Salut, CNP: 1231231231231"

    l = BubbleSort(l,cmp_nume_clienti,rev=True)
    assert str(l[2]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert str(l[1]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert str(l[0]) == "Id: 1, Nume: Salut, CNP: 1231231231231"

    l = ShellSort(l,cmp_nume_clienti)
    assert str(l[0]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert str(l[1]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert str(l[2]) == "Id: 1, Nume: Salut, CNP: 1231231231231"

    l = ShellSort(l,cmp_nume_clienti,rev=True)
    assert str(l[2]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert str(l[1]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert str(l[0]) == "Id: 1, Nume: Salut, CNP: 1231231231231"

    # testam Bubble Sort si Shell Sort cu cmp_nume_nr_carti
    l = []
    lista = []
    lista.append(Client(1,"Salut",1231231231231))
    lista.append(1)
    l.append(lista)

    lista = []
    lista.append(Client(2,"Hei",1231231231231))
    lista.append(1)
    l.append(lista)

    lista = []
    lista.append(Client(3,"Abc",1231231231231))
    lista.append(2)
    l.append(lista)

    l = BubbleSort(l,cmp_nume_nr_carti)
    assert str(l[0][0]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert l[0][1] == 1
    assert str(l[1][0]) == "Id: 1, Nume: Salut, CNP: 1231231231231"
    assert l[1][1] == 1
    assert str(l[2][0]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert l[2][1] == 2

    l = BubbleSort(l,cmp_nume_nr_carti,rev=True)
    assert str(l[1][0]) == "Id: 1, Nume: Salut, CNP: 1231231231231"
    assert l[1][1] == 1
    assert str(l[2][0]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert l[2][1] == 1
    assert str(l[0][0]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert l[0][1] == 2

    l = ShellSort(l,cmp_nume_nr_carti)
    assert str(l[0][0]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert l[0][1] == 1
    assert str(l[1][0]) == "Id: 1, Nume: Salut, CNP: 1231231231231"
    assert l[1][1] == 1
    assert str(l[2][0]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert l[2][1] == 2

    l = ShellSort(l,cmp_nume_nr_carti,rev=True)
    assert str(l[1][0]) == "Id: 1, Nume: Salut, CNP: 1231231231231"
    assert l[1][1] == 1
    assert str(l[2][0]) == "Id: 2, Nume: Hei, CNP: 1231231231231"
    assert l[2][1] == 1
    assert str(l[0][0]) == "Id: 3, Nume: Abc, CNP: 1231231231231"
    assert l[0][1] == 2

    # testam cmp_lista_de_liste
    assert cmp_lista_de_liste([1,2],[1,3],rev=False) == 1
    assert cmp_lista_de_liste([1,2],[2,2],rev=False) == 0
    assert cmp_lista_de_liste([1,3],[1,2],rev=False) == -1

    assert cmp_lista_de_liste([1,2],[1,3],rev=True) == -1
    assert cmp_lista_de_liste([1,2],[2,2],rev=True) == 0
    assert cmp_lista_de_liste([1,3],[1,2],rev=True) == 1

    # testam cmp_nume_clienti
    c1 = Client(1,"Stefan",1231231231231)
    c2 = Client(2,"Radu",1231231231232)
    c3 = Client(3,"Stefan",1231231231233)

    assert cmp_nume_clienti(c1,c2,rev=False) == -1
    assert cmp_nume_clienti(c1,c3,rev=False) == 0
    assert cmp_nume_clienti(c2,c1,rev=False) == 1

    assert cmp_nume_clienti(c1,c2,rev=False) == -1
    assert cmp_nume_clienti(c1,c3,rev=False) == 0
    assert cmp_nume_clienti(c2,c1,rev=False) == 1

    # testam cmp_nume_nr_carti

    l1 = [c1,1]
    l2 = [c2,2]

    assert cmp_nume_nr_carti(l1,l2,rev=False) == 1
    assert cmp_nume_nr_carti(l2,l1,rev=False) == -1
    assert cmp_nume_nr_carti(l2,[c3,2],rev=False) == 1
    assert cmp_nume_nr_carti(l1,[c3,1],rev=False) == 0
    assert cmp_nume_nr_carti([c3,2],l2,rev=False) == -1

    assert cmp_nume_nr_carti(l1,l2,rev=True) == -1
    assert cmp_nume_nr_carti(l2,l1,rev=True) == 1
    assert cmp_nume_nr_carti(l2,[c3,2],rev=True) == -1
    assert cmp_nume_nr_carti(l1,[c3,1],rev=True) == 0
    assert cmp_nume_nr_carti([c3,2],l2,rev=True) == 1

Test_sortari()

