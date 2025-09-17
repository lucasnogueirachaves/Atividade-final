# Solução 1:
endereco = "1.1.1.1"
endereco_certo = ""
for i in endereco:  # Para cada caracter no endereço, verifica se é um . , se for adiciona [.] no endereço certo, senao adiciona o caracter
    if i == ".":
        endereco_certo += "[.]"
    else:
        endereco_certo += i
print(endereco_certo)

# Solução 2:

print(endereco.replace(".", "[.]")) # Replace troca o primeiro parametro pelo segundo na string