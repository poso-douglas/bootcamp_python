### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

lista = [10,55,12,21,88,41]
nova_lista = []
for item in lista:
    nova_lista.append(item/100)

nova_lista.sort()
print(nova_lista)