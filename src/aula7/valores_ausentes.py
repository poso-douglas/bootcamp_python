def encontrar_valores_ausentes_sequencia(lista: list[int]) -> list[int]:
    """
    Recebe uma lista de inteiros e devolve outra lista com os valoes ausentes
    na lista de valores
    """
    valores_ausentes: list[int] = []
    for i in range(min(lista), max(lista) + 1):
        if i not in lista:
            valores_ausentes.append(i)

    return valores_ausentes
