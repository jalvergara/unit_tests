""" main functions to explain unit testing"""

import pandas as pd


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
    # TODO: write function to substract two numbers
    pass

def square(a: int) -> int:
    # TODO: write function to square a number
    pass


def is_even(x: int) -> bool:
    # TODO: write function to check if a number is even
    pass


def find_max(numbers: list) -> int:
    # TODO: write function to find the maximum number in a list
    pass


def find_min(numbers: list) -> int:
    # TODO: write function to find the minimum number in a list
    pass


def find_mean(numbers: list) -> float:
    # TODO: write function to find the mean of a list of numbers
    pass


def find_median(numbers: list) -> float:
    # TODO: write function to find the median of a list of numbers
    pass


def find_mode(numbers: list) -> int:
    # TODO: write function to find the mode of a list of numbers
    pass


def factorial(n: int) -> int:
    # TODO: write function to find the factorial of a number
    pass


def is_prime(n: int) -> bool:
    # TODO: write function to check if a number is prime
    pass


def is_palindrome(word: str) -> bool:
    # TODO: write function to check if a word is a palindrome
    pass


def reverse_string(string: str) -> str:
    # TODO: write function to reverse a string
    pass


def list_sum(numbers: list) -> int:
    # TODO: write function to sum a list of numbers
    pass


def list_product(numbers: list) -> int:
    # TODO: write function to multiply a list of numbers
    pass
