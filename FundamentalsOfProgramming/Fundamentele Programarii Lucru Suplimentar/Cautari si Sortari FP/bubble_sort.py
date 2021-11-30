"""
    Cum functioneaza?
    Compara elementele consecutive, iar daca nu sunt in ordinea dorita le interschimba
    Acest proces continua pana cand nu mai avem ce elemente sa schimbam
    Sorteaza de la dreapta la stanga oarecum(duce elem max/min pe ultima poz si tot asa)
"""

def BubbleSort(l):
    """
        Sorteaza crecator/descrescator lista de elemente
        l - lista de nr
        returneaza lista sortata

        Analiza complexitatii:

            - Timp:
                Best case: Teta(n^2) - lista e sortata
                Worst case: Teta(n^2) - lista e sortata descrescator
                Average case: Teta(n^2)
                Overall case: O(n^2)

            - Spatiu:
                Este un algoritm In-place, ne avand nevoie de memorie aditionala - Teta(1)
    """

    for i in range(1,len(l)):
        for j in range(0,len(l)-i):
            if l[j+1] < l[j]:
                l[j],l[j+1] = l[j+1],l[j]

def test_bubble_sort():
    
    l = [2,1,3,5,4,9]
    print("Before bubble sort: ",l)
    BubbleSort(l)
    print("After bubble sort: ",l)

test_bubble_sort()