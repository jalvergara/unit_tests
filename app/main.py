""" main functions to explain unit testing"""

import pandas as pd
from collections import Counter
from math import factorial as math_factorial



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



def subtract(a, b):
    """
    Subtract b from a.

    Parameters
    ----------
    a : int
        first digit
    b : int
        second digit

    Returns
    -------
    int
        a - b
    """
    return a - b


def square(a):
    """
    Calculate the square of a number.

    Parameters
    ----------
    a : int
        The number to be squared.

    Returns
    -------
    int
        The square of the input number.
    """
    return a * a


def is_even(a):
    """
    Check if a number is even.

    Parameters
    ----------
    a : int
        The number to check.

    Returns
    -------
    bool
        True if the number is even, False otherwise.
    """
    return a % 2 == 0


def find_max(lst):
    """
    Find the maximum value in a list.

    Parameters
    ----------
    lst : list of int
        The list of integers.

    Returns
    -------
    int or None
        The maximum value in the list, or None if the list is empty.
    """
    if len(lst) == 0:
        return None
    return max(lst)


def find_min(lst):
    """
    Find the minimum value in a list.

    Parameters
    ----------
    lst : list of int
        The list of integers.

    Returns
    -------
    int or None
        The minimum value in the list, or None if the list is empty.
    """
    if len(lst) == 0:
        return None
    return min(lst)


def find_mean(lst):
    """
    Calculate the mean (average) of a list of numbers.

    Parameters
    ----------
    lst : list of int
        The list of integers.

    Returns
    -------
    float or None
        The mean of the numbers in the list, or None if the list is empty.
    """
    if len(lst) == 0:
        return None
    return sum(lst) / len(lst)


def find_median(lst):
    """
    Calculate the median of a list of numbers.

    Parameters
    ----------
    lst : list of int
        The list of integers.

    Returns
    -------
    int or float or None
        The median of the numbers in the list, or None if the list is empty.
    """
    n = len(lst)
    if n == 0:
        return None
    sorted_lst = sorted(lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]


def find_mode(lst):
    """
    Find the mode(s) of a list of numbers.

    Parameters
    ----------
    lst : list of int
        The list of integers.

    Returns
    -------
    int or list of int or None
        The mode(s) of the numbers in the list, or None if the list is empty.
    """
    if len(lst) == 0:
        return None
    counter = {}
    max_count = 0
    modes = []
    for num in lst:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1
        if counter[num] > max_count:
            max_count = counter[num]
            modes = [num]
        elif counter[num] == max_count:
            modes.append(num)
    return modes[0] if len(modes) == 1 else modes


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The non-negative integer.

    Returns
    -------
    int
        The factorial of the input integer.
    
    Raises
    ------
    ValueError
        If the input is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Check if a number is prime.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Parameters
    ----------
    s : str
        The string to check.

    Returns
    -------
    bool
        True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]


def reverse_string(s):
    """
    Reverse a string.

    Parameters
    ----------
    s : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    return s[::-1]


def list_sum(lst):
    """
    Calculate the sum of elements in a list.

    Parameters
    ----------
    lst : list of int
        The list of integers.

    Returns
    -------
    int
        The sum of the numbers in the list.
    """
    return sum(lst)


def list_product(lst):
    """
    Calculate the product of elements in a list.

    Parameters
    ----------
    lst : list of int
        The list of integers.

    Returns
    -------
    int
        The product of the numbers in the list.
    """
    number = 1
    for num in lst:
        number *= num
    return number
