import time
from functools import wraps

import sentry_sdk
from loguru import logger

logger.add(
    sink="logs/log_decorator.log", format="{time} {message} {file}", level="INFO"
)


def log_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Chamando a função {func.__name__} com args {args} e kwargs {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função {func.__name__} retornou {result}")
        except Exception as e:
            sentry_sdk.init(
                dsn="""https://5775b1c52c2d0ef0b75c860729536ece@o4507232464535552.
                    ingest.us.sentry.io/4507232467353600""",
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,
            )
            logger.exception(f"Exceção captura em {func.__name__} - {e} {func}")
            raise  # relança a execeção para não alterar o comportamento da função

    return wrapper


def log_etl(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f"""O tempo de execução da função {func.__name__} 
            foi de {end_time - start_time:.4f}"""
        )
        return result

    return wrapper
