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

# JPGC 
def subtract(a: int, b: int) -> int:
    # HECHO: función para restar dos números
    return a - b

def square(a: int) -> int:
    # HECHO: función para calcular el cuadrado de un número
    return a * a

def is_even(x: int) -> bool:
    # HECHO: función para verificar si un número es par
    return x % 2 == 0

def find_max(numbers: list) -> int:
    # HECHO: función para encontrar el número máximo en una lista
    return max(numbers) if numbers else None

def find_min(numbers: list) -> int:
    # HECHO: función para encontrar el número mínimo en una lista
    return min(numbers) if numbers else None

def find_mean(numbers: list) -> float:
    # HECHO: función para calcular la media de una lista de números
    return sum(numbers) / len(numbers) if numbers else None

def find_median(numbers: list) -> float:
    # HECHO: función para calcular la mediana de una lista de números
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return None
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

from collections import Counter

def find_mode(numbers: list) -> int:
    # HECHO: función para encontrar la moda en una lista de números
    if not numbers:
        return None
    count = Counter(numbers)
    return count.most_common(1)[0][0]

import math

def factorial(n: int) -> int:
    # HECHO: función para calcular el factorial de un número
    if n < 0:
        return None
    return math.factorial(n)

def is_prime(n: int) -> bool:
    # HECHO: función para verificar si un número es primo
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(word: str) -> bool:
    # HECHO: función para verificar si una palabra es un palíndromo
    return word == word[::-1]

def reverse_string(string: str) -> str:
    # HECHO: función para invertir una cadena de texto
    return string[::-1]

def list_sum(numbers: list) -> int:
    # HECHO: función para sumar una lista de números
    return sum(numbers)

def list_product(numbers: list) -> int:
    # HECHO: función para multiplicar una lista de números
    product = 1
    for number in numbers:
        product *= number
    return product
