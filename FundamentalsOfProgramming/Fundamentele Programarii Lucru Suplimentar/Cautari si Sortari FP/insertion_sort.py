"""
    Cum functioneaza?
    Porneste de pe o poztie i>=1 dupa care verfica valoarea ce se afla la pozitia respectiva cu elementele 
    din inaintea elementului curent pentru a determina pozitia unde trebuie inserat elementul nostru
"""

def insertionSort(l):
    """
        Sorteaza crecator/descrescator lista de elemente
        l - lista de nr
        returneaza lista sortata

        Analiza complexitatii:

            - Timp:
                Best Case: Teta(n) - lista sortata
                Worst Case: Teta(n^2) - lista sortata descrescator
                Average Case: Teta(n^2)
                Overall Case: O(n^2)
            
            - Spatiu:
                Este un algoritm In-place, ne avand nevoie de memorie aditionala - Teta(1)
    """
    
    for i in range(1,len(l)):
        ind = i - 1
        a = l[i]
        # inseram a in pozitia buna
        while ind >= 0 and a < l[ind]:
            l[ind + 1] = l[ind]
            ind = ind -1

        l[ind + 1] = a

def test_insertion_sort():

    l = [2,1,3,5,4,9]
    print("Before insertion sort: ",l)
    insertionSort(l)
    print("After insertion sort: ",l)

test_insertion_sort()