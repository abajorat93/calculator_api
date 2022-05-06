from fastapi import FastAPI, Path, Query
from calculator import calculator as calc

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.


app = FastAPI()


@app.get("/sum/{v1}/{v2}")
async def sum(v1: int, v2: int):
    return {"resultado": int(calc.sum(v1, v2))}


@app.get("/substract/{v1}/{v2}")
async def substract(v1: float, v2: float):
    return {"resultado": calc.subtract(v1, v2)}


@app.get("/divide/{v1}/{v2}")
async def divide(v1: float, v2: float):
    if v2 == 0:
        return {"resultado": "can't divide with 0"}
    return {"resultado": calc.divide(v1, v2)}


@app.get("/multiply/{text}")
async def multiply(text: str):
    try:
        values = text.split("*")
        v1 = values[0]
        v2 = values[1]
        return {"resultado": calc.multiply(v1, v2)}
    except IndexError or ValueError:
        return {"resultado": "invalid multiplication string. Must be 'a*b'"}
