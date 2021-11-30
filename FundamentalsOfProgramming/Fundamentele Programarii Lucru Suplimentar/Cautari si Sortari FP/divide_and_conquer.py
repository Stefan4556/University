"""
    Cum functioneaza acest principiu?
        Pas1: Divide - se imparte problema in probleme mai mici
        Pas2: Conquer - se rezolva subproblemele recursiv
        Pas3: Combine - combinarea rezultatelor
    
    Aceasta metoda se poate aplica cand o problema P pe un set de date D poate fi rezolvata prin rezolvarea
aceleiasi probleme P pe un alt set de date Dprim mai mic decat dimensiunea lui D

    Algoritm general:
    def divideAndConquer(data):
        if size(data)<a:
            #solve the problem directly
            #base case
            return rez

        #decompose data into d1,d2,..,dk
        rez_1 = divideAndConquer(d1)
        rez_2 = divideAndConquer(d2)
        ...
        rez_k = divideAndConquer(dk)
        #combine the results
        return combine(rez_1,rez_2,...,rez_k)

"""
def findMax(l):
    """
        find the greatest element in the list
        l list of elements
        return max
        complexitate: Teta(n)
    """
    if len(l)==1:
        #base case
        return l[0]
    #divide into 2 of size n/2
    mid = len(l) // 2
    max1 = findMax(l[:mid])
    max2 = findMax(l[mid:])
    #combine the results
    if max1<max2:
        return max2
    return max1

print("Maximul din lista este",findMax([1,23,4,5,6,99]))

def power(x, k):
    """
        compute x^k
        x real number
        k integer number
        return x^k
        complexitate: Teta(log2(n))
    """
    if k==1:
        #base case
        return x
    #divide
    half = k//2
    aux = power(x, half)
    #conquer
    if k%2==0:
        return aux*aux
    else:
        return aux*aux*x

print("2 la puterea 10 este",power(2,10))
print("2 la puterea 11 este",power(2,11))