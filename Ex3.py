# Solução 1:
endereco = "1.1.1.1"
endereco_certo = ""
for i in endereco:
    if i == ".":
        endereco_certo += "[.]"
    else:
        endereco_certo += i
print(endereco_certo)

# Solução 2:

print(endereco.replace(".", "[.]"))