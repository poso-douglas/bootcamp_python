def filtrar_dados_acima_limite(lista: list[float], limit: float) -> list:
    """
    Recebe uma lista de valores float e um valor de limite float e retorna
    uma lista com os valores acima do valor de limite
    """
    lista_acima_limite = []
    for item in lista:
        if item > limit:
            lista_acima_limite.append(item)

    return lista_acima_limite
