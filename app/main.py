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



def subtract(a: int, b: int) -> int:
    # TODO: write function to substract two numbers
    return a - b

def square(a: int) -> int:
    # TODO: write function to square a number
    return a**2


def is_even(x: int) -> bool:
    # TODO: write function to check if a number is even
    return (x % 2 == 0) == True


def find_max(numbers: list) -> int:
    # TODO: write function to find the maximum number in a list
    return max(numbers)


def find_min(numbers: list) -> int:
    # TODO: write function to find the minimum number in a list
    return min(numbers)


def find_mean(numbers: list) -> float:
    # TODO: write function to find the mean of a list of numbers
    return sum(numbers) / len(numbers) if numbers else 0


def find_median(numbers: list) -> float:
    # TODO: write function to find the median of a list of numbers
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def find_mode(numbers):
    # TODO: write function to find the mode of a list of numbers
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    max_count = 0
    mode = None
    for num, freq in count.items():
        if freq > max_count:
            max_count = freq
            mode = num

    return mode


def factorial(n: int) -> int:
    # TODO: write function to find the factorial of a number
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def is_prime(n: int) -> bool:
    # TODO: write function to check if a number is prime
    if n <= 1:
        return False
    for i in range(2, n): 
        if n % i == 0: 
            return False
    return True


def is_palindrome(word: str) -> bool:
    # TODO: write function to check if a word is a palindrome
    return word == word[::-1]


def reverse_string(string: str) -> str:
    # TODO: write function to reverse a string
    return string[::-1]


def list_sum(numbers: list) -> int:
    # TODO: write function to sum a list of numbers
    return sum(numbers)


def list_product(numbers: list) -> int:
    # TODO: write function to multiply a list of numbers
    product = 1
    for number in numbers:
        product *= number
    return product
