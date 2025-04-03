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
    """Function to subtract two numbers (a - b)

    Parameters
    ----------
    a : int
        minuend
    b : int
        subtrahend

    Returns
    -------
    int
        Result of a - b
    """
    return a - b

def square(a: int) -> int:
    """Function to square a number

    Parameters
    ----------
    a : int
        Number to square

    Returns
    -------
    int
        a squared
    """
    return a * a


def is_even(x: int) -> bool:
    """Function to check if a number is even 
    
    Parameters
    ----------
    x : int
        Number to check

    Returns
    -------
    bool
        True if x is even, False otherwise
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list

    Parameters
    ----------
    numbers : list
        List of numbers

    Returns
    -------
    int
        Maximum number in the list

  
    """
    return max(numbers)


def find_min(numbers: list) -> int:
    """Finds the minimum number in a list.

    Parameters:
      numbers (list): A list of numbers.

    Returns:
      int: The smallest number in the list.

    """
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Calculates the mean (average) of a list of numbers.

    Parameters:
      numbers (list): A list of numbers.

    Returns:
      float: The average value.
    """
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """Calculates the median of a list of numbers.

    Parameters:
      numbers (list): A list of numbers.

    Returns:
      float: The median value.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
       
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]


def find_mode(numbers: list) -> int:
    """Function to find the mode (most frequent number) in a list of numbers.

    Parameters
    ----------
    numbers : list
        List of numbers to evaluate.

    Returns
    -------
    int
        The mode of the list (the number that appears most frequently). 
        Returns None if the list is empty.
    """
    if not numbers: 
        return None
    return max(set(numbers), key=numbers.count)


def factorial(n: int) -> int:
    """Function to calculate the factorial of a number

    Parameters
    ----------
    n : int
        The number to calculate the factorial of

    Returns
    -------
    int
        The factorial of n

    Raises
    ------
    ValueError
        If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    


def is_prime(n: int) -> bool:
    """Function to check if a number is prime

    Parameters
    ----------
    n : int
        The number to check

    Returns
    -------
    bool
        True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
  
   


def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome

    Parameters
    ----------
    word : str
        The word to check

    Returns
    -------
    bool
        True if word is a palindrome, False otherwise

    Raises
    ------
    ValueError
        If the word is empty
    """
    word = ''.join(char.lower() for char in word if char.isalnum())
    if not word:
        raise ValueError("cannot check palindrome for an empty string")
    return word == word[::-1]


def reverse_string(string: str) -> str:
        """Function to reverse a string

    Parameters
    ----------
    string : str
        The string to reverse

    Returns
    -------
    str
        The reversed string

    Raises
    ------
    ValueError
        If the string is empty
    """
        if not string:
            raise ValueError("Cannot reverse an empty string")
        return string[::-1]
        


def list_sum(numbers: list) -> int:
        """Function to calculate the sum of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    int
        The sum of the numbers in the list

    Raises
    ------
    ValueError
        If the list is empty
    """
        if not numbers:
            raise ValueError("cannot sum an empty list")
        return sum(numbers)


def list_product(numbers: list) -> int:
    """Function to calculate the product of a list of numbers

    Parameters
    ----------
    numbers : list
        A list of numbers

    Returns
    -------
    int
        The product of the numbers in the list

    Raises
    ------
    ValueError
        If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate product of an empty list")
    result = 1
    for num in numbers:
        result *= num
    return result


