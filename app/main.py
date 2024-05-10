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
    """_summary_

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

def square(a: int) -> int:
    """
    Squares a number.

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



def is_even(x: int) -> bool:
    """
    Checks if a number is even.

    Parameters
    ----------
    x : int
        The number to be checked.

    Returns
    -------
    bool
        True if the number is even, False otherwise.
    """
    return x % 2 == 0



def find_max(numbers: list) -> int:
    """
    Finds the maximum number in a list.

    Parameters
    ----------
    numbers : list
        The list of numbers.

    Returns
    -------
    int
        The maximum number in the list.
    """
    if not numbers:  
        return None
    max_num = numbers[0]  
    for num in numbers:   
        if num > max_num:  
            max_num = num  
    return max_num



def find_min(numbers: list) -> int:
    """
    Finds the minimum number in a list.

    Parameters
    ----------
    numbers : list
        The list of numbers.

    Returns
    -------
    int
        The minimum number in the list.
    """
    if not numbers:  
        return None
    min_num = numbers[0]  
    for num in numbers:   
        if num < min_num:  
            min_num = num  
    return min_num



def find_mean(numbers: list) -> float:
    """
    Finds the mean of a list of numbers.

    Parameters
    ----------
    numbers : list
        The list of numbers.

    Returns
    -------
    float
        The mean of the list.
    """
    if not numbers:  # Si la lista está vacía, devuelve None
        return None
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """
    Finds the median of a list of numbers.

    Parameters
    ----------
    numbers : list
        The list of numbers.

    Returns
    -------
    float
        The median of the list.
    """
    if not numbers:  # Si la lista está vacía, devuelve None
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        return sorted_nums[n//2]


def find_mode(numbers: list) -> int:
    pass


def factorial(n: int) -> int:
    # TODO: write function to find the factorial of a number
    pass


def is_prime(n: int) -> bool:
    # TODO: write function to check if a number is prime
    pass


def is_palindrome(word: str) -> bool:
    # TODO: write function to check if a word is a palindrome
    pass


def reverse_string(string: str) -> str:
    # TODO: write function to reverse a string
    pass


def list_sum(numbers: list) -> int:
    # TODO: write function to sum a list of numbers
    pass


def list_product(numbers: list) -> int:
    # TODO: write function to multiply a list of numbers
    pass
