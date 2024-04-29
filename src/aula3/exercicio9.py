### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista1= [10,3,8,7,55,74,99,120]
result = [i for i in lista1 if i % 2 ==0]
result.sort()
print(result)