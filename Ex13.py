meu_array = [1, 2, 2, 3, 3, 4, 4, 4, 5, 7, 1]
dicionario = {}

for i in meu_array: # Para cada elemento da lista, crio uma chave elemento no dicionario que recebe o valor de elemento
    dicionario.update({i: i})

print(dicionario)