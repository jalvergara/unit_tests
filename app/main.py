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
        Result of a - b.
    """
    return a - b


def square(a: int) -> int:
    """Function to square a number.

    Parameters
    ----------
    a : int
        Number to square.

    Returns
    -------
    int
        Square of a.
    """
    return a * a


def is_even(x: int) -> bool:
    """Check if a number is even.

    Parameters
    ----------
    x : int
        Number to check.

    Returns
    -------
    bool
        True if x is even, False otherwise.
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Find the maximum number in a list.

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
    """Find the minimum number in a list.

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
    """Find the mean of a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        Mean of the numbers.
    """
    return sum(numbers) / len(numbers) if numbers else 0


def find_median(numbers: list) -> float:
    """Find the median of a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        Median of the numbers.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def find_mode(numbers: list) -> int:
    """Find the mode of a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Mode of the numbers.
    """
    return max(set(numbers), key=numbers.count)


def factorial(n: int) -> int:
    """Calculate the factorial of a number.

    Parameters
    ----------
    n : int
        Number to calculate the factorial for.

    Returns
    -------
    int
        Factorial of n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Parameters
    ----------
    n : int
        Number to check.

    Returns
    -------
    bool
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome.

    Parameters
    ----------
    word : str
        Word to check.

    Returns
    -------
    bool
        True if word is a palindrome, False otherwise.
    """
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """Reverse a string.

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
    """Sum a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers to sum.

    Returns
    -------
    int
        Sum of the numbers.
    """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """Multiply a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers to multiply.

    Returns
    -------
    int
        Product of the numbers.
    """
    product = 1
    for num in numbers:
        product *= num
    return product