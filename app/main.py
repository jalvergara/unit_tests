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


def subtract(a: int, b: int) -> int:
    """_summary_

    Args:
        a : int
            Parameter 1.
        b : int
            Parameter 2.
    ------------------
    Returns:
        int
            a - b
    """
    return a - b

def square(a: int) -> int:
    """Function to square a number (a)

    Args:
        a : int
            Parameter 1.
    ------------------
    Returns:
        int
            a - b
    """
    return a ** 2


def is_even(x: int) -> bool:
    """ Function to check if a number is even
    
    Args:
        x : int
            Number to check if it is even
    ------------------
    Returns:
        bool
            True if x is even, False otherwise    
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """ Function to find the maximum number in a list
    
    Args:
        numbers : list
            List of numbers
    ------------------
    Returns:
        int
            Maximum number in the list
        ValueError
            Empty list
    """
    if len(numbers) == 0:
        raise ValueError("Empty list")

    return max(numbers)


def find_min(numbers: list) -> int:
    """ Function to find the minimum number in a list 
    
    Args:
        numbers : list
            List of numbers
    ------------------
    Returns:
        int
            Minimum number in the list
        ValueError
            Empty list
    """
    if len(numbers) == 0:
        raise ValueError("Empty list")
    
    return min(numbers)


def find_mean(numbers: list) -> float:
    """ Function to find the mean of a list of numbers
    
    Args:
        numbers : list
            List of numbers
    ------------------
    Returns:
        float
            Mean of the list
        ValueError
            Empty list
    """
    if len(numbers) == 0:
        raise ValueError("Empty list")
    
    return round(sum(numbers) / len(numbers), 2)


def find_median(numbers: list) -> float:
    """ Function to find the median of a list of numbers
    
    Args:
        numbers : list
            List of numbers
    ------------------
    Returns:
        float
            Median of the list
        ValueError
            Empty list
    """
    if len(numbers) == 0:
        raise ValueError("Empty list")
    
    numbers.sort()
    n = len(numbers)

    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    return numbers[n // 2]


def find_mode(numbers: list) -> int:
    """ Function to find the mode of a list of numbers
    
    Args:
        numbers : list
            List of numbers
    ------------------
    Returns:
        int
            Mode of the list
        ValueError
            Empty list
    """
    if len(numbers) == 0:
        raise ValueError("Empty list")
    
    return max(set(numbers), key = numbers.count)


def factorial(n: int) -> int:
    """ Function to find the factorial of a number 
    
    Args:
        n : int
            Number to find the factorial
    ------------------
    Returns:
        int
            Factorial of the number
    """
    
    if n == 0:
        return 1
    return n * factorial(n - 1)    


def is_prime(n: int) -> bool:
    """ Function to check if a number is prime 
    
    Args:
        n : int
            Number to check if it is prime
    ------------------
    Returns:
        bool
            True if n is prime, False otherwise
    """
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """ Function to check if a word is a palindrome 
    
    Args:
        word : str
            Word to check if it is a palindrome
    ------------------
    Returns:
        bool
            True if word is a palindrome, False otherwise
    """
    word = word.lower()
    return word == word[::-1]


def reverse_string(string: str) -> str:
    # TODO: write function to reverse a string
    """ Function to reverse a string 
    
    Args:
        string : str
            String to reverse
    ------------------
    Returns:
        str
            Reversed string
    """
    return string[::-1]


def list_sum(numbers: list) -> int:
    # TODO: write function to sum a list of numbers
    """ Function to sum a list of numbers 
    
    Args:
        numbers : list
            List of numbers
    ------------------
    Returns:
        int
            Sum of the list
    """
    return sum(numbers)    


def list_product(numbers: list) -> int:
    # TODO: write function to multiply a list of numbers
    """ Function to multiply a list of numbers 
    
    Args:
        numbers : list
            List of numbers
    ------------------
    Returns:
        int
            Product of the list
    """
    result = 1
    for number in numbers:
        result *= number
    return result
    
