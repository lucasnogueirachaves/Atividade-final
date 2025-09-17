meu_array = [1, 2, 3, 2, 1, 4, 10]
dicionario = {}

for i in meu_array:  # Para cada elemento da lista, se o elemento nao estiver nas chaves do dicionario, a chave i recebe 0 valor 1. se ja tiver nas chaves, soma mais 1 ao valor associado àquela chave
    if i not in dicionario.keys():
        dicionario[i] = 1
    else:
        dicionario[i] += 1

print(dicionario)