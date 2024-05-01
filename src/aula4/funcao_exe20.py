# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

def ordernar_chaves(entrada: dict) -> list:
    lista_ordenada: list = [key for key in entrada.keys()]
    retorno: list =sorted(lista_ordenada)

    print(retorno)

ordernar_chaves({"f": 1,"z": 1,"x": 1,"p": 1,"g": 1,"l": 1})