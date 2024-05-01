# Adicionar type hint

import re
import json

def cadastro_bonus(nome: str, salario: float, bonus: float) -> float:
    CONSTANTE_CALC: float = 1000
    while re.search(r'\d',nome) or nome.isspace() or len(nome) ==0:
        print("Você digitou números no campo nome")
    while salario <=0:
        try:
            if salario <= 0:
                print('Informe um salário maior que 0')
        except ValueError as e:
            print(f"Digite um valor decimal - {e}")
            salario = 0

    while bonus <= 0:
        try:
            if bonus <= 0:
                print('Informe um bonus maior que 0')
        except ValueError as e:
            print(f"Digite um valor decimal ")
            bonus = 0
    ##################################################################################
    kpi: float = CONSTANTE_CALC + (salario * (bonus/100))
    dict_retorno = {
        "nome":nome,
        "salario":salario,
        "bonus":bonus,
        "kpi":f"{kpi:.2f}"
    }

    dict_json = json.dumps(dict_retorno)
    with open(file="cadastro.json",mode="w",encoding="utf-8") as json_write:
        json_write.write(dict_json)

    print(f"Olá {nome}, o seu valor bônus foi de {kpi:.2f}")
    print(dict_retorno)


cadastro_bonus("Joao",17.70,8)