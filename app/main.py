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


# Jhonatan Morales
def subtract(a: int, b: int) -> int:
    return a-b
def square(a: int) -> int:
    return a*a

def is_even(x: int) -> bool:
    return x%2 == 0


def find_max(numbers: list) -> int:
    if not numbers:
        raise ValueError("lista vacia")
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num

def find_min(numbers: list) -> int:
    if not numbers:
        raise ValueError("lista vacia")
    min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num



def find_mean(numbers: list) -> float:
    if not numbers:
        raise ValueError("lista vacia")
    
    sum = 0
    for i in numbers:
        sum += i
    mean = sum/len(numbers)
    return mean

def find_median(numbers: list) -> float:
    if not numbers:
        raise ValueError("lista vacia")

    numbers = sorted(numbers)
    n = len(numbers) 
    mid = n//2

    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2  
    else:
        return numbers[mid]

def find_mode(numbers: list) -> int:
    if not numbers:
        raise ValueError("lista vacia")
    
    freq = {}

    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    mode = None
    max_count = 0
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            mode = num
    
    return mode


def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)


def is_prime(n: int) -> bool:

    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


def is_palindrome(word: str) -> bool:
    return word == word[::-1]

def reverse_string(string: str) -> str:
    return string[::-1]


def list_sum(numbers: list) -> int:
    if not numbers:
        raise ValueError("lista vacia")
    suma = 0
    for i in numbers:
        suma += i
    return suma
    


def list_product(numbers: list) -> int:
    if not numbers:
        raise ValueError("lista vacia")
    product = 1
    for i in numbers:
        product *= i
    return product