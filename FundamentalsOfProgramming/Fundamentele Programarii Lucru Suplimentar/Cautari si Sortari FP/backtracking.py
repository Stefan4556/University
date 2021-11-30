"""
    Cum functioneaza?
        Algoritmul genereal de descoperire al tuturor solutiilor unei probleme. E o tehnica genereala ce 
    trebuie adaptata pentru fiecare problema in parte, iar marele dezavantaj este faptul ca are timp de
    executie exponential.

    Algoritm general:

        - Recursiv:

    def backRec(x):
        el = first(x)   # generam o solutie candidat
        x.append(el)
        while el!=None:
            x[-1] = el
            if consistent(x):   # functia ce verifica daca are rost sa continuam pe ramura respectiva sau nu
                if solution(x):     # functia ce verifica daca candidatul e si solutie
                    outputSolution(x)       # functia ce se ocupa cu afisarea solutiei
                backRec(x[:])       # functia ce se ocupa cu realizarea pasului de backtrack
            el = next(x)        # adauga un nou element la candidatul curent
        
        - Iterativ:
    
    def backIter(dim):
        x=[-1] #candidate solution
        while len(x)>0:
            choosed = False
            while not choosed and x[-1]<dim-1:
                x[-1] = x[-1]+1 #increase the last component
                choosed = consistent(x, dim)
            if choosed:
                if solution(x, dim):
                    solutionFound(x, dim)
                x.append(-1) # expand candidate solution
            else:
                x = x[:-1] #go back one component

    Descrierea solutiei de backtracking:

        - solutie candidat: cum arata si din ce elemente e formata
        - conditie consistent: care este conditia de consistenta
        - conditie solutie: care este conditia pentru ca un candidat sa fie si solutie
"""

def isSet(cand):
    
    return len(set(cand)) == len(cand)

def backtracking(x,DIM):
    if len(x)==DIM:
        print (x)
        return #stop recursion
    x.append(0)
    for i in range(0,DIM):
        x[-1] = i
        if isSet(x):
            #continue only if x can conduct to a solution
            backtracking(x,DIM)
    x.pop()

backtracking([], 3)