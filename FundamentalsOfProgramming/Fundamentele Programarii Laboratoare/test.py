n = int(input("Dati nr de numere "))
s = 0
for i in range(n):
    a = int(input())
    if a % 2 == 0:
        s += a
print("Suma numerelor este ",s)
