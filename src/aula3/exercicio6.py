### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "O palmeiras não tem mundial, bi-rebaixado nao tem mundial"
new_texto = texto.replace(",","")
lista_palavras= new_texto.split()
dict_palavras = {}

for palavra in lista_palavras:
    if palavra in dict_palavras:
        dict_palavras[palavra] +=1
    else:
        dict_palavras[palavra] = 1

print(dict_palavras)