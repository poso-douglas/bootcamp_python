#Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal 
#e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome 
#e informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_CALC = 1000
nome = input("Insira seu nome ")
salario = float(input("Insira seu salário "))
bonus = float(input("Insira a porcentagem do bonus recebido "))

kpi = CONSTANTE_CALC + salario * bonus

print(f"Olá {nome}, o seu valor bônus foi de {int(kpi)}")
