l=[1,2,3,4,5]
'''
for element in l:
    print(element)
    element = element**2
    print(element)

for i in range(0,len(l)): # range(0,5) rezulta 0,1,2,3,4,5
    print(l[i])
'''

while len(l) > 0:
    a= l.pop()
    if a < 2:
        a = -1
    elif a < 4:
        a=0
    else:
        a = a**2
    print (a)

print (l)

