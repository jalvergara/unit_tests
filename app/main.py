""" main functions to explain unit testing"""

import pandas as pd
from collections import Counter


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


# FUNCIONES IMPLEMENTADAS:

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
    return a - b


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
    return a * a


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
    return x % 2 == 0


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

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot find maximum of an empty list")
    return max(numbers)


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

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot find minimum of an empty list")
    return min(numbers)


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

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)


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

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate median of an empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]


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

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of an empty list")
    counter = Counter(numbers)
    return counter.most_common(1)[0][0]


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

    Raises
    ------
    ValueError
        If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


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
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


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

    Raises
    ------
    ValueError
        If the word is empty
    """
    if not word:
        raise ValueError("Cannot check palindrome for an empty string")
    return word == word[::-1]


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

    Raises
    ------
    ValueError
        If the string is empty
    """
    if not string:
        raise ValueError("Cannot reverse an empty string")
    return string[::-1]


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

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot sum an empty list")
    return sum(numbers)


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

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate product of an empty list")
    result = 1
    for num in numbers:
        result *= num
    return result