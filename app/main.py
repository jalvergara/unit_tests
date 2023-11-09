""" main functions to explain unit testing"""

import numpy as np
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
    """_summary_

    Parameters
    ----------
    a : int
        parameter1
    b : int
        parameter2

    Returns
    -------
    int
        a-b
    """
    return a - b


# Samuel Patino
def square(a: int) -> int:
    # TODO: write function to square a number
    pass


# Sebastian Diaz
def is_even(x: int) -> bool:
    # TODO: write function to check if a number is even
    pass


# Andres enriquez
def find_max(numbers: list) -> int:
    """
    Encuentra el número máximo en una lista de números.

    Args:
        numbers (list): Una lista de números.

    Returns:
        int: El número máximo encontrado en la lista.

    Raises:
        ValueError: Si la lista está vacía.

    Examples:
        >>> find_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        9

        >>> find_max([])
        Traceback (most recent call last):
            ...
        ValueError: La lista está vacía. No se puede encontrar el número máximo.
    """
    if not numbers:
        raise ValueError("La lista está vacía. No se puede encontrar el número máximo.")

    max_number = numbers[0]  # Suponemos que el primer número es el máximo inicialmente.

    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number



# Juan Felipe Zambrano
def find_min(numbers: list) -> int:
    # TODO: write function to find the minimum number in a list
    pass


# Kevin Artunduaga
def find_mean(numbers: list) -> float:
    """ Function to find the mean of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers

    Returns
    -------
    float
        mean of the list of numbers

    """
    # Por si la lista esta vacia y evitar dividir por 0
    if len(numbers) == 0:
        return 0.0

    mean = sum(numbers) / len(numbers)
    return mean


# Camila Cardona
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


# Juan Camilo Vargas
def find_mode(numbers: list) -> int:
    """
    Function to find the mode(s) in a list of integers.

    Parameters
    ----------
    data : list[int]
        List of integers to find the mode(s) from.

    Returns
    -------
    int
        If multiple values have the same highest frequency, it returns the smallest one.
        If the list is empty, it returns None.
    """

    if not numbers:
        return None

    num_frequency = {}
    for num in numbers:
        num_frequency[num] = num_frequency.get(num, 0) + 1

    max_frequency = max(num_frequency.values())
    modes = [num for num, freq in num_frequency.items() if freq == max_frequency]
    return min(modes)


# Samuel Pinzon
def factorial(n: int) -> int:
    """
    Function to calculate the factorial of a number

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

# Atenea Rojas
def is_prime(n: int) -> bool:
    """
    This function checks whether or not a given integer is prime.

    Parameter
    ----------
    n : int
       Integer number to check primality for.

    Returns
    -------
    bool
        True if the input parameter is prime, False otherwise.
    """
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# Gustavo Chipatinza
def is_palindrome(word: str) -> bool:
    """
    Determine if a given word or phrase is a palindrome.

    Parameters:
    ----------
    word : str
        The word or phrase to be checked for palindromicity.

    Returns:
    -------
    bool
        True if the input is a palindrome, False otherwise.
    """
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]
    


# Santiago Murgueitio
def reverse_string(string: str) -> str:
    """
    Reverse a given string.

    Args:
        string (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Example:
        input -> reverse_string("Hello, World!")
        output -> '!dlroW ,olleH'
    """
    return string[::-1]


# Maria Angelica Portocarrero
def list_sum(numbers: list) -> int:
    """ This method calculates the sum of a list of numbers.

    Arguments:
        numbers (list): A list of numbers.

    Returns:
        int: The sum of the numbers in the list.
    """
    return sum(numbers)

# Angie Manzano
def list_product(numbers: list) -> int:
    """Function to multiply a list of numbers

    Parameters
    ----------
    numbers : list
        list with numbers to multiply

    Returns
    -------
    int
        [a * b * c * d * ... * n]
    """
    product = 1
    listNumbers = []
    for i in numbers:
         if i != None :
            listNumbers.append(i)
    for i in listNumbers:
         product = product * i
    return product
