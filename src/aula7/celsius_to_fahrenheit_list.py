def converter_celcius_to_fahrenheit_list(lista: list[float]) -> list[float]:
    """
    Recebe uma lista com as temperaturas em graus Celcius e retorna
    outra lista com as temperaturas em graus Fahrenheit
    """
    fahrenheit: list[float] = []
    for t in lista:
        fahrenheit.append((t * 9 / 5) + 32)

    return fahrenheit
