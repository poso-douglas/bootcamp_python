try:
    num1= float(input("Insira um número "))
    tipo =""

    if num1 == 0:
        tipo = "zero"
    elif num1  > 0:
        tipo = "positito"
    else:
        tipo = "negativo" 

    par = False

    if num1 % 2 == 0:
        par = True

    print(f"O número informado é {tipo} e {"par" if par else "impar"}")

except:
    print("Entrada invalida")
    
