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
    """Function to subtract two numbers

    Parameters
    ----------
    a : int
        first digit to subtract
    b : int
        second digit to subtract

    Returns
    -------
    int
        a '-' b
    """
    return a - b

def square(a: int) -> int:
    """Function to square the number

    Parameters
    ----------
    a : int
        digit to square

    Returns
    -------
    int
        a '**' a
    """
    return a ** 2


def is_even(x: int) -> bool:
    """Function to know if is even a number

    Parameters
    ----------
    x : int
        digit to know if is even

    Returns
    -------
    bool
        x '%' 2 '==' 0
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the max number

    Parameters
    ----------
    numbers : list
        list to validate

    Returns
    -------
    int
        Max number of the list
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to find the min number

    Parameters
    ----------
    numbers : list
        list to validate

    Returns
    -------
    int
        Min number of the list
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Function to find the mean

    Parameters
    ----------
    numbers : list
        list to validate

    Returns
    -------
    float
        Mean of the list
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """Function to find the median

    Parameters
    ----------
    numbers : list
        list to validate

    Returns
    -------
    float
        Median of the list
    """
    if not numbers:
        raise ValueError("The list is empty.")
    
    numbers.sort()
    mid = len(numbers) // 2
    
    return numbers[mid] if len(numbers) % 2 else (numbers[mid - 1] + numbers[mid]) /2


def find_mode(numbers: list) -> int:
    """Function to find the mode

    Parameters
    ----------
    numbers : list
        list to validate

    Returns
    -------
    int
        Mode of the list
    """
    if not numbers:
        raise ValueError("The list is empty.")
    
    freq, max_count = {}, 0
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        max_count = max(max_count, freq[num])

    return [num for num in freq if freq[num] == max_count][0]


def factorial(n: int) -> int:
    """Function to calculate the factorial of a number.

    Parameters
    ----------
    n : int
        Number to calculate the factorial.

    Returns
    -------
    int
        Factorial of n.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n < 2 else n * factorial(n - 1)

def is_prime(n: int) -> bool:
    """Function to check if a number is prime.

    Parameters
    ----------
    n : int
        Number to check.

    Returns
    -------
    bool
        True if prime, False otherwise.
    """
    if n < 2:
        return False
    return all(n % i for i in range(2, int(n**0.5) + 1))

def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome.

    Parameters
    ----------
    word : str
        Word to check.

    Returns
    -------
    bool
        True if palindrome, False otherwise.
    """
    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Function to reverse a string.

    Parameters
    ----------
    string : str
        String to reverse.

    Returns
    -------
    str
        Reversed string.
    """
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Sum of all elements in the list.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers)

def list_product(numbers: list) -> int:
    """Function to multiply all elements in a list.

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Product of all elements in the list.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return 0 if not numbers else eval('*'.join(map(str, numbers)))
