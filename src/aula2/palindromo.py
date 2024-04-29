frase =input("Insira uma frase ")
if isinstance(frase,str):
    if frase == frase[::-1]:
        print("É um palindromo!")
        print(frase[::-1])
    else:
        print("Não é um palindromo")
else:
    print("Insira apenas texto")