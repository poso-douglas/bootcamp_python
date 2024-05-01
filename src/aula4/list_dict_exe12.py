# Dados dois dicionários, fundi-los em um único dicionário.

dict1: dict = {"nome": "Poso", "idade":25, "sexo":"M"}
dict2: dict = {"endereco": "rua a", "cor": "branca"}

dict1.update(dict2)
print(dict1)