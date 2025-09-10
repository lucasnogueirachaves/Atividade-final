lista = [12, 342, 345, 2, 8, 7896]

def dig_pares(lista):
    par = 0
    for i in lista:
        if len(str(i)) % 2 == 0:
            par += 1
    return par

print(dig_pares(lista))

