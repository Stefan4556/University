"""
    Cum functioneaza?
        Lista este impartita in doua subsecvente egale si fiecare dintre acestea este sortata, dupa care se 
    interclaseaza
        Pentru fiecare subsecventa se aplica acelasi algoritm pana cand se ajunge la o subsecventa formata 
    dintr un singur element
"""

def merge(l,start,end,m):
    """
        Complexitate interclasare Teta(m+n) unde m este lungimea partii din stanga si n lung partii din dreapta
    """

    lung_st = m - start + 1
    lung_dr = end - m
    stanga = []
    dreapta = []

    for i in range(0,lung_st):
        stanga.append(l[start + i])
    
    for j in range(0,lung_dr):
        dreapta.append(l[j + m + 1])
    
    i = 0   # parcurgem stanga
    j = 0   # parcurgem dreapta
    k = start # pozitia de unde o sa incepem sa facem interclasarea

    while i < lung_st and j < lung_dr:
        if stanga[i] <= dreapta[j]:
            l[k] = stanga[i]
            i += 1
        else:
            l[k] = dreapta[j]
            j += 1
        
        k += 1
    
    while i < lung_st:

        l[k] = stanga[i]
        i += 1
        k += 1
    
    while j < lung_dr:
    
        l[k] = dreapta[j]
        j += 1
        k += 1
 
def MergeSort(l,start,end):
    """
        Sorteaza crecator/descrescator lista de elemente
        l - lista de nr
        returneaza lista sortata

        Analiza complexitatii:

            - Timp:
                Best case = Worst case = Average case = Teta(n*log2(n))

            - Spatiu:
                Este un algoritm Not-in-place, avand nevoie de memorie aditionala - Teta(n)
    """

    if start >= end:
        return
    m = (end + start - 1) // 2
    MergeSort(l,start,m)
    MergeSort(l,m+1,end)
    merge(l,start,end,m)

def test_merge_sort():
    
    l = [2,1,3,5,4,9]
    print("Before merge sort: ",l)
    MergeSort(l,0,len(l)-1)
    print("After merge sort: ",l)

test_merge_sort()