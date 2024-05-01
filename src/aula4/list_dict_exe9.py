# Dado um conjunto de números, calcular a média.
from statistics import mean

lista_numeros: int = [10,15,44,66,85,12,77,51,1,2,99,78]
media: float = mean(lista_numeros)

print(media)