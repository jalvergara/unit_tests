""" main functions to explain unit testing"""

from collections import Counter

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
    """Function to divide two numbers.

    Parameters
    ----------
    a : int
        Numerator.
    b : int
        Denominator.

    Returns
    -------
    float
        Result of a divided by b.

    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")

    return a / b


# Function to validate that a Pandas DataFrame has no null values
def validate_no_null_values(df: pd.DataFrame) -> bool:
    """Validate that a DataFrame has no null values.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to validate.

    Returns
    -------
    bool
        True if no null values, False otherwise.
    """
    return not df.isnull().values.any()


def db_query() -> str:
    """Function to mock a database query.

    Returns
    -------
    str
        Mocked database query.
    """
    return "DATA: [1, 2, 3]"


# Alejandro Vergara
def subtract(a: int, b: int) -> int:
    """Function to subtract two numbers.

    Parameters
    ----------
    a : int
        Minuend.
    b : int
        Subtrahend.

    Returns
    -------
    int
        Result of a minus b.
    """
    return a - b

def square(a: int) -> int:
    """Function to calculate the square of a number.

    Parameters
    ----------
    a : int
        Number to square.

    Returns
    -------
    int
        Square of the number.
    """
    return a * a

def is_even(x: int) -> bool:
    """Function to check if a number is even.

    Parameters
    ----------
    x : int
        Number to check.

    Returns
    -------
    bool
        True if the number is even, False otherwise.
    """
    return x % 2 == 0

def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Maximum number in the list.
    """
    return max(numbers)

def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Minimum number in the list.
    """
    return min(numbers)

def find_mean(numbers: list) -> float:
    """Function to calculate the mean of a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        Mean of the numbers.
    """
    return sum(numbers) / len(numbers)

def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        Median value.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Mode of the numbers.
    """
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]

def factorial(n: int) -> int:
    """Function to calculate the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        Non-negative integer.

    Returns
    -------
    int
        Factorial of n.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """Function to check if a number is prime.

    Parameters
    ----------
    n : int
        Number to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome.

    Parameters
    ----------
    word : str
        Word to check.

    Returns
    -------
    bool
        True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Function to reverse a string.

    Parameters
    ----------
    string : str
        String to reverse.

    Returns
    -------
    str
        Reversed string.
    """
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Sum of the numbers.
    """
    return sum(numbers)

def list_product(numbers: list) -> int:
    """Function to calculate the product of a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Product of the numbers.
    """
    result = 1
    for number in numbers:
        result *= number
    return result