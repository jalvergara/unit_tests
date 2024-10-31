""" main functions to explain unit testing"""

import pandas as pd
from math import factorial as math_factorial
from statistics import mean, median, mode

def add(a: int, b: int) -> int:
    """Function to add two numbers

    Parameters
    ----------
    a : int
        first digit to add
    b : int
        second digit to add

    Returns
    -------
    int
        a '+' b
    """
    return a + b


def divide(a: int, b: int) -> float:
    """_summary_

    Parameters
    ----------
    a : int
        first digit
    b : int
        second digit

    Returns
    -------
    float
        a divided by b

    Raises
    ------
    ValueError
        Zero division
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")

    return a / b


# Function to validate that a Pandas DataFrame has no null values
def validate_no_null_values(df: pd.DataFrame) -> bool:
    """_summary_

    Parameters
    ----------
    df : pd.DataFrame
        dataframe to validate

    Returns
    -------
    bool
        True if no null values, False otherwise
    """
    return not df.isnull().values.any()


def db_query() -> str:
    """function to mock a database query

    Returns
    -------
    str
        mocked database query
    """
    return "DATA: [1, 2, 3]"


# Alejandro Vergara
def subtract(a: int, b: int) -> int:
    return a - b

def square(a: int) -> int:
    return a * a


def is_even(x: int) -> bool:
    return x % 2 == 0


def find_max(numbers: list) -> int:
    return max(numbers)


def find_min(numbers: list) -> int:
    return min(numbers)


def find_mean(numbers: list) -> float:
    return mean(numbers)


def find_median(numbers: list) -> float:
    return median(numbers)


def find_mode(numbers: list) -> int:
    return mode(numbers)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("No está definido para números negativos")
    return math_factorial(n)

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def reverse_string(string: str) -> str:
    return string[::-1]


def list_sum(numbers: list) -> int:
    return sum(numbers)


def list_product(numbers: list) -> int:
    product = 1
    for num in numbers:
        product *= num
    return product
