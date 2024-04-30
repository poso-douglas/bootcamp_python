### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero = 0
intervalo = [1,5,10]
while numero not in intervalo:
    numero = int(input("Insira um número "))
    print("Informe os números 1,5 ou 10 para sair")