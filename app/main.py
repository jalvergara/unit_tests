""" main functions to explain unit testing"""

import pandas as pd
import numpy as np
import statistics
import math


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
    """Function to substract two numbers
    
    Parameters
    ----------
    a: int
        first digit to substract
    b: int
        second digit to substract
        
    Returns
    -------
    int
        a '-' b
    """
    return a - b

def square(a: int) -> int:
    """Function to square a number
    
    Parameters
    ----------
    a: int
        number to square
        
    Returns
    -------
    int
        a '**' 2
    """
    return a ** 2


def is_even(x: int) -> bool:
    """Function to check if a number is even
    
    Parameters
    ----------
    a: int
        number to check
        
    Returns
    -------
    bool
        True if even, False otherwise
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to fin the maximum number in a list
    
    Parameters
    ----------
    numbers: list
            list of numbers to check
        
    Returns
    -------
    int
        maximum number in the list
    
    Raises
    ------
    ValueError
        Empty List
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to fin the minimum number in a list
    
    Parameters
    ----------
    numbers: list
            list of numbers to check
        
    Returns
    -------
    int
        minimum number in the list
    
    Raises
    ------
    ValueError
        Empty List
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Function to fin the mean of the numbers in a list
    
    Parameters
    ----------
    numbers: list
            list of numbers to check
        
    Returns
    -------
    float
        mean of the numbers in the list

    Raises
    ------
    ValueError
        Empty List
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    return np.mean(numbers)


def find_median(numbers: list) -> float:
    """Function to fin the median of the numbers in a list
    
    Parameters
    ----------
    numbers: list
            list of numbers to check
        
    Returns
    -------
    float
        median of the numbers in the list
    
    Raises
    ------
    ValueError
        Empty List
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    return np.mean(numbers)


def find_mode(numbers: list) -> int:
    """Function to fin the mode of the numbers in a list
    
    Parameters
    ----------
    numbers: list
            list of numbers to check
        
    Returns
    -------
    int
        mode of the numbers in the list

    Raises
    ------
    ValueError
        Empty List
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    return statistics.mode(numbers)


def factorial(n: int) -> int:
    """Function to calculate the factorial of a number
    
    Parameters
    ----------
    n: int
        number to calculate the factorial
        
    Returns
    -------
    int
        factorial of the number
    """

    return math.factorial(n)


def is_prime(n: int) -> bool:
    """Function to calculate if a number is prime
    
    Parameters
    ----------
    n: int
        number to check
        
    Returns
    -------
    bool
        True  if primer, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """Function to check if a word is palindrome
    
    Parameters
    ----------
    word: str
        word to check
        
    Returns
    -------
    bool
        True  if palindrome, False otherwise
    
    Raises
    ------
    ValueError
        Empty Word
    """
    if not word:
        raise ValueError("The word is empty")
    
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """Function to reverse a string
    
    Parameters
    ----------
    string: str
        string to reverse
            
    Returns
    -------
    str
        reversed string
    
    Raises
    ------
    ValueError
        Empty String
    """

    if not string:
        raise ValueError("The String is empty")
    
    return string[::-1]


def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers
    
    Parameters
    ----------
    number: list
        list of numbers to sum
        
    Returns
    -------
    int
       sum of the number in the list
    
    Raises
    ------
    ValueError
        Empty List
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    return sum(numbers)


def list_product(numbers: list) -> int:
    """Function multiply a list of numbers
    
    Parameters
    ----------
    number: list
        list of numbers to multiply
        
    Returns
    -------
    int
        product of the numbers in the list

    Raises
    ------
    ValueError
        Empty List
    """

    if len(numbers) == 0:
        raise ValueError("The list is empty")

    product = 1
    for i in numbers:
        product *= i
    return product 
