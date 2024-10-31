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

# Manuel Gruezo
def subtract(a: int, b: int) -> int:
    """Function to subtract two numbers

    Parameters
    ----------
    a : int
        first number
    b : int
        second number

    Returns
    -------
    int
        result of a - b
    """
    return a - b


def square(a: int) -> int:
    """Function to square a number

    Parameters
    ----------
    a : int
        number to square

    Returns
    -------
    int
        result of a squared
    """
    return a * a


def is_even(x: int) -> bool:
    """Function to check if a number is even

    Parameters
    ----------
    x : int
        number to check

    Returns
    -------
    bool
        True if x is even, False otherwise
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    int
        maximum number in the list
    """
    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    int
        minimum number in the list
    """
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Function to find the mean of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    float
        mean of the numbers
    """
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    float
        median of the numbers
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
        list of numbers

    Returns
    -------
    int
        mode of the numbers
    """
    from collections import Counter
    count = Counter(numbers)
    return count.most_common(1)[0][0]


def factorial (n: int) -> int:
    """Function to find the factorial of a number iteratively

    Parameters
    ----------
    n : int
        number to find factorial of

    Returns
    -------
    int
        factorial of n
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Function to check if a number is prime

    Parameters
    ----------
    n : int
        number to check

    Returns
    -------
    bool
        True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome

    Parameters
    ----------
    word : str
        word to check

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
        list of numbers

    Returns
    -------
    int
        sum of the numbers
    """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """Function to multiply a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    int
        product of the numbers
    """
    product = 1
    for number in numbers:
        product *= number
    return product
