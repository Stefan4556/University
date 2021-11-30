"""
    Functiile de cautare secventiala pentru o lista in care elementele sunt sortate
"""

def searchSeq(el,l):    # algoritm gresit
    """
        Cautarea unui element intr o lista:
        el - elementul pe care l cautam
        l - lista in care cautam
        returnam pozitia elementului sau pozitia pe care acesta poate fi inserat

        Complexitate: Teta(n)
    """

    if len(l) == 0:
        return 0
    
    if el <= l[0]:
        return 0
    
    if el >= l[len(l)-1]:
        return len(l)
    
    poz = -1
    for i in range(0,len(l)):
        if l[i] < el:
            poz = i
    
    if poz == -1:
        return len(l)
    return poz

def searchSucc(el,l):
    """
        Cautam pe el in l
        el - element
        l - lista in care cautam
        returneaza pozitia pe care se afla elementul sau pozitia unde poate sa fie inserat daca nu exista

        Complexitate:

            - Best Case - Teta(1)
            - Worst Case - Teta(n)
            - Average - T(n) = (1 + 2 + ... + n-1) / n apartine lui Teta(n)
            - Overall - O(n)
    """
    if len(l) == 0:
        return 0
    if el <= l[0]:
        return 0
    if el >= l[len(l)-1]:
        return len(l)
    i = 0
    while i < len(l) and el > l[i]:
        i = i + 1
    return i

def test_cautare_secventiala():

    l = [3,6,9,12,15]
    print(searchSeq(8,l))
    print(searchSucc(8,l))

test_cautare_secventiala()