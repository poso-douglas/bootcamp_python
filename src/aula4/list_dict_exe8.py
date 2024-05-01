# Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

lista_pessoas: list = [
    {"nome": "Douglas", "idade": 38, "estado_civel":"casado"},
    {"nome": "Bruno", "idade": 18, "estado_civel":"solteiro"},
    {"nome": "Andre", "idade": 58, "estado_civel":"casado"},
    {"nome": "Joana", "idade": 5, "estado_civel":"solteiro"},
]

sorted_list: list = sorted(lista_pessoas,key=lambda p: p["nome"])
print(sorted_list)