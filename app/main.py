""" main functions to explain unit testing"""

from typing import Counter
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


def subtract(a: int, b: int) -> int:
    """Function to subtract two numbers

    Parameters
    ----------
    a : int
        First number.
    b : int
        Second number.

    Returns
    -------
    int
        Difference of a and b.
    """
    return a - b


def square(a: int) -> int:
    """Funtion to calculate the square of a number
    
    Parameters
    ----------
    a : int
        Number to square.

    Returns
    -------
    int
        Square of the number.
    """
    return a * a


def is_even(x: int) -> bool:
    """Funtion to check if a number is even
    
    Parameters
    ----------
    x : int
        Number to check.

    Returns
    -------
    bool
        True if x is even, False otherwise.
    """

    return x % 2 == 0

def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Maximum number in the list.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list

    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Minimum number in the list.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Function to find the mean of a list of numbers
    
    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        Mean of the numbers.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)

def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers
    
    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    float
        Median of the numbers.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    
    numbers.sort()
    n = len(numbers)
    m = n // 2

    if n % 2 == 0:
        return (numbers[m - 1] + numbers[m]) / 2
    else:
        return numbers[m]
    
def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers
    
    Parameters
    ----------
    numbers : list
        List of numbers.

    Returns
    -------
    int
        Mode of the number list.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    
    counter = Counter(numbers)
    return counter.most_common(1)[0][0]


def factorial(n: int) -> int:
    """Function to find the factorial of a number

    Parameters
    ----------
    n : int
        Non-negative integer.

    Returns
    -------
    int
        Factorial of n.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Function to check if a number is prime.

    Parameters
    ----------
    n : int
        Number to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 1, 2):  
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome.

    Parameters
    ----------
    word : str
        Word to check.

    Returns
    -------
    bool
        True if the word is a palindrome, False otherwise.
    
    Raises
    ------
    TypeError
        If the input is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    
    return word == word[::-1]
    



def reverse_string(string: str) -> str:
    """Function to reverse a string.

    Parameters
    ----------
    string : str
        String to reverse.

    Returns
    -------
    str
        Reversed string.

    Raises
    ------
    TypeError
        If the input is not a string.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    return string[::-1]


def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers.
    Parameters
    ----------
    numbers : list of int
        List of numbers to sum.

    Returns
    -------
    int 
        Sum of all numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty.
    TypeError
        If the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All elements must be numbers.")

    return sum(numbers)


def list_product(numbers: list) -> int:
    """Function to multiply a list of numbers.

    Parameters
    ----------
    numbers : List
        List of numbers to multiply.

    Returns
    -------
    int
        Product of all numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty.
    TypeError
        If the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All elements must be numbers.")

    product = 1
    for num in numbers:
        product *=num
    return product
