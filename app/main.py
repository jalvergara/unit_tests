""" main functions to explain unit testing"""

import pandas as pd
from collections import Counter
import math

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
    """Function to mock a database query"""
    return "DATA: [1, 2, 3]"

def subtract(a: int, b: int) -> int:
    """Function to subtract two numbers"""
    return a - b

def square(a: int) -> int:
    """Function to return the square of a number"""
    return a * a

def is_even(x: int) -> bool:
    """Check if a number is even"""
    return x % 2 == 0

def find_max(numbers: list) -> int:
    """Find the maximum number in a list"""
    return max(numbers)

def find_min(numbers: list) -> int:
    """Find the minimum number in a list"""
    return min(numbers)

def find_mean(numbers: list) -> float:
    """Calculate the mean of a list of numbers"""
    return sum(numbers) / len(numbers)

def find_median(numbers: list) -> float:
    """Calculate the median of a list of numbers"""
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] if n % 2 != 0 else (numbers[mid - 1] + numbers[mid]) / 2)

def find_mode(numbers: list) -> int:
    """Find the mode of a list of numbers"""
    count = Counter(numbers)
    return max(count, key=count.get)

def factorial(n: int) -> int:
    """Calculate the factorial of a number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)

def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome"""
    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Reverse a string"""
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Sum all numbers in a list"""
    return sum(numbers)

def list_product(numbers: list) -> int:
    """Multiply all numbers in a list"""
    product = 1
    for num in numbers:
        product *= num
    return product
