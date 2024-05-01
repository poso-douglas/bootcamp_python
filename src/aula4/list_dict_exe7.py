# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
lista_idades: list = [18,22,1,5,4,15,9,55,88,99,66,32,11,45]

def maioridade(idade: int) -> int:
    if idade >= 18:
        return idade
retorno_maioridade =filter(maioridade , lista_idades)

nova_lista = list(retorno_maioridade)
print(nova_lista)
