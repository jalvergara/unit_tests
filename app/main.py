""" main functions to explain unit testing"""

import pandas as pd
import numpy as np


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
    """Function to subtrac two numbers

    Parameters
    ----------
    a : int
        first digit to subtrac
    b : int
        second digit to subtrac

    Returns
    -------
    int
        a '-' b
    """
    return a - b

def square(a: int) -> int:
    """Function to square a number.

    Parameters:
    a (int): The number to be squared.

    Returns:
    int: The square of the input number.
    """
    return a * a


def is_even(x: int) -> bool:
    """Function to check if a number is even.

    Parameters:
    num (int): The number to be checked.

    Returns:
    bool: True if the number is even, False otherwise.
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list.

    Parameters:
    numbers (list): The list of numbers.

    Returns:
    int: The maximum number in the list.
    """
    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list.

    Parameters:
    numbers (list): The list of numbers.

    Returns:
    int: The minimum number in the list.
    """
    if not numbers:
        return None  
    
    min_num = numbers[0]  
    
    for num in numbers:
        if num < min_num:
            min_num = num  
    return min_num


def find_mean(numbers: list) -> float:
    """Function to find the mean of a list of numbers.

    Parameters:
    numbers (list): The list of numbers.

    Returns:
    float: The mean of the numbers in the list.
    """
    if not numbers:
        return None  
    
    total = sum(numbers)  
    count = len(numbers)  
    
    return total / count  


def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers
    
    Parameters
    ----------
    numbers : list
        list of numbers
        
    Returns
    -------
    float
        median of the list of numbers
    
    """

    numbers_array = np.array(numbers)

    median = np.median(numbers_array)

    return median

def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers
    
    Parameters
    ----------
    numbers : list
        list of numbers
        
    Returns
    -------
    int
        mode of the list of numbers
    
    """
    frequency = {} 
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_freq = max(frequency.values()) 
    mode = None
    for num, freq in frequency.items():
        if freq == max_freq:
            mode = num
            break
    
    return mode


def factorial(n: int) -> int:
    """Function to calculate the factorial of a number

    Parameters
    ----------
    n : int
        number to calculate the factorial
    
    Returns
    -------
    int
        factorial of n

    Raises
    ------
    ValueError
        If n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """Function to check if a number is prime
    
    Parameters
    ----------
    n : int
        non-negative integer
        
    Returns
    -------
    bool
        True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def is_palindrome(word: str) -> bool:
    # TODO: write function to check if a word is a palindrome
    pass


def reverse_string(string: str) -> str:
    """Function to reverse a string
    
    Parameters
    ----------
    string : str
        input string
        
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
    float
        sum of the numbers in the list
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
        product of the numbers in the list
    """
    product = 1

    for num in numbers:
        product *= num
    
    return product
