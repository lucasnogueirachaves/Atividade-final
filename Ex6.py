array = [1, 2, 2, 1, 3, 3, 4, 5, 5, 6, 6]

for i in array: # Para cada elemento do array, conta a quantidade de vezes q ele aparece com count(), se aparecer só uma vez, printa o elemento
    if array.count(i) == 1:
        print(f"O elemento {i} aparece apenas uma vez")
