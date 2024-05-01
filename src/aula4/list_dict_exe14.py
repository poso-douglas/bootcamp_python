# Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario: dict = {"a": 1,"b": 2, "c": 3}

lista_chave: list = list(dicionario.keys())
lista_valores: list = list(dicionario.values())

print(f"{lista_chave} - {lista_valores}")