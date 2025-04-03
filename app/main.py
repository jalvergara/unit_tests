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


# Gabriel Martinez

def subtract(a: int, b: int) -> int:
    """Subtracts two integers and returns the result."""
    return a - b

def square(a: int) -> int:
    """Returns the square of an integer."""
    return a ** 2

def is_even(x: int) -> bool:
    """Checks if an integer is even, returns True if even, False otherwise."""
    return x % 2 == 0

def find_max(numbers: list) -> int:
    """Returns the maximum number in a list of numbers."""
    return max(numbers)

def find_min(numbers: list) -> int:
    """Returns the minimum number in a list of numbers."""
    return min(numbers)

def find_mean(numbers: list) -> float:
    """Calculates and returns the mean (average) of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def find_median(numbers: list) -> float:
    """Calculates and returns the median of a list of numbers."""
    if not numbers:
        return 0.0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def find_mode(numbers: list) -> int:
    """Returns the mode (most frequent number) of a list of numbers."""
    if not numbers: 
        return None
    return max(set(numbers), key=numbers.count)

def factorial(n: int) -> int:

    """Calculates and returns the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n: int) -> bool:

    """Checks if an integer is prime, returns True if prime, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """Checks if a string is a palindrome, returns True if it is, False otherwise."""
    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Returns the reversed version of a string."""
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Returns the sum of all numbers in a list."""
    return sum(numbers)

def list_product(numbers: list) -> int:
    """Returns the product of all numbers in a list."""
    if not numbers:
        return 1
    product = 1
    for num in numbers:
        product *= num
    return product
