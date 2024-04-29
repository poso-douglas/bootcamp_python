### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, 
#filtrar aqueles que têm um campo específico faltando
users = [{"nome":"Douglas", "idade":38,"endereco":"Rua A"},
         {"nome":"Poso", "endereco":"Rua A"},
         { "idade":38,"endereco":"Rua A"},
         { "idade":40,"endereco":"Rua A"}]

usuarios = [user for user in users if "nome" not in user]
print(usuarios)
