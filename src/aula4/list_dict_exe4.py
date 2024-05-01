# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(palavra: str) -> int:
    contagem: dict = {}
    for p in palavra:
        contagem["caracter"] = contagem.get("caracter",0) + 1

    return contagem

print(contar_caracteres("O Palmeiras não tem mundial!"))