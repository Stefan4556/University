"""
    Cum functioneaza? 
    Cauta elementul cel mai mic/mare si il pune pe prima pozitie
"""

def selection_sort(l):
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
        ind = i
        # cautam cel mai mic element din lista
        for j in range(i+1,len(l)):
            if l[j] < l[ind]:
                ind = j

        if i < ind: # inseamna ca s a gasit un element mai mic decat i
            l[i],l[ind] = l[ind],l[i] 

def test_selection_sort():

    l = [2,1,3,5,4,9]
    print("Before selection sort: ",l)
    selection_sort(l)
    print("After selection sort: ",l)

test_selection_sort()