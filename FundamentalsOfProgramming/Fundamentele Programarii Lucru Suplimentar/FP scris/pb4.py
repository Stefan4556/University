def divide_et_impera(lista,st,dr):

    if len(lista) == 0:

        return

    if st == dr:

        if lista[st] % 2 == 0:
            
            return 1
        
        return 0
    
    else:

        mijloc = (st + dr) // 2

        return divide_et_impera(lista,mijloc+1,dr) + divide_et_impera(lista,st,mijloc)

l = [1,2,3,4,5,6]
print(divide_et_impera(l,0,len(l)-1))