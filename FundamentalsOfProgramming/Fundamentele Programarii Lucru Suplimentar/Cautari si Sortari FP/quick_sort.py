"""
    Cum functioneaza?
    Lista este impartita in 2 parti in functie de un pivot, in stanga pivotului vor ajunge elementele mai mici
    decat acesta, iar in dreapta elementele mai mari. 
    In cazul de fata pivotul ales este elemntul cel mai din stanga
"""
def partition(l,left,right):
    """
        Impartim valorile din sir:
            el mai mici decat pivot - pivot - elemente mai mari decat pivot
        
        Returneaza pozitia pivotului
        post: in st elem mai mici decat pivot
              in dr elem mai mari decat pivot
    """
    pivot = l[left]
    i = left
    j = right
    while i != j:
        while l[j] >= pivot and i<j:
            j = j - 1
        l[i] = l[j]
        while l[i] <= pivot and i<j:
            i = i + 1 
        l[j] = l[i]
    l[i] = pivot
    return i

def QuickSortRecursiv(l,left,right):
    """
        Sorteaza crecator/descrescator lista de elemente
        l - lista de nr
        returneaza lista sortata

        Analiza complexitatii:

            - Timp:
                Best case: pivotul este fix la mijloc, iar in stanga sunt elementele mai mici si in dreapta mai mari
                           T(n) = 2*T(n/2) + Teta(n) = Teta(n*log2(n))
                Worst case: elementele sunt in ordine inversa - Teta(n^2)
                Average case: Teta(n*log2(n))

            - Spatiu:
                Este un algoritm In-place, ne avand nevoie de memorie aditionala - Teta(1)
    """

    # impartim lista
    pos = partition(l,left,right)

    # ordonam partea stanga
    if left < pos - 1:
        QuickSortRecursiv(l,left,pos-1)
    
    # ordonam partea dreapta
    if right > pos + 1:
        QuickSortRecursiv(l,pos+1,right)

def test_quick_sort():

    l = [2,1,3,5,4,9]
    print("Before quick sort: ",l)
    QuickSortRecursiv(l,0,len(l)-1)
    print("After quick sort: ",l)

test_quick_sort()