#Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal 
#e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome 
#e informando o valor do salário em comparação com o bônus recebido.

import re

CONSTANTE_CALC = 1000
nome = input("Insira seu nome ")
while re.search(r'\d',nome) or nome.isspace() or len(nome) ==0:
    print("Você digitou números no campo nome")
    nome = input("Insira seu nome ")

salario = 0
while salario <=0:
    try:
        salario = float(input("Insira seu salário "))
        if salario <= 0:
            print('Informe um salário maior que 0')
    except ValueError as e:
        print(f"Digite um valor decimal - {e}")
        salario = 0

bonus =0
while bonus <= 0:
    try:
        bonus = float(input("Insira a porcentagem do bonus recebido "))
        if bonus <= 0:
            print('Informe um bonus maior que 0')
    except ValueError as e:
        print(f"Digite um valor decimal ")
        bonus = 0
##################################################################################
kpi = CONSTANTE_CALC + (salario * (bonus/100))

print(f"Olá {nome}, o seu valor bônus foi de {kpi:.2f}")
