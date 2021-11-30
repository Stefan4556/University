"""
    Se poate folosi pentru a rezolva probleme de optimizare unde:
        - solutia e rezultatul unui sir de decizii
        - timp polinomial de executie
        - gaseste solutia optima intotdeauna
        - rezolva problema combinand sub solutii de la subprobleme
    Vezi Curs13 pag - 15, 16, 17
"""
def fiboDP(n):
    """
        Dynamic programming:
        DP(1) = DP(2) = 1
        DP(i) = DP(i-1) + DP(i-2)
        Complexitatea - Teta(n)
    """
    if n<= 2:
        return 1
    mem = [None] * (n)
    mem[0] = 1
    mem[1] = 1
    for i in range(2,n):
        mem[i] = mem[i-1] + mem[i-2]
    return mem[n-1] 

print(fiboDP(10))