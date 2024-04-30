### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = ["maça", "abacaxi","morango","acerola","uva"]
cnt = 1

while cnt <= len(lista):
    print(lista[cnt])

    if lista[cnt] == "acerola":
        print("Condição de saida")
        break
    cnt +=1