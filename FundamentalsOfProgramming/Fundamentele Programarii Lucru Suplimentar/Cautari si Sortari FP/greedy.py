"""
    Cum functioneaza?
        Este o strategie pentru problemele de optimizare si este aplicabil acolo unde optimul global se poate
    afla selectand succesiv optime locale.Folosit în multe probleme practice care necesite selecția unei mulțimi de elemente care
    satisfac anumite condiții și realizează un optim.
        Greedy are complexitate polinomiala - O(n^2), unde n e numar de elemente din lista candidat C

    Structura Greedy:

    def greedy(c):

    Greedy algorithm
    c - a list of candidates
    return a list (B) the solution found (if exists) using the greedy
    strategy, None if the algorithm
    selectMostPromissing - a function that return the most promising
    candidate
    acceptable - a function that returns True if a candidate solution can be
    extended to a solution
    solution - verify if a given candidate is a solution

    b = [] #start with an empty set as a candidate solution
    while not solution(b) and c!=[]:
        #select the local optimum (the best candidate)
        candidate = selectMostPromissing(c)
        #remove the current candidate
        c.remove(candidate)
        #if the new extended candidate solution is acceptable
        if acceptable(b+[candidate]):
            b.append(candidate)

    if solution(b):
        return b
    #there is no solution
    return None
"""
def solution(b):
    """
        verify if a candidate solution is an actual solution
        basically verify if the coins conduct to the sum M
        b – candidate solution
    """
    sum = _computeSum(b)
    return sum==SUM

def _computeSum(b):
    """
    compute the payed amount with the current candidate
    return int, the payment
    b – candidate solution
    """
    sum = 0
    for coin in b:
        nrCoins = (SUM-sum) // coin
    #if this is in a candidate solution we need to use at least 1 coin
        if nrCoins==0: 
            nrCoins = 1
        sum += nrCoins*coin
    return sum

def acceptable(b):
    """
        verify if a candidate solution is valid
        basically verify if we are not over the sum M
    """
    sum = _computeSum(b)
    return sum<=SUM

def selectMostPromissing(c):
    """
        select the largest coin from the remaining
        c - candidate coins
        return a coin
    """
    return max(c)

def printSol(b):
    """
        Print the solution: NrCoinns1 * Coin1 + NrCoinns2 *
        Coin2 +...
    """
    solStr = ""
    sum = 0
    for coin in b:
        nrCoins = (SUM-sum) // coin
        solStr+=str(nrCoins)+"*"+str(coin)
        sum += nrCoins*coin
        if SUM-sum>0:solStr+=" + "
    print (solStr)

def greedy_monede(c):

    b = []
    while not solution(b) and c!=[]:
        
        candidate = selectMostPromissing(c)
        c.remove(candidate)
        if acceptable(b+[candidate]):
            b.append(candidate)
            
    if solution(b):
        printSol(b)
    return None

SUM = 80
c = [1,5,25]
greedy_monede(c)