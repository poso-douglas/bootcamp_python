from decorador import log_func


@log_func
def soma(n1: int, n2: int) -> int:
    return n1 + n2


@log_func
def erro():
    raise ValueError("Erro intencional")


soma(10, 20)
soma(10, "5")
erro()
