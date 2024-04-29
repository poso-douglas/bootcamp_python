#Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal 
#e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome 
#e informando o valor do salário em comparação com o bônus recebido.

import re

CONSTANTE_CALC = 1000
nome = input("Insira seu nome ")
###########################VALIDAÇÕES DO NOME#####################################
## 1-) TEM CARACTER NUMÉRICOS NO NOME
if re.search(r'\d',nome):
    print("Você digitou números no campo nome")
    exit()
## 2-) SE NÃO DIGITOU NADA OU ENTÃO SOMENTE VAZIO
elif nome.isspace() or len(nome) ==0:
    print("Você não digitou o seu nome")
    exit()
############################- VALIDACÕES DO SALÁRIO -##############################
try:
    #1-)VALIDA O TIPO DE ENTRADA COMO FLOAT
    salario = float(input("Insira seu salário "))
    #2-)VALIDA SE O SALARIO É MAIOR QUE 0
    if salario <= 0:
        print('Informe um salário maior que 0')
        exit()
except ValueError as e:
    print(f"Digite um valor decimal - {e}")
    exit()
############################- VALIDACÕES DO BONUS -##############################
try:
    #1-)VALIDA O TIPO DE ENTRADA COMO FLOAT
    bonus = float(input("Insira a porcentagem do bonus recebido "))
    #2-)VALIDA SE O BONUS É MAIOR QUE 0
    if bonus <= 0:
        print('Informe um bonus maior que 0')
        exit()
except ValueError as e:
    print(f"Digite um valor decimal ")
    exit()
##################################################################################
kpi = CONSTANTE_CALC + (salario * (bonus/100))

print(f"Olá {nome}, o seu valor bônus foi de {kpi:.2f}")
