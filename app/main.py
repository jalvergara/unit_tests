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
    
    return a - b

def square(a: int) -> int:
    return a**2    


def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    return False


def find_max(numbers: list) -> int:
    numbers.sort()
    return numbers.pop()


def find_min(numbers: list) -> int:
    numbers.sort(reverse=True)
    return numbers.pop()


def find_mean(numbers: list) -> float:
    x = sum(numbers)
    y = len(numbers)
    if y == 0:
        raise ZeroDivisionError("Dont divide for zero")
    return x/y


def find_median(numbers: list) -> float:
    numbers.sort()
    longitud = len(numbers)
    medium = longitud // 2

    if longitud == 0:
        raise ZeroDivisionError

    if longitud % 2 == 0:
        median = (numbers[medium - 1] + numbers[medium]) / 2
    else:
        median = numbers[medium]

    return median

def find_mode(numbers: list) -> int:
    if numbers.__len__() == 0:
        raise RuntimeError("The list lenght must be > 0")
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    

    max_count = 0
    mode = None
    for number, count in frequency.items():
        if count > max_count:
            max_count = count
            mode = number
    return mode


def factorial(n: int) -> int:
    result = 1
    if n < 0: 
        raise ValueError("The factorial must be a natural value")
    if n == 0:
        return 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def reverse_string(string: str) -> str:
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


def list_sum(numbers: list) -> int:
    return sum(numbers)


def list_product(numbers: list) -> int:
    if numbers.__len__() == 0:
        return 0
    result = 1
    for number in numbers:
        result *= number
    return result