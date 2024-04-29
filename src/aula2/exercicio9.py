# Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input("Insira a temperatura em graus Celsius "))
BASE_FAH=1.8
VALUE_TO_SUM=32

fahr = (celsius * BASE_FAH) + 32

print(f"A temperatura em fahrnheit é {fahr}")
