n = int(input("Valoarea numarului este:"))
ok = 1
for i in range (2,n-1):
    if n%i == 0:
        ok = 0
if ok == 1:
    print("Prim")
else:
    print("Nu e prim")
