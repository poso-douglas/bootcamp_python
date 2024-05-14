import pandas as pd

df = pd.read_csv("../aula9/data/vendas_1.csv")
# json_return = []
# #print(json_return)

# test = df.to_json(orient="records")
# print (test)

# df1 = df[(df["Produto"]== "Notebook Gamer")]

produto = 8
df1 = df[(df["Cod_Venda"] == produto)]
print(df1)
