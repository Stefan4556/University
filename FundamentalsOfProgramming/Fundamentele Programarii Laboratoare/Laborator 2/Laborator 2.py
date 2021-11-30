
# Problema 12

n = int (input("Introduceti indicele numarului pe care vreti sa-l aflati: "))
contor = 0
if n <= 3:
    print(n)
else:
    nr=4
    contor=3
    while contor < n:
        p = 0
        copie = nr
        while copie % 2 == 0:
            copie = copie // 2           # incepem descompunerea in factori primi
            p += 1                      # p - puterea
                
        if p != 0:
            contor += 1
            if contor == n:
                print(2)
                
        d=3
        while copie != 1:
            p = 0
            while copie % d == 0:
                p += 1
                copie = copie // d
                    
            if p != 0:
                contor += 1
                if contor == n:
                    print(d)
                      
            d += 2
            
        nr += 1
    
            
                    
