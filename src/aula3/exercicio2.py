### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temp = 10
if temp >= 100:
    print("Temperatura alta")
elif temp > 30:
    print("Temperatura normal")
else:
    print("Temperartura baixa")