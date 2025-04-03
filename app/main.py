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
    """"Function to substract two numbers
    
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
    """"Function to square a number
    
    Parameters
    ----------
    a : int
        single digit to square
        
        Returns
        -------
        int
            a '**' 2
    
    """
    return a ** 2


def is_even(x: int) -> bool:
    """Function to check if a number is even
    parameters
    ----------
    x : int
        number to check
        
        returns
        -------
        bool
            True if even, False otherwise
    """
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list
    parameters
    ----------
        numbers : list
            list of numbers to check
            
            returns
            -------
                int
                maximum number in the list 
    """
    if not numbers:
        return None
    return max(numbers)


def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list
    parameters
    ----------
        numbers : list  
            list of numbers to check
            
        returns
        -------
            int :
                minimum number in the list"""
    if not numbers:
        return None
    return min(numbers)


def find_mean(numbers: list) -> float:
    """Function to find the mean of a list of numbers
    parameters
    ----------
        numbers : list
            list of numbers to check
            
            returns
            -------
                float
                    mean of the list"""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def find_median(numbers: list) -> float:
    """"Function to find the median of a list of numbers
    parameters
    ----------
        numbers : list
            list of numbers to check
            
            returns
            -------
                float
                    median of the list"""
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]


def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers
    parameters
    ----------
        numbers : list
            list of numbers to check
            
            returns
            -------
                int
                    mode of the list"""
    if not numbers:
        return None
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_count = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == max_count]
    if len(modes) == len(numbers):
        return None
    if len(modes) == 1:
        return modes[0]
    return modes

def factorial(n: int) -> int:
    """"Function to find the factorial of a number
    parameters
    ----------
        n : int
            number to find the factorial of
            
            returns
            -------
                int
                    factorial of the number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n ==1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result 


def is_prime(n: int) -> bool:
    """Function to check if a number is prime
    parameters
    ----------
        n : int
            number to check
        
        returns
        -------
            bool
                True if prime, False otherwise"""
    if  n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome(word: str) -> bool:
    """"Function to check if a word is a palindrome
    parameters
    ----------
        word : str
            word to check
        
        returns
        -------
            bool
                True if palindrome, False otherwise"""
    word = word.lower()
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def reverse_string(string: str) -> str:
    """Function to reverse a string
    parameters
    ----------
        string : str
            string to reverse
        
        returns
        -------
            str
                reversed string"""
    if not string:
        return string
    reversed_string = ""
    for char in string[::-1]:
        reversed_string += char
    return reversed_string

def list_sum(numbers: list) -> int:
    """"Function to sum a list of numbers
    
    parameters
        ----------
        numbers : list
            list of numbers to sum
        
        returns
        -------
            int
                sum of the list"""
    if not numbers:
            return 0
    total = 0
    for number in numbers:
        total += number
    return total


def list_product(numbers: list) -> int:
    """" Function to multiply a list of numbers
    parameters
    ----------
        numbers : list
            list of numbers to multiply
        
        returns
        -------
            int
                product of the list"""
    if not numbers:
        return 1
    product = 1
    for number in numbers:
        product *= number
    return product
