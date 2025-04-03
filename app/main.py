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


# Alejandro Vergara
def subtract(a: int, b: int) -> int:
    """Function to substract two numbers

    Parameters
    ----------
    a : int
        first digit to add
    b : int
        second digit to add

    Returns
    -------
    int
        a '-' b
    """
    return a - b


def square(a: int) -> int:
    """Function to square a number

    Parameters
    ----------
    a : int
        digit to square

    Returns
    -------
    int
        a^2
    """
    return a * a


def is_even(x: int) -> bool:
    """Function to check if a number is even

    Parameters
    ----------
    x : int
        digit to check

    Returns
    -------
    bool
        True if number is even, False if number is odd
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list

    Parameters
    ----------
    numbers : list
        number list

    Returns
    -------
    int
        the maximum number in a list
    """
    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list

    Parameters
    ----------
    numbers : list
        number list

    Returns
    -------
    int
        the minimum number in a list
    """
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Function to find the mean of a list of numbers

    Parameters
    ----------
    numbers : list
        number list

    Returns
    -------
    float
        the mean in a list of numbers
    """
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers

    Parameters
    ----------
    numbers : list
        number list

    Returns
    -------
    float
        median value
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        number list

    Returns
    -------
    int
        Mode of the numbers
    """
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]


def factorial(n: int) -> int:
    # TODO: write function to find the factorial of a number
    """Function to find the factorial of a number

    Parameters
    ----------
    n : int
        digit to find the factorial 

    Returns
    -------
    int
        n!
    """

    if n < 0: 
        return "Negative factorials are not allowed "
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Function to check if a number is prime

    Parameters
    ----------
    n : int
        Number to check

    Returns
    -------
    bool
        True if the number is prime, false if the number is not prime 
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False
    return True



def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome

    Parameters
    ----------
    word : str
        the word to check

    Returns
    -------
    bool
        True if the word is palidrome, false if the word is not palidrome 
    """
    word = word.lower().replace(" ", "")
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """Function to reverse a string

    Parameters
    ----------
    word : str
        string to reverse

    Returns
    -------
    str
        reversed string 
    """
    return string[::-1]


def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers

    Parameters
    ----------
    numbers : list

    Returns
    -------
    int
        sum of the numbers in the list
    """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """Function to multiply a list of numbers

    Parameters
    ----------
    numbers : list

    Returns
    -------
    int
        multiply of the numbers in the list
    """
    result = 1
    for num in numbers:
        result *= num
    return result
