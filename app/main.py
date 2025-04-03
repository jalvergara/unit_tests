""" main functions to explain unit testing"""

import pandas as pd
import statistics
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
    """
    Function to computes the square of a given integer.

    Parameters
    ----------
    a : int
        Integer to be squared.

    Returns
    -------
    int
        a '**' 2 : The square of the input integer.
    """

    return a**2


def is_even(x: int) -> bool:

    """
    Determines whether a given integer is even.

    Parameters
    ----------
    x : int
        Integer to check.

    Returns
    -------
    bool: 
        True if the integer is even
        False otherwise.
    """

    return x % 2 == 0


def find_max(numbers: list) -> int:
    """
    Finds the maximum number in a given list of integers.

    Parameters
    ----------
    numbers : list
        A list of integers.

    Returns
    -------
    int:
        Maximum integer in the list.

    Raises
    ------
    ValueError
        If the list is empty or contains non-integer elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(num, (int)) for num in numbers):
        raise ValueError("All elements in the list must be integer.")

    return max(numbers)



def find_min(numbers: list) -> int:
    """
    Finds the minimum number in a given list of integers.

    Parameters
    ----------
    numbers : list
        A list of integers.

    Returns
    -------
    int:
        Minimum integer in the list.

    Raises
    ------
    ValueError
        If the list is empty or contains non-integer elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(num, (int)) for num in numbers):
        raise ValueError("All elements in the list must be integer.")

    return min(numbers)


def find_mean(numbers: list) -> float:
    """
    Calculates the mean (average) of a given list of numbers.

    Parameters
    ----------
    numbers : list
        A list containing integer values.

    Returns
    -------
    float
        The mean of the numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty or contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integer.")

    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """Calculate the median of a given list of numbers.

    Parameters
    ----------
    numbers : list
        A list containing integer values.

    Returns
    -------
    float
        The median of the numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty or contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integer.")

    return statistics.median(numbers)


def find_mode(numbers: list) -> int:
    """Calculate the mode of a given list of numbers.

    Parameters
    ----------
    numbers : list
        A list containing integer values.

    Returns
    -------
    float
        The mode of the numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty or contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(num, (int)) for num in numbers):
        raise ValueError("All elements in the list must be integer.")
    
    freq_counts = {num: numbers.count(num) for num in set(numbers)}
    
    if len(set(freq_counts.values())) == 1:
        raise ValueError("There is no mode in the list.")

    return statistics.mode(numbers)


def factorial(n: int) -> int:
    """Calculate the factorial of a given non-negative integer.

    Parameters
    ----------
    n : int
        A non-negative integer.

    Returns
    -------
    int
        The factorial of the given number.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    return math.factorial(n)


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.

    Raises
    ------
    ValueError
        If n is less than 2.
    """
    if n < 2:
        raise ValueError("n must be greater than or equal to 2.")

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome.

    Parameters
    ----------
    word : str
        The word to check.

    Returns
    -------
    bool
        True if the word is a palindrome, False otherwise.
    """
    return word.lower() == word.lower()[::-1]


def reverse_string(string: str) -> str:
    """Reverse the characters of a string.

    Parameters
    ----------
    string : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    return string[::-1]


def list_sum(numbers: list) -> int:
    """Calculate the sum of all numbers in a list.

    Parameters
    ----------
    numbers : list
        A list of integer values.

    Returns
    -------
    int
        The sum of the numbers in the list.

    Raises
    ------
    ValueError
        If the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integer.")

    return sum(numbers)


def list_product(numbers: list) -> int:
    """Calculate the product of all numbers in a list.

    Parameters
    ----------
    numbers : list
        A list of integer values.

    Returns
    -------
    int
        The product of the numbers in the list.

    Raises
    ------
    ValueError
        If the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integer.")

    product = 1
    for num in numbers:
        product *= num
    return product
