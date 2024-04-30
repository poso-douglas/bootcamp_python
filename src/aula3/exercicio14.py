### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

limite_con = 5
tentativas = 1

while tentativas <= limite_con:
    print(f"tentativa de conexão {tentativas}")
    tentativas +=1
print("Limite de tentativas excedido!")