# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

from datetime import datetime
data = input("Insira uma data no formato dd/mm/aaaa ")
new_date = datetime.strptime(data,'%d/%m/%Y')

print(f"year {new_date.year}")
print(f"month {new_date.month}")
print(f"year {new_date.day}")