# Dada uma string, contar a frequência de cada caractere usando um dicionário.

string_entrada = "Sapo sapato lata"

frequencia: dict = {}

for i in string_entrada:
    if i in frequencia:
        frequencia[i] += 1
    else:
        frequencia[i] = 1

print(frequencia)
