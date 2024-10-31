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
    Resta dos números.

    Parameters
    ----------
    a : int
        primer número
    b : int
        segundo número

    Returns
    -------
    int
        resultado de a - b
    """
    return a - b



def square(a: int) -> int:
    """
    Calcula el cuadrado de un número.

    Parameters
    ----------
    a : int
        número a elevar al cuadrado

    Returns
    -------
    int
        cuadrado de a
    """
    return a * a



def is_even(x: int) -> bool:
    """
    Verifica si un número es par.

    Parameters
    ----------
    x : int
        número a verificar

    Returns
    -------
    bool
        True si x es par, False de lo contrario
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """
    Encuentra el valor máximo en una lista de números.

    Parameters
    ----------
    numbers : list
        Lista de números.

    Returns
    -------
    int
        Valor máximo de la lista.
    """
    return max(numbers)



def find_min(numbers: list) -> int:
    """
    Encuentra el valor mínimo en una lista de números.

    Parameters
    ----------
    numbers : list
        Lista de números.

    Returns
    -------
    int
        Valor mínimo de la lista.
    """
    return min(numbers)



def find_mean(numbers: list) -> float:
    """
    Calcula la media de una lista de números.

    Parameters
    ----------
    numbers : list
        Lista de números.

    Returns
    -------
    float
        Media de la lista.
    """
    return sum(numbers) / len(numbers)



def find_median(numbers: list) -> float:
    """
    Calcula la mediana de una lista de números.

    Parameters
    ----------
    numbers : list
        Lista de números.

    Returns
    -------
    float
        Mediana de la lista.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]



from collections import Counter

def find_mode(numbers: list) -> int:
    """
    Encuentra la moda en una lista de números.

    Parameters
    ----------
    numbers : list
        Lista de números.

    Returns
    -------
    int
        Moda de la lista.
    """
    counter = Counter(numbers)
    return max(counter, key=counter.get)


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero.

    Parameters
    ----------
    n : int
        Número entero.

    Returns
    -------
    int
        Factorial del número n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """
    Verifica si un número es primo.

    Parameters
    ----------
    n : int
        Número a verificar.

    Returns
    -------
    bool
        True si el número es primo, False de lo contrario.
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

    Parameters
    ----------
    word : str
        Palabra a verificar.

    Returns
    -------
    bool
        True si es un palíndromo, False de lo contrario.
    """
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """
    Invierte una cadena de texto.

    Parameters
    ----------
    string : str
        Cadena a invertir.

    Returns
    -------
    str
        Cadena invertida.
    """
    return string[::-1]


def list_sum(numbers: list) -> int:
    """
    Calcula la suma de una lista de números.

    Parameters
    ----------
    numbers : list
        Lista de números.

    Returns
    -------
    int
        Suma de todos los números en la lista.
    """
    return sum(numbers)


def list_product(numbers: list) -> int:
    """
    Calcula el producto de una lista de números.

    Parameters
    ----------
    numbers : list
        Lista de números.

    Returns
    -------
    int
        Producto de todos los números en la lista.
    """
    product = 1
    for number in numbers:
        product *= number
    return product
