from loguru import logger

logger.add(sink="logs/captura.log", format="{time} - {message}", level="ERROR")


def minha_funcao():
    raise ValueError("Ocorreu um erro na sua aplicação!")


try:
    minha_funcao()
except Exception:
    logger.exception("Erro de execução.")
