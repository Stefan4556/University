# Problema 9

def palindrom (n):
    nou=0
    while n != 0:
        cif = n % 10
        n = n // 10
        nou = nou * 10 + cif
    return nou

n = int (input ("Scrieti numarul al carui palindrom doriti sa-l aflati: "))

print ("Palindromul numarului", n, "este", palindrom (n))
        
