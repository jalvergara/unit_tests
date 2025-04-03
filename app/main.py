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


# TODO: PENDING FUNCTIONS:

def subtract(a: int, b: int) -> int:
    """Function to subtract two numbers

    Parameters
    ----------
    a : int
        The number from which to subtract
    b : int
        The number to subtract

    Returns
    -------
    int
        The result of a - b
    """
    # TODO: write function to substract two numbers
    pass

def square(a: int) -> int:
    """Function to calculate the square of a number

    Parameters
    ----------
    a : int
        The number to square

    Returns
    -------
    int
        The square of a
    """
    # TODO: write function to square a number
    pass


def is_even(x: int) -> bool:
    """Function to check if a number is even

    Parameters
    ----------
    x : int
        The number to check

    Returns
    -------
    bool
        True if x is even, False otherwise
    """
    # TODO: write function to check if a number is even
    pass


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    int
        The maximum number in the list
    """
    # TODO: write function to find the maximum number in a list
    pass


def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    int
        The minimum number in the list
    """
    # TODO: write function to find the minimum number in a list
    pass


def find_mean(numbers: list) -> float:
    """Function to calculate the mean of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    float
        The mean of the numbers in the list
    """
    # TODO: write function to find the mean of a list of numbers
    pass


def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    float
        The median of the numbers in the list
    """
    # TODO: write function to find the median of a list of numbers
    pass


def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    int
        The mode of the numbers in the list
    """
    # TODO: write function to find the mode of a list of numbers
    pass


def factorial(n: int) -> int:
    """Function to calculate the factorial of a number

    Parameters
    ----------
    n : int
        The number to calculate the factorial of

    Returns
    -------
    int
        The factorial of n
    """
    # TODO: write function to find the factorial of a number
    pass


def is_prime(n: int) -> bool:
    """Function to check if a number is prime

    Parameters
    ----------
    n : int
        The number to check

    Returns
    -------
    bool
        True if n is prime, False otherwise
    """
    # TODO: write function to check if a number is prime
    pass


def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome

    Parameters
    ----------
    word : str
        The word to check

    Returns
    -------
    bool
        True if word is a palindrome, False otherwise
    """
    # TODO: write function to check if a word is a palindrome
    pass


def reverse_string(string: str) -> str:
    """Function to reverse a string

    Parameters
    ----------
    string : str
        The string to reverse

    Returns
    -------
    str
        The reversed string
    """
    # TODO: write function to reverse a string
    pass


def list_sum(numbers: list) -> int:
    """Function to calculate the sum of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    int
        The sum of the numbers in the list
    """
    # TODO: write function to sum a list of numbers
    pass


def list_product(numbers: list) -> int:
    """Function to calculate the product of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    int
        The product of the numbers in the list
    """
    # TODO: write function to multiply a list of numbers
    pass
