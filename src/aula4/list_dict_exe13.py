estoque: dict = {
    "sofa": 10,
    "cadeira": 0,
    "travesseiro": -7,
    "mesa": 15
}

estoque_positivo: dict = {chave : valor for chave,valor in estoque.items() if valor >=0}

print(estoque_positivo)