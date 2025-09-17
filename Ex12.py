lista = [1, 2, 3, 3, 3, 4, 5]

def repet(lista):
    lista1 = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)

    comp = 0

    for j in lista1:
        if lista.count(j) > comp:
            comp = j

    return comp

print(repet(lista))