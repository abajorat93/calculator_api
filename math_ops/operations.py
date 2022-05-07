import logging
from mimetypes import init
import calculator as calc

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("operations.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Operations:
    def __init__(self) -> None:
        pass

    def get_sum(self, v1: any, v2: any) -> any:
        """Perform the sum of two values
        and return the result.

        Parameters
        ----------
        v1 : any
            Value 1
        v2 : any
            Value 2

        Returns
        -------
        any
            Sum result
        """

        logger.debug(f"get_sum: v1={v1}, v2={v2}")
        return calc.sum(v1, v2)

    def get_subtract(self, v1: any, v2: any) -> any:
        """Perform the subtraction of two values
        and return the result.

        Parameters
        ----------
        v1 : any
            Value 1
        v2 : any
            Value 2

        Returns
        -------
        any
            Subtraction result
        """
        logger.debug(f"get_subtract: v1={v1}, v2={v2}")
        return calc.subtract(v1, v2)

    def get_division(self, v1: any, v2: any) -> any:
        """Perform the division of two values
        and return the result.

        Parameters
        ----------
        v1 : any
            Value 1
        v2 : any
            Value 2

        Returns
        -------
        any
            Division result
        """
        try:
            logger.debug(f"get_division: v1={v1}, v2={v2}")
            result = v1 / v2
        except ZeroDivisionError:
            logger.exception("Tried to divide by zero")
        else:
            return result

    def get_multiplication(self, v1: any, v2: any) -> any:
        """Perform the multiplication of two values
        and return the result.

        Parameters
        ----------
        v1 : any
            Value 1
        v2 : any
            Value 2

        Returns
        -------
        any
            Multiplication result
        """
        logger.debug(f"get_multiplication: v1={v1}, v2={v2}")
        return calc.multiply(v1, v2)
