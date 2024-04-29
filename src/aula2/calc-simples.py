try:
    num1 = float(input("Insira o primeiro número "))
    num2 = float(input("Insira o segundo número "))
    ope = input("Insira a operação (+ - * /) ")

    if ope not in ("+","-","*","/"):
        print("Operador invalido!")

    else:
        try:
            resultado = 0

            if ope == '+' :
                resultado = num1 + num2

            elif ope == '-' :
                resultado = num1 - num2

            elif ope == '*' :
                resultado = num1 * num2

            elif ope == '/' :
                resultado = num1 / num2

            print(f"O resultado da operação {ope} = {resultado}")
            

        except ZeroDivisionError as e:
            print(f"Não é possível dividir por  - {e}")

except ValueError as e:
    print(f"Informe um valor flat ou inteiro - {e}")