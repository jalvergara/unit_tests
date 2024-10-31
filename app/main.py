import pandas as pd
from typing import List

def add(a: int, b: int) -> int:
    """Function to add two numbers

    Parameters
    ----------
    a : int
        First number to add
    b : int
        Second number to add

    Returns
    -------
    int
        Sum of a and b
    """
    return a + b

def divide(a: int, b: int) -> float:
    """Function to divide two numbers

    Parameters
    ----------
    a : int
        Numerator
    b : int
        Denominator

    Returns
    -------
    float
        Result of a divided by b

    Raises
    ------
    ValueError
        If division by zero is attempted
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def validate_no_null_values(df: pd.DataFrame) -> bool:
    """Validates that a DataFrame has no null values

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to check for null values

    Returns
    -------
    bool
        True if no null values, False otherwise
    """
    return not df.isnull().values.any()

def db_query() -> str:
    """Mock function to simulate a database query

    Returns
    -------
    str
        Simulated query result
    """
    return "DATA: [1, 2, 3]"

def subtract(a: int, b: int) -> int:
    """Function to subtract two numbers

    Parameters
    ----------
    a : int
        Number to subtract from
    b : int
        Number to subtract

    Returns
    -------
    int
        Result of a - b
    """
    return a - b

def square(a: int) -> int:
    """Function to return the square of a number

    Parameters
    ----------
    a : int
        Number to square

    Returns
    -------
    int
        Square of a
    """
    return a * a

def is_even(x: int) -> bool:
    """Function to check if a number is even

    Parameters
    ----------
    x : int
        Number to check

    Returns
    -------
    bool
        True if x is even, False otherwise
    """
    return x % 2 == 0

def find_max(numbers: List[int]) -> int:
    """Function to find the maximum number in a list

    Parameters
    ----------
    numbers : list
        List of integers

    Returns
    -------
    int
        Maximum number in the list
    """
    return max(numbers)

def find_min(numbers: List[int]) -> int:
    """Function to find the minimum number in a list

    Parameters
    ----------
    numbers : list
        List of integers

    Returns
    -------
    int
        Minimum number in the list
    """
    return min(numbers)

def find_mean(numbers: List[int]) -> float:
    """Function to find the mean of a list of numbers

    Parameters
    ----------
    numbers : list
        List of integers

    Returns
    -------
    float
        Mean of the list
    """
    return sum(numbers) / len(numbers)

def find_median(numbers: List[int]) -> float:
    """Function to find the median of a list of numbers

    Parameters
    ----------
    numbers : list
        List of integers

    Returns
    -------
    float
        Median of the list
    """
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def find_mode(numbers: List[int]) -> int:
    """Function to find the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        List of integers

    Returns
    -------
    int
        Mode of the list
    """
    from collections import Counter
    counter = Counter(numbers)
    mode = counter.most_common(1)[0][0]
    return mode

def factorial(n: int) -> int:
    """Function to find the factorial of a number

    Parameters
    ----------
    n : int
        Number to compute factorial for

    Returns
    -------
    int
        Factorial of n
    """
    if n == 0:
        return 1
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
        True if n is prime, False otherwise
    """
    if n <= 1:
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
        Word to check

    Returns
    -------
    bool
        True if word is a palindrome, False otherwise
    """
    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Function to reverse a string

    Parameters
    ----------
    string : str
        String to reverse

    Returns
    -------
    str
        Reversed string
    """
    return string[::-1]

def list_sum(numbers: List[int]) -> int:
    """Function to calculate the sum of a list of numbers

    Parameters
    ----------
    numbers : list
        List of integers

    Returns
    -------
    int
        Sum of the list
    """
    return sum(numbers)

def list_product(numbers: List[int]) -> int:
    """Function to calculate the product of a list of numbers

    Parameters
    ----------
    numbers : list
        List of integers

    Returns
    -------
    int
        Product of the list
    """
    product = 1
    for number in numbers:
        product *= number
    return product
