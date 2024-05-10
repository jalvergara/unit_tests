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


# Mariana Mera
def subtract(a: int, b: int) -> int:
    """Function to substract two numbers

    Parameters
    ----------
    a : int
        first digit to substract
    b : int
        second digit to substract

    Returns
    -------
    int
        a '-' b
    """
    return a - b

def square(a: int) -> int:
    """Function to square a number

    Parameters
    ----------
    a : int
        
    Returns
    -------
    int
        a '*' a
    """ 
    return a * a


def is_even(x: int) -> bool:
    """
    Function to check if a number is even.

    Parameters
    ----------
    x : int
        The number to check.

    Returns
    -------
    bool
        True if the number is even, False otherwise.
    """
    return x % 2 == 0



def find_max(numbers: list) -> int:
    """
    Function to find the maximum number in a list.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    int
        The maximum number found in the list.
    """
    if not numbers:
        raise ValueError("The list is empty")
    
    return max(numbers)


def find_min(numbers: list) -> int:
    """
    Function to find the minimum number in a list.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    int
        The minimum number found in the list.
    """
    if not numbers:
        raise ValueError("The list is empty")
    
    return min(numbers)




def find_mean(numbers: list) -> float:
    """
    Function to find the mean (average) of numbers in a list.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The mean of the numbers in the list.
    """
    if not numbers:
        return 0  

    total = sum(numbers)

    mean = total / len(numbers)

    return mean



def find_median(numbers: list) -> float:
    """
    Function to find the median of numbers in a list.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The median of the numbers in the list.
    """
    if not numbers:
        return 0
    
    numbers.sort()  
    
    n = len(numbers)
    
    if n % 2 == 0:
        middle_left = numbers[n // 2 - 1]
        middle_right = numbers[n // 2]
        median = (middle_left + middle_right) / 2
    else:
        median = numbers[n // 2]
    
    return median



def find_mode(numbers: list) -> list:
    """
    Function to find the mode(s) in a list of numbers.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    list
        A list containing the mode(s) found in the input list.
        If there are multiple modes, they are all returned.
        If there is no mode (all numbers are unique), an empty list is returned.
    """
    if not numbers:
        return []  
    
    counts = {}
    
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    
    max_count = max(counts.values())
    
    modes = [number for number, count in counts.items() if count == max_count]
    
    return modes



def factorial(n: int) -> int:
    """
    Function to compute the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The non-negative integer for which factorial is to be computed.

    Returns
    -------
    int
        The factorial of the given non-negative integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def is_prime(n: int) -> bool:
    """
    Function to check if a number is prime.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False  
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    
    return True 



def is_palindrome(word: str) -> bool:
    """
    Function to check if a word is a palindrome.

    Parameters
    ----------
    word : str
        The word to check.

    Returns
    -------
    bool
        True if the word is a palindrome, False otherwise.
    """
    word = word.lower()
    
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """
    Function to reverse a given string.

    Parameters
    ----------
    string : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    reversed_string = ""
    
    for char in string[::-1]:
        
        reversed_string += char

    return reversed_string




def list_sum(numbers: list) -> int:
    """
    Function to compute the sum of numbers in a list.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    int
        The sum of the numbers in the list.
    """
    total = 0
    
    for num in numbers:
        total += num
    
    return total



def list_product(numbers: list) -> int:
    """
    Function to compute the product of numbers in a list.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    int
        The product of the numbers in the list.
    """
    product = 1
    
    for num in numbers:
        product *= num
    
    return product

