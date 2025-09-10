lista = [1, 5, 33, 8, 77, 43, 124, 6, 8, 99]

def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def soma(lista):
    lista.sort()
    return lista[0] + lista[-1]

def soma_total(lista):
    return sum(lista)

def media(lista):
    return sum(lista) / len(lista)
