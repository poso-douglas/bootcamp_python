# Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos: dict = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for i in produtos:
    if i["id"] == 2:
        i["preço"] = 1000

print(produtos)