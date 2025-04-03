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


# Daniel Contreras
def subtract(a: int, b: int) -> int:
    """
    Function to substract two numbers
    Parameterts
    ----------
    a : int
    first digit to substract
    b : int
    second digit to substract
    Returns
    -------
    int
    """
    return a - b


def square(a: int) -> int:
    """
    Function to square a number
    Parameters
    ----------
    a : int
    number to square
    Returns
    -------
    int
    """
    return a * a


def is_even(x: int) -> bool:
    """
    Function to check if a number is even
    Parameters
    ----------
    x : int
    number to check
    Returns
    -------
    bool
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
    """Function to find the minimun number in a list

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    int
        minimun number in the list
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
        mean of the list of numbers
    """
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """function to find the median of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    float
        median of the list of numbers
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2


def find_mode(numbers: list) -> int:
    """function to find the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    int
        mode of the list of numbers
    """
    if len(set(numbers)) == len(numbers):
        return "No hay números repetidos"
    else:
        return max(set(numbers), key=numbers.count)


def factorial(n: int) -> int:
    """function to find the factorial of a number

    Parameters
    ----------
    n : int
        number to find the factorial of

    Returns
    -------
    int
        factorial of the number
    """
    if n < 0:
        raise ValueError("El factorial no está definido para *.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """function to check if a number is prime

    Parameters
    ----------
    n : int
        number to check

    Returns
    -------
    bool
        True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """function to check if a word is a palindrome

    Parameters
    ----------
    word : str
        word to check

    Returns
    -------
    bool
        True if the word is a palindrome, False otherwise
    """
    word = word.lower().replace(" ", "")
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """function to reverse a string

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
    """function to sum a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    int
        sum of the list of numbers
    """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """function to multiply a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    int
        product of the list of numbers
    """
    product = 1
    for num in numbers:
        product *= num
    return product
