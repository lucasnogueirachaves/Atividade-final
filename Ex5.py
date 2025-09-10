meu_array = [1, 2, 3, 2, 1, 4, 10]
dicionario = {}

for i in meu_array:
    if i not in dicionario.keys():
        dicionario[i] = 1
    else:
        dicionario[i] += 1

print(dicionario)