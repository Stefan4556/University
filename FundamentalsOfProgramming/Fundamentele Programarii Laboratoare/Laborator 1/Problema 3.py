a = int(input("Primul numar este: "))
b = int(input("Al doilea numar este: "))
while b!=0:
    r=a%b
    a=b
    b=r
print(a)
