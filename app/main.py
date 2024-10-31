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
    """Divides two numbers, handling division by zero

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

def validate_no_null_values(df: pd.DataFrame) -> bool:
    """Validates that there are no null values in the DataFrame

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
    """Mocked database query function

    Returns
    -------
    str
        mocked database query
    """
    return "DATA: [1, 2, 3]"

def subtract(a: int, b: int) -> int:
    """Subtracts two integers

    Parameters
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns
    -------
    int
        The result of subtracting b from a.
    """
    return a - b

def square(a: int) -> int:
    """Calculates the square of an integer

    Parameters
    ----------
    a : int
        The integer to square.

    Returns
    -------
    int
        The square of the input integer.
    """
    return a * a

def is_even(x: int) -> bool:
    """Checks if an integer is even

    Parameters
    ----------
    x : int
        The integer to check.

    Returns
    -------
    bool
        True if x is even, False otherwise.
    """
    return x % 2 == 0

def find_max(numbers: list) -> int:
    """Finds the maximum number in a list

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        The maximum number.
    """
    return max(numbers)

def find_min(numbers: list) -> int:
    """Finds the minimum number in a list

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        The minimum number.
    """
    return min(numbers)

def find_mean(numbers: list) -> float:
    """Calculates the mean of a list of numbers

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        The mean value.
    """
    return sum(numbers) / len(numbers)

def find_median(numbers: list) -> float:
    """Calculates the median of a list of numbers

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        The median value.
    """
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return numbers[mid] if n % 2 == 1 else (numbers[mid - 1] + numbers[mid]) / 2

def find_mode(numbers: list) -> int:
    """Finds the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        The mode value.
    """
    return max(set(numbers), key=numbers.count)

def factorial(n: int) -> int:
    """Calculates the factorial of a number

    Parameters
    ----------
    n : int
        The number for which factorial is to be calculated.

    Returns
    -------
    int
        The factorial of the number.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """Checks if a number is prime

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    bool
        True if prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(word: str) -> bool:
    """Checks if a word is a palindrome

    Parameters
    ----------
    word : str
        The word to check.

    Returns
    -------
    bool
        True if palindrome, False otherwise.
    """
    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Reverses a string

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
    """Sums a list of numbers

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        The sum of the numbers.
    """
    return sum(numbers)

def list_product(numbers: list) -> int:
    """Calculates the product of a list of numbers

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        The product of the numbers.
    """
    result = 1
    for number in numbers:
        result *= number
    return result
