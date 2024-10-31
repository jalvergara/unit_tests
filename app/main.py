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
    """
    Resta dos números enteros.

    Parámetros:
    a (int): El minuendo.
    b (int): El sustraendo.

    Retorna:
    int: El resultado de restar b a a.
    """
    return a - b

def square(a: int) -> int:
    """
    Calcula el cuadrado de un número entero.

    Parámetros:
    a (int): El número a elevar al cuadrado.

    Retorna:
    int: El cuadrado de a.
    """
    return a ** 2


def is_even(x: int) -> bool:
    """
    Verifica si un número es par.

    Parámetros:
    x (int): El número a verificar.

    Retorna:
    bool: True si el número es par, False si es impar.
    """
    return x % 2 == 0

def find_max(numbers: list) -> int:
    """
    Encuentra el número máximo en una lista de números.

    Parámetros:
    numbers (list): Lista de números.

    Retorna:
    int: El valor máximo de la lista.
    """
    return max(numbers)

def find_min(numbers: list) -> int:
    """
    Encuentra el número mínimo en una lista de números.

    Parámetros:
    numbers (list): Lista de números.

    Retorna:
    int: El valor mínimo de la lista.
    """
    return min(numbers)



def find_mean(numbers: list) -> float:
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    numbers (list): Lista de números.

    Retorna:
    float: El promedio de los números en la lista.
    """
    return sum(numbers) / len(numbers) if numbers else 0.0

def find_median(numbers: list) -> float:
    """
    Calcula la mediana de una lista de números.

    Parámetros:
    numbers (list): Lista de números.

    Retorna:
    float: La mediana de los números en la lista.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 1:
        return sorted_numbers[middle]
    else:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

from collections import Counter

def find_mode(numbers: list) -> int:
    """
    Calcula la moda de una lista de números.

    Parámetros:
    numbers (list): Lista de números.

    Retorna:
    int: La moda de los números en la lista (el valor que más se repite).
    """
    if not numbers:
        return None
    frequency = Counter(numbers)
    mode = max(frequency, key=frequency.get)
    return mode


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número.

    Parámetros:
    n (int): El número para calcular su factorial (debe ser un entero no negativo).

    Retorna:
    int: El factorial de n.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """
    Verifica si un número es primo.

    Parámetros:
    n (int): El número a verificar.

    Retorna:
    bool: True si el número es primo, False si no lo es.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(word: str) -> bool:
    """
    Verifica si una palabra es un palíndromo.

    Parámetros:
    word (str): La palabra a verificar.

    Retorna:
    bool: True si la palabra es un palíndromo, False si no lo es.
    """
    return word == word[::-1]



def reverse_string(string: str) -> str:
    """
    Invierte una cadena de texto.

    Parámetros:
    string (str): La cadena de texto a invertir.

    Retorna:
    str: La cadena invertida.
    """
    return string[::-1]

def list_sum(numbers: list) -> int:
    """
    Calcula la suma de los elementos de una lista de números.

    Parámetros:
    numbers (list): Lista de números.

    Retorna:
    int: La suma de todos los elementos en la lista.
    """
    return sum(numbers)

def list_product(numbers: list) -> int:
    """
    Calcula el producto de los elementos de una lista de números.

    Parámetros:
    numbers (list): Lista de números.

    Retorna:
    int: El producto de todos los elementos en la lista.
    """
    product = 1
    for number in numbers:
        product *= number
    return product if numbers else 0

