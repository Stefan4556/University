"""
    Functiile de cautare secventiala pentru o lista in care elementele nu sunt sortate
"""

def searchSeq(el,l):
    """
        Cautarea unui element intr o lista:
        el - elementul pe care l cautam
        l - lista in care cautam
        returnam o valoare diferita de -1 daca acesta s a gasit sau -1 daca nu exista

        Complexitate: Teta(n)
    """

    poz = -1
    for i in range(0,len(l)):

        if el == l[i]:

            poz = i

    return poz

def searchSucc(el,l):
    """
        Cautam pe el in l
        el - element
        l - lista in care cautam
        returneaza -1 sau pozitia pe care se gaseste elementul

        Complexitate:

            - Best Case - Teta(1)
            - Worst Case - Teta(n)
            - Average - T(n) = (1 + 2 + ... + n-1) / n apartine lui Teta(n)
            - Overall - O(n)
    """

    i = 0
    while i < len(l) and el != l[i]:
        i = i + 1
    
    if i < len(l):

        return i
    
    return -1

def test_cautare_secventiala():

    l = [3,4,5,1,2]
    print(searchSeq(5,l))
    print(searchSucc(5,l))

test_cautare_secventiala()
