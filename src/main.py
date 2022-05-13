import logging
from fastapi import FastAPI
from .calculator import calculator as calc


# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem
# in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("logs_calculator.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream
app = FastAPI()


@app.get("/sum/{v1}/{v2}")
async def sum(v1: int, v2: int):
    result = int(calc.sum(v1, v2))
    logger.debug(f"'resultado': {result}")
    logger.info(f"'resultado': {result}")
    return {"resultado": result}


@app.get("/subtract/{v1}/{v2}")
async def subtract(v1: float, v2: float):
    result = int(calc.subtract(v1, v2))
    logger.debug(f"'resultado': {result}")
    logger.info(f"'resultado': {result}")
    return {"resultado": result}


@app.get("/divide/{v1}/{v2}")
async def divide(v1: float, v2: float):
    if v2 == 0 or v1 == 0:
        print("resultado: cannot divide with 0")
        logger.error("'resultado': 'cannot divide with 0'")
        return {"resultado": "can't divide with 0"}

    result = int(calc.divide(v1, v2))
    logger.debug(f"'resultado': {result}")
    logger.info(f"'resultado': {result}")
    return {"resultado": result}


@app.get("/multiply/{text}")
async def multiply(text: str):
    try:
        values = text.split("*")
        v1 = values[0]
        v2 = values[1]
        result = int(calc.multiply(v1, v2))
        logger.debug(f"'resultado': {result}")
        logger.info(f"'resultado': {result}")
        return {"resultado": result}
    except IndexError or ValueError:
        logger.exception("Invalid multiplication string. Must be 'a*b'")
        return {"resultado": "invalid multiplication string. Must be 'a*b'"}
