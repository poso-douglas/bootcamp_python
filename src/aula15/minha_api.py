import pandas as pd
from fastapi import FastAPI

app = FastAPI(debug=True)


@app.get("/")
async def hello_world():
    return "Minha primeira api"


@app.get("/get_data")
async def get_data():
    df = pd.read_csv("../aula9/data/vendas_1.csv")
    return df.to_json(orient="records")


@app.get("/get_data/{cod_venda}")
async def get_data(cod_venda: str):
    df = pd.read_csv("../aula9/data/vendas_1.csv")
    df1 = df[(df["Cod_Venda"] == int(cod_venda))]

    return df1.to_json(orient="records")
