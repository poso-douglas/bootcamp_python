lista = input("Insira uma sequencia de números separados por , ")
list = []
try:
    new_list = lista.split(",")
    for i in new_list:
        list.append(int(i))
    print(list)
except ValueError as e:
    print(f"Um dos elementos da lista não era do tipo inteiro -  {e}")