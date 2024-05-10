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



"""
🔢 **Funciones Matemáticas y de Utilidad:**

- `subtract(a, b)`: ➖ Resta dos números.
- `square(a)`: 🟥 Eleva un número al cuadrado.
- `is_even(x)`: ✅ Verifica si un número es par.
- `find_max(numbers)`: 📈 Encuentra el máximo en una lista.
- `find_min(numbers)`: 📉 Encuentra el mínimo en una lista.
- `find_mean(numbers)`: 📊 Calcula la media de una lista.
- `find_median(numbers)`: 🔍 Calcula la mediana de una lista.
- `find_mode(numbers)`: 🔢 Encuentra la moda en una lista.
- `factorial(n)`: ➗ Calcula el factorial de un número.
- `is_prime(n)`: 🎯 Verifica si un número es primo.
- `is_palindrome(word)`: 🔁 Checa si una palabra es palíndromo.
- `reverse_string(string)`: 🔀 Invierte un string.
- `list_sum(numbers)`: ➕ Suma los números de una lista.
- `list_product(numbers)`: ✖️ Multiplica los números de una lista.
"""


def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

def square(a: int) -> int:
    """Square a number."""
    return a * a

def is_even(x: int) -> bool:
    """Check if a number is even."""
    return x % 2 == 0

def find_max(numbers: list) -> int:
    """Find the maximum number in a list."""
    return max(numbers)

def find_min(numbers: list) -> int:
    """Find the minimum number in a list."""
    return min(numbers)

def find_mean(numbers: list) -> float:
    """Find the mean of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def find_median(numbers: list) -> float:
    """Find the median of a list of numbers."""
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    else:
        return numbers[mid]

def find_mode(numbers: list) -> int:
    """Find the mode of a list of numbers."""
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count][0]

def factorial(n: int) -> int:
    """Find the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome."""
    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Reverse a string."""
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Sum a list of numbers."""
    return sum(numbers)

def list_product(numbers: list) -> int:
    """Multiply a list of numbers."""
    from functools import reduce
    import operator
    return reduce(operator.mul, numbers, 1)

