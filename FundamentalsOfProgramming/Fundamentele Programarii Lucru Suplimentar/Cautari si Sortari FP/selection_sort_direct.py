"""
    Sortarea basic pe care o stie toata lumea, cea cu 2 for-uri
"""

def directSelectionSort(l):
    """
        sorteaza elementele listei crescator/descrescator
        l - lista de nr

        Analiza complexitatii:
          
            - Timp:
                Best Case = Worst Case = Average Case - complexitate Teta(n^2)
            
            - Spatiu:
                Este un algoritm In-place, ne avand nevoie de memorie aditionala - Teta(1)
    """

    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]

def test_direct_selection_sort():

    l = [2,1,3,5,4,9]
    print("Before direct selection sort: ",l)
    directSelectionSort(l)
    print("After direct selection sort: ",l)

test_direct_selection_sort()
