import csv


def ler_csv(path: str) -> list[dict]:
    """
    Recebe o path do arquivo e devolve uma lista de dicionario
    com os registros do csv
    """

    with open(path, mode="r", encoding="utf-8") as arquivo:
        csv_file = list(csv.DictReader(arquivo))

    return csv_file


def calcular_vendas_categoria(lista: list) -> dict:
    """
    Recebe uma lista de dicionarios de vendas e retorna o
    calculo de vendas agrupado por categoria
    """

    new_dict: dict = {}
    for i in lista:
        if i.get("Categoria") not in new_dict:
            new_dict[i.get("Categoria")] = int(i.get("Quantidade")) * int(
                i.get("Venda")
            )
        else:
            new_dict[i.get("Categoria")] += int(i.get("Quantidade")) * int(
                i.get("Venda")
            )

    return new_dict


def processar_dados(lista: list[dict]) -> dict:
    """
    Recebe uma lista de dicionarios de venda e retorna
    um dicionario onde cada categoria é uma chave que
    contém uma lista de dicionarios de vendas referentes
    aquela categoria
    """

    new_dict: dict = {}
    for i in lista:
        if i.get("Categoria") not in new_dict:
            new_dict[i.get("Categoria")] = []

        new_dict[i.get("Categoria")].append(i)

    return new_dict
