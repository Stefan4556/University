def functie(l):
    """
        Programul returneaza 0 in momentul in care nu mai exista elemente in
    lista, daca mai exista acesta returneaza 1 daca este par sau 0 daca e impar
    pentru a putea sau nu fi contorizat
    """
    if len(l) == 0:
        return 0
    if l[0]%2 == 0:
        p = 1
    else:
        p = 0
    return functie(l[1:]) + p

def test_functie():

    assert functie([1,1,1]) == 0
    assert functie([2,2,2]) == 3
    assert functie([1,2,3,4]) == 2

test_functie()
print(functie([1,2,3,4]))

"""
    Legat de pb 5:
        As fi ales programarea dinamica:
            De ce?
                Pentru ca as fi generat ciurul lui Eratostene pana la valoarea
                lui n dupa care l-as parcurge si as incerca sa vad daca poate fi
                scris ca si suma de numere prime
"""
