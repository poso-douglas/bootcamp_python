### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:
    idade = int(input("Informe sus idade "))
except ValueError as e:
    print("Informe apenas números")
    exit()

email = input("informe seu email ")

if len(email.split("@"))> 1:
    if idade >=18:
        if idade <=65:
            print("Dados de usuário válidos")
        else:
            print("Idade maior que 65 anos")
    else:
        print("Idade menor que 18 anos")
else:
    print("Email invalido")