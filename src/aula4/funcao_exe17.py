# Crie uma função que receba um número como argumento e retorne True se o número for primo e 
# False caso contrário

def verificar_se_numero_primo(numero: int) -> bool:
    if numero > 1:
        for i in range(2, (numero)):
            if numero % i == 0:
                print(f"{numero} não é primo")
                break
        else:
            print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")

verificar_se_numero_primo(37)