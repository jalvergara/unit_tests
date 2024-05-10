""" main functions to explain unit testing"""

import pandas as pd
import statistics


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
    """Function to subtract two numbers

    Parameters
    ----------
    a : int
        first digit to subtract
    b : int
        second digit to subtract

    Returns
    -------
    int
        a '-' b
    """
    return a - b


def square(a: int) -> int:
    """Function to squeare one number

    Parameters
    ----------
    a : int
        first digit to square

    Returns
    -------
    int
        a '**' 2
    """
    return a ** 2


def is_even(x: int) -> bool:
    """Function to even one number

    Parameters
    ----------
    x : int
        first digit provide

    Returns
    -------
    int
        x '%' 2
    """
    if (x % 2) == 0:
        return True
    else:
        return False


def find_max(numbers: list) -> int:
    """Function to find the max number of the list

    Parameters
    ----------
    numbers : list
        list of numbers provide

    Returns
    -------
    int
        'max' number of the list
    """
    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to find the min number of the list

    Parameters
    ----------
    numbers : list
        list of numbers provide

    Returns
    -------
    int
        'min' number of the list
    """
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Function to find the mean number of the list

    Parameters
    ----------
    numbers : list
        list of numbers provide

    Returns
    -------
    int
        'mean' number of the list provide
    """
    return statistics.mean(numbers)


def find_median(numbers: list) -> float:
    """Function to find the median number of the list

    Parameters
    ----------
    numbers : list
        list of numbers provide

    Returns
    -------
    int
        'median' number of the list provide
    """
    return statistics.median(numbers)


def find_mode(numbers: list) -> int:
    """Function to find the mode number of the list

    Parameters
    ----------
    numbers : list
        list of numbers provide

    Returns
    -------
    int
        'mode' number of the list provide
    """
    return statistics.mode(numbers)


def factorial(n: int) -> int:
    """Function to factorial one number

    Parameters
    ----------
    n : int
        first digit provide

    Returns
    -------
    int
        'factorial' result of the integer provide
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def is_prime(n: int) -> bool:
    """Function to check if a number is prime 

    Parameters
    ----------
    x : int
        first digit provide

    Returns
    -------
    int
        Iterate from 2 to n // 2
        If n is divisible by any number between
        2 and n / 2, it is not prime
    """

    if n > 1:
        for i in range(2, (n//2)+1):
            if (n % i) == 0:
                return False
            else:
                return True
    else:
        raise ValueError(n, "is not a valid number")


def is_palindrome(word: str) -> bool:
    """Function to check if a word is palindrome

    Parameters
    ----------
    word : str
        first string provide

    Returns
    -------
    string
        check if the word is 'palindrome' (the same in order and reversed)
    """
    if (word == word[::-1]):
        return True
    else:
        return False


def reverse_string(string: str) -> str:
    """Function reverse a string

    Parameters
    ----------
    word : str
        first string provide

    Returns
    -------
    string
         'reversed' string provide
        """    
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers provide

    Returns
    -------
    int
        the result of sum all the numbers in the list
    """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """Function to multiply a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers provide

    Returns
    -------
    int
        Make a cycle to multiply all the numbers in the list.
    """
    total = 1
    for i in numbers:
        total = total * i
    return total
