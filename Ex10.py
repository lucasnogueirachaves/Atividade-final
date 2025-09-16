def func(entrada):
    comp = 0
    for letra in entrada:
        if letra == "b":
            comp += 1
        if comp > 0:
            if letra == "a":
                return False
    return True
            
print(func("ababababab"))