import glob

import pandas as pd


def ler_consolidar_json(path: str) -> pd.DataFrame:
    """
    Recebe uma path e retorna um pandas dataframe
    com todo o conteudo dos json deste path
    """
    path_lista = []
    lista_arquivos: list[pd.DataFrame] = glob.glob(f"{path}/*.json")
    for arquivo in lista_arquivos:
        path_lista.append(pd.read_json(arquivo))
    df = pd.concat(path_lista, ignore_index=True)

    return df


def calcular_total_venda(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe um dataframe pandas e calcula o total da venda
    """
    df["Total_Venda"] = df["Quantidade"] * df["Venda"]
    return df


def salvar_arquivo_csv_parquet(df: pd.DataFrame, tipo: list):
    """
    Recebe um dataframe pandas e uma lista com os tipos de arquivos
    que se deseja salvar o resultado. Opções são 'csv' e 'parquet'
    """
    for i in tipo:
        if i == "csv":
            df.to_csv("data/vendas.csv")
        if i == "parquet":
            df.to_parquet("data/vendas.parquet")


def executar_pipeline(path: str, tipo: list):
    """
    Executa todo o ETL - Carrega os dados, transforma
    e salva.
    """
    df: pd.DataFrame = ler_consolidar_json(path)
    df_calculado: pd.DataFrame = calcular_total_venda(df)
    salvar_arquivo_csv_parquet(df_calculado, tipo)


if __name__ == "__main__":
    print(
        salvar_arquivo_csv_parquet(
            calcular_total_venda(ler_consolidar_json("data")), ["csv", "parquet"]
        )
    )
