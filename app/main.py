""" main functions to explain unit testing"""

import pandas as pd
from typing import List, Union

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
    """Function to square a number
    parameters
    ----------  
    a : int
        number to square
    Returns

    """
    if a == 0:
        return 1
    else:
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
        True if even, False otherwise
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list
    parameters
    ----------      
    numbers : list
        list of numbers
    returns
    ------- 
    int
        maximum number in the list
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List must contain only numbers")
    
    max_value = numbers[0] 
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_min(numbers: list) -> int:
    if not numbers:
        raise ValueError("Cannot find minimum of empty list")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("list must contain only numbers")
    return min(numbers)



def find_mean(numbers: list) -> float:
    """Function to find the mean of a list of numbers
    parameters  
    ----------
    numbers : list
        list of numbers to check"""
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("list must contain only numbers")
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers
    parameters
    ----------
    numbers : list
        list of numbers to check"""
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("List must contain only numbers")
    if not numbers:
        return 0.0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]

def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers
    parameters
    ----------
    numbers : list
        list of numbers to check"""
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("List must contain only numbers")
    return max(set(numbers), key=numbers.count)


def factorial(n: int) -> int:
    """Function to calculate the factorial of a number
    parameters
    ----------
    n : int
        number to calculate the factorial of"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Function to check if a number is prime
    parameters
    ----------
    n : int
        number to check"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """Function to check if a string is a palindrome
    parameters
    ----------
    word : str
        string to check"""
    return word == word[::-1]
   


def reverse_string(string: str) -> str:
    """Function to reverse a string
    parameters
    ----------
    string : str
        string to reverse"""
    if not isinstance(string, str):
        raise TypeError("Only strings are allowed")
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers
    parameters
    ----------
    numbers : list
        list of numbers to check"""
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("list must contain only numbers")
    return sum(numbers)

def list_product(numbers: list) -> int:
    """Function to multiply a list of numbers
    parameters
    ----------
    numbers : list
        list of numbers to check"""
    if not numbers:
        raise ValueError("Cannot multiply empty list")
    elif not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Only can put numbers (int o float)")
    product = 1
    for num in numbers:
        product *= num
    return product