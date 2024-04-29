# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
from math import pi

raio = float(input("Insira o raio do circulo "))
area = pi * (raio ** 2)
print(f"{area:.2f}")