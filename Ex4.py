lista = [12, 342, 345, 2, 8, 7896]

def dig_pares(lista):
    par = 0
    for i in lista:  # Para cada elemento da lista, verifico se o tamanho da string é par, ao final retorno a quantidade de pares
        if len(str(i)) % 2 == 0: # len() retorna o tamanho de uma string ou array
            par += 1
    return par

print(dig_pares(lista))

