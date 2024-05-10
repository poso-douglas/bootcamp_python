from sys import stderr

from loguru import logger

logger.add(
    sink=stderr, format="{time} <y>{level}</y>  <r>{message}</r> {file}", level="INFO"
)

logger.add(
    sink="logs/dois_sinks.log",
    format="{time}, {level}, {message} ,{file}",
    level="ERROR",
)


logger.info("Log de informação")
logger.error("Log de erro")
