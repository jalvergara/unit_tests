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


# Nicolas Cuaran
def subtract(a: int, b: int) -> int:
    """substract
    Parameters
    ----------
    a : int
        first digit
    b : int
        second digit

    Returns
    -------
    int
        a '-' b
    
    """
    return a - b 

def square(a: int) -> int:
    """square

    Parameters
    ----------
    a : int
        first digit

    Returns
    -------
    int
        a * a
    """
    return a * a

def is_even(x: int) -> bool:
    """ is even?
    Parameters
    ----------
    x : int
        first digit

    Returns
    -------
    Bool :
        if x % 2 == 0
            True 
        e
            False
    """
    return x % 2 == 0

def find_max(numbers: list) -> int:
    """ find max
    Parameters
    ----------
     numbers : list
        list of numbers

    Returns
    -------
    int:  max of numbers
    """
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list")
    
    return max(numbers)

def find_min(numbers: list) -> int:
    """ find min
    Parameters
    ----------
     numbers : list
        list of numbers

    Returns
    -------
    int:  min of numbers
    
    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list")
    
    return min(numbers)

def find_mean(numbers: list) -> float:
    """ find mean
    Parameters
    ----------
     numbers : list
        list of numbers
    Returns
    -------
    float:  mean of numbers
   
     Raises
    ------
    ValueError
        If the list is empty.
    """
    
    if not numbers:
        raise ValueError("Cannot compute mean of an empty list")

    return sum(numbers) / len(numbers)

def find_median(numbers: list) -> float:
    """Returns the median of a list of numbers.

        Parameters
        ----------
        numbers : list
            A list of numerical values.

        Returns
        -------
        float
            The median of the numbers in the list.

        Raises
        ------
        ValueError
            If the list is empty.
        """
    if not numbers:
            raise ValueError("Cannot compute median of an empty list")
        
    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 0:
            return (numbers[mid - 1] + numbers[mid]) / 2
    else:
            return numbers[mid]

def find_mode(numbers: list) -> int:
    """Returns the mode of a list of numbers.

    Parameters
    ----------
    numbers : list
        A list of numerical values.

    Returns
    -------
    int
        The mode of the numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot compute mode of an empty list")

    frequency = {}
    max_count = 0
    mode = numbers[0]

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > max_count:
            max_count = frequency[num]
            mode = num

    return mode

def factorial(n: int) -> int:
    """Calculates the factorial of a given number.

        Parameters
        ----------
        n : int
            A non-negative integer.

        Returns
        -------
        int
            The factorial of the number.

        Raises
        ------
        ValueError
            If `n` is negative.
        """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

def is_prime(n: int) -> bool:
    """Checks if a number is prime.

        Parameters
        ----------
        n : int
            A positive integer.

        Returns
        -------
        bool
            True if the number is prime, False otherwise.

        Raises
        ------
        ValueError
            If `n` is less than 2.
        """
    if n < 2:
            raise ValueError("Prime numbers must be greater than or equal to 2")

    for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

    return True

def is_palindrome(word: str) -> bool:
    """Checks if a word is a palindrome.

    Parameters
    ----------
    word : str
        The word to check.

    Returns
    -------
    bool
        True if the word is a palindrome, False otherwise.
    """
    word = word.lower().replace(" ", "")

    return word == word[::-1]

def reverse_string(string: str) -> str:
    """Reverses a given string.

    Parameters
    ----------
    string : str
        The string to be reversed.

    Returns
    -------
    str
        The reversed string.
    """
    return string[::-1]

def list_sum(numbers: list) -> int:
    """Calculates the sum of a list of numbers.

    Parameters
    ----------
    numbers : list
        A list of integers.

    Returns
    -------
    int
        The sum of all numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
         raise ValueError("The list cannot be empty")
    
    return sum(numbers)
 


def list_product(numbers: list) -> int:
    """Calculates the product of a list of numbers.

    Parameters
    ----------
    numbers : list
        A list of integers.

    Returns
    -------
    int
        The product of all numbers in the list.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("The list cannot be empty")

    product = 1
    for num in numbers:
        product *= num

    return product