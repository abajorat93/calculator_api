import string
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("operations.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_fractions(frac_str: (int or float or string)) -> (int or float):
    """Checks a number and returns to float type.

    Parameters
    ----------
    frac_str : int or float or string
        Number in int, float or string type.

    Returns
    -------
    float
        Fixed float type number.
    """

    if isinstance(frac_str, (int, float)):
        return frac_str

    if "/" not in frac_str:
        return float(frac_str)
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split("/")
        try:
            leading, num = num.split(" ")
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac


def sum(a: any, b: any) -> (int or float):
    """Gets two numbers, adds them, and returns the result.

    Parameters
    ----------
    a : any
        Number in int or float type.
    b : any
        Number in int or float type.

    Returns
    -------
    any
        Result of the sum.
    """

    sum_a = get_fractions(a)
    sum_b = get_fractions(b)
    logger.debug(f"get_sum: v1={sum_a}, v2={sum_b}")
    return np.sum([sum_a, sum_b])


def subtract(a: any, b: any) -> (int or float):
    """Gets two numbers, subtracts the second from the first,
    and returns the result.

    Parameters
    ----------
    a : any
        Number in int or float type.
    b : any
        Number in int or float type.

    Returns
    -------
    any
        Result of the substraction.
    """

    minuend = get_fractions(a)
    subtrahend = get_fractions(b)
    logger.debug(f"get_subtract: minuend={minuend}, subtrahend={subtrahend}")
    return minuend - subtrahend


def multiply(a: any, b: any) -> (int or float):
    """Gets two numbers, multiplies them, and returns the result.

    Parameters
    ----------
    a : any
        Number in int or float type.
    b : any
        Number in int or float type.

    Returns
    -------
    any
        Result of the multiplication.
    """

    multiplicand = get_fractions(a)
    multiplier = get_fractions(b)
    logger.debug(
        f"get_multiplication: multiplicand={multiplicand}, multiplier={multiplier}"
    )

    return multiplicand * multiplier


def divide(a: any, b: any) -> (int or float):
    """Gets two numbers, divide the first by the second,
    and returns the result.

    Parameters
    ----------
    a : any
        Number in int or float type.
    b : any
        Number in int or float type.

    Returns
    -------
    any
        Result of the division.
    """

    dividend = get_fractions(a)
    divider = get_fractions(b)
    logger.debug(f"get_division: dividend={dividend}, divider={divider}")

    try:
        return np.divide(dividend, divider)
    except ZeroDivisionError:
        return "Division by zero is not allowed!"
