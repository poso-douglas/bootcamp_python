### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_vendas ={}
for i in vendas:
    if i["categoria"] in total_vendas:
        total_vendas[i["categoria"]]+=int(i["valor"])
    else:
        total_vendas[i["categoria"]] = i["valor"]

print(total_vendas)