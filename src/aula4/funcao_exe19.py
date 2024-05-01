# Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def soma_combinacoes(lista: list, numero: int) ->list:
    cnt: int = 1
    lista_retorno: list = []
    for i in lista[:-1]:
        for j in lista[cnt:]:
            if i + j == numero:
                lista_retorno.append([i,j])
        cnt += 1
    print(lista_retorno)

soma_combinacoes([5,5,3,2,1,4,7,6,5,8],10)