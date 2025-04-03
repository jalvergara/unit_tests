""" main functions to explain unit testing"""

import pandas as pd
import math
from statistics import mean, median, mode
from typing import Union, List


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


def subtract(a: int, b: int) -> int:
    
    """Subtracts two numbers.

    Args:
        a: Minuend.
        b: Subtrahend.

    Returns:
        The result of a minus b.

    Examples:
        >>> subtract(5, 3)
        2
    """

    return a - b


def square(a: int) -> int:
    """Calculates the square of a number.

    Args:
        a: Number to square. Must be an integer or a float.

    Returns:
        The square of the input number.

    Examples:
        >>> square(4)
        16
    """
    return a ** 2


def is_even(x: int) -> bool:
    """Checks if a number is even.

    Args:
        x: Number to check.

    Returns:
        True if the number is even, False otherwise.

    Examples:
        >>> is_even(4)
        True
    """
    
    return x % 2 == 0
    

def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Finds the maximum value in a list.

    Args:
        numbers: List of numbers.

    Returns:
        The maximum value in the list.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> find_max([3, 1, 4, 2])
        4
    """
    if not numbers:
        raise ValueError("The list is empty.")
    
    return max(numbers)


def find_min(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Finds the minimum value in a list.

    Args:
        numbers: List of numbers.

    Returns:
        The minimum value in the list.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> find_min([3, 1, 4, 2])
        1
    """

    if not numbers:
        raise ValueError("The list is empty.")
    
    return min(numbers)


def find_mean(numbers: List[Union[int, float]]) -> float:
    """Calculates the arithmetic mean of a list.

    Args:
        numbers: List of numbers.

    Returns:
        The arithmetic mean.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> find_mean([1, 2, 3, 4])
        2.5
    """
    
    if not numbers:
        raise ValueError("The list is empty.")

    return mean(numbers)


def find_median(numbers: List[Union[int, float]]) -> float:
    """Calculates the median of a list.

    Args:
        numbers: List of numbers.

    Returns:
        The median value.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> find_median([1, 3, 2])
        2
    """
    
    if not numbers:
        raise ValueError("The list is empty.")

    return median(numbers)


def find_mode(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Finds the mode (most frequent value) of a list.

    Args:
        numbers: List of numbers.

    Returns:
        The mode of the list.

    Raises:
        ValueError: If the input list is empty.
        StatisticsError: If there is no unique mode.

    Examples:
        >>> find_mode([1, 2, 2, 3])
        2
    """
    
    if not numbers:
        raise ValueError("The list is empty.")

    return mode(numbers)


def factorial(n: int) -> int:
    """Calculates the factorial of a non-negative integer.

    Args:
        n: Non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.

    Examples:
        >>> factorial(5)
        120
    """

    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    return math.factorial(n)


def is_prime(n: int) -> bool:
    """Checks if a number is prime.

    Args:
        n: Integer to check.

    Returns:
        True if the number is prime, False otherwise.

    Notes:
        Negative numbers are not considered prime.

    Examples:
        >>> is_prime(7)
        True
    """

    if n < 0:
        raise ValueError("Negative numbers are not prime")
    
    if n <= 1:
        if n == 0 or n == 1:
            raise ValueError("0 and 1 are not prime numbers")
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    max_divisor = math.isqrt(n) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
            
    return True



def is_palindrome(word: str) -> bool:
    """Checks if a string is a palindrome (reads the same forwards and backwards).

    Args:
        word: String to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Raises:
        ValueError: If the input string is empty.
        TypeError: If the input is not a string.

    Examples:
        >>> is_palindrome("racecar")
        True
    """

    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    if not word:
        raise ValueError("The string is empty"
                         )
    normalized = word.lower().replace(" ", "")
    return normalized == normalized[::-1]



def reverse_string(string: str) -> str:
    """Reverses a string.

    Args:
        string: Input string.

    Returns:
        The reversed string.

    Examples:
        >>> reverse_string("hello")
        'olleh'
    """
    return string[::-1]


def list_sum(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the sum of a list of numbers.

    Args:
        numbers: List of numbers.

    Returns:
        The sum of all numbers in the list.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> list_sum([1, 2, 3])
        6
    """

    if not numbers:
        raise ValueError("The list is empty.")
    
    return sum(numbers)


def list_product(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the product of a list of numbers.

    Args:
        numbers: List of numbers.

    Returns:
        The product of all numbers in the list.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> list_product([2, 3, 4])
        24
    """

    if not numbers:
        raise ValueError("The list is empty.")
    
    return math.prod(numbers)