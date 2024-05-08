from statistics import stdev


def calcular_desvio_padrao_lista(lista: list[float]) -> float:
    """
    Recebe uma lista de float e retorna o desvio padrão da lista float
    """

    return stdev(lista)
