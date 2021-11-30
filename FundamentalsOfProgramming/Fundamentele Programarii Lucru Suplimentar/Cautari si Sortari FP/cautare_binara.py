"""
    Cautare binara - analiza complexitate:
        
        - Best Case: Teta(1) pt n = 1
        - Worst Case: Teta(log2(n))
        - Average Case: Teta(log2(n))
        - Overall Case: O(log2(n))
"""

def cautare_binara_recursiv(element,lista,stanga,dreapta):
    """
        Cautam elementul in lista
        element - cel pe care l cautam
        lista - o lsita de numere sortata
        stanga,dreapta - inceputul, respectiv sfarsitul zonei din lista in care cautam
        returneaza pozitia numarului, daca nu exista returneaza pozitia unde ar putea fi inserat
    """

    if stanga >= dreapta-1:
        return dreapta
        
    mijloc = (stanga+dreapta)//2

    if element <= lista[mijloc]:

        return cautare_binara_recursiv(element,lista,stanga,mijloc)

    else:

        return cautare_binara_recursiv(element,lista,mijloc,dreapta)

def cautare_binara_iterativ(element,lista):
    """
        Cautam elementul in lista
        element - cel pe care l cautam
        lista - o lsita de numere sortata
        returneaza pozitia numarului, daca nu exista returneaza pozitia unde ar putea fi inserat
    """
    if len(lista) == 0:
        return 0
    if element <= lista[0]:
        return 0
    if element >= lista[len(lista)-1]:
        return len(lista)
    dreapta = len(lista)
    stanga = 0
    while dreapta - stanga > 1:
        mijloc = (stanga+dreapta)//2
        if element <= lista[mijloc]:
            dreapta = mijloc
        else:
            stanga = mijloc
    
    return dreapta



def test_cautare_binara():

    lista = [1,2,3,4,5]
    print(cautare_binara_recursiv(2,lista,0,len(lista)-1))
    print(cautare_binara_iterativ(2,lista)) 

test_cautare_binara()