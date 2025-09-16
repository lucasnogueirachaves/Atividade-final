lista = [0, 2, 3, 4, 5, 6, 7, 8]

def num_falta(lista):
    lista.sort()
    comp = lista[0]
    for num in lista:
        if num - comp > 1:
            return num - 1
        comp = num
        
print(num_falta(lista))