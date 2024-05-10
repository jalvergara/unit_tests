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


def subtract(a: int, b: int) -> int:
    """
    This function subtracts the second number (b) from the first number (a).
    
    Args:
        a (int): The first number.
        b (int): The second number to be subtracted.
        
    Returns:
        int: The result of subtracting b from a.
    """
    return a - b

def square(a: int) -> int:
    """
    This function squares a number.

    Args:
        a (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    return a * a


def is_even(x: int) -> bool:
    """
    This function checks if a number is even.

    Args:
        x (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """
    This function finds the maximum number in a list.

    Args:
        numbers (list): The list of numbers to search for the maximum.

    Returns:
        int: The maximum number found in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty")

    max_number = max(numbers)
    return max_number


def find_min(numbers: list) -> int:
    """
    This function finds the minimum number in a list.

    Args:
        numbers (list): The list of numbers to search for the minimum.

    Returns:
        int: The minimum number found in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty")

    min_number = min(numbers)
    return min_number


def find_mean(numbers: list) -> float:
    """
    Calculate the mean of a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The mean of the numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """
    Calculate the median of a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The median of the numbers.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]


def find_mode(numbers: list) -> int:
    """
    Calculate the mode of a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    int: The mode of the numbers.
    """
    if not numbers:
        return 0
    counter = Counter(numbers)
    max_count = max(counter.values())
    mode = [number for number, count in counter.items() if count == max_count]
    return mode[0] if len(mode) == 1 else mode


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): An integer.

    Returns:
    int: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Parameters:
    n (int): An integer.

    Returns:
    bool: True if the number is prime, False otherwise.
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
    """
    Check if a word is a palindrome.

    Parameters:
    word (str): A string.

    Returns:
    bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """
    Reverse a string.

    Parameters:
    string (str): A string.

    Returns:
    str: The reversed string.
    """
    return string[::-1]


def list_sum(numbers: list) -> int:
    """
    Sum a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    int: The sum of the numbers.
    """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """
    Multiply a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    int: The product of the numbers.
    """
    result = 1
    for num in numbers:
        result *= num
    return result
