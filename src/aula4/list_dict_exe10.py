# Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

lista_valores: int = [10,15,44,66,85,12,77,51,1,2,99,78]
lista_par: int = [n for n in lista_valores if n % 2 == 0]
lista_impar: int = [n for n in lista_valores if n % 2 != 0] 

print(f"lista par - {lista_par} - lista impar - {lista_impar}")