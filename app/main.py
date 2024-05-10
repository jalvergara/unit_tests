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


# Emmanuel's functions
def subtract(a: int, b: int) -> int:
    return a - b

def square(a: int) -> int:
    a = a * a
    return a


def is_even(x: int) -> bool:
    return x % 2 == 0



def find_max(numbers: list) -> int:
    return max(numbers)


def find_min(numbers: list) -> int:
    return min(numbers)


def find_mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """_summary_
    Parameters 
    ----------
    numbers : list
        list of numbers
        Returns
        -------
        float
            median of the list
            """
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]


def find_mode(numbers: list) -> int:
    """_summary_
    Parameters
    ----------
    numbers : list
        list of numbers
        Returns
        -------
        int
            mode of the list
            """
    return max(set(numbers), key=numbers.count)


def factorial(n: int) -> int:
    """_summary_
    Parameters
    ----------
    n : int
        number to find factorial
        Returns
        -------
        int
            factorial of n
            """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """_summary_
    Parameters
    ----------
    n : int
        number to check if prime
        Returns
        -------
        bool
            True if prime, False otherwise
            """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """_summary_
    Parameters
    ----------
    word : str
        word to check if palindrome
        Returns
        -------
        bool
            True if palindrome, False otherwise
            """
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """_summary_
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
    """_summary_
    Parameters
    ----------
    numbers : list
        list of numbers
        Returns
        -------
        int
            sum of the list
            """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """_summary_
    Parameters
    ----------
    numbers : list
        list of numbers
        Returns
        -------
        int
            product of the list
            """
    result = 1
    for number in numbers:
        result *= number
    return result
