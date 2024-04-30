### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop 
# até que não haja mais páginas.

total_paginas =10
cnt = 1
while cnt <= total_paginas:
    print(f"pagina_{cnt}")
    cnt +=1

