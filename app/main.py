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
    """Function to subtract two numbers

    Parameters
    ----------
    a : int
        first digit to subtract
    b : int
        second digit to subtract

    Returns
    -------
    int
        a '-' b
    """
    return a - b


def square(a: int) -> int:
    """Funtion to square a number 
    parameters
    ----------  
    a : int
        number to square
    -------
    int
        a squared
    """
    if not isinstance(a, (int)):  
        raise TypeError("The input must be a number (int)")
    
    return a ** 2


def is_even(x: int) -> bool:
    """Function to check if a number is even

    Parameters
    ----------
    x : int
        number to check

    Returns
    -------
    bool
        True if even, False otherwise
    """
    
    if not isinstance(x, (int)):  
        raise TypeError("The input must be a number (int)")
    
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """Function to find the maximum number in a list
    parameters
    ----------      
    numbers : list
        list of numbers
    returns
    ------- 
    int
        maximum number in the list

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers (int or float)")
    
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    max_value = numbers[0] 
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_min(numbers: list) -> int:
    """Function to find the minimum number in a list
    parameters
    ----------      
    numbers : list
        list of numbers
    
    returns
    ------- 
    int
        minimum number in the list

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers (int or float)")
    
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    min_value = numbers[0]  
    for num in numbers:
        if num < min_value: 
            min_value = num
    return min_value


def find_mean(numbers: list) -> float:
    """Function to find the mean of a list of numbers
    parameters
    ----------      
    numbers : list
        list of numbers
    returns
    -------
    float
        mean of the numbers in the list

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers (int or float)")
    
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean


def find_median(numbers: list) -> float:
    """Function to find the median of a list of numbers
    parameters
    ----------      
    numbers : list
        list of numbers
    returns
    -------
    float
        median of the numbers in the list

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers (int or float)")
    
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    numbers.sort()
    count = len(numbers)

    if count % 2 == 0:
        middle1 = numbers[count // 2 - 1]
        middle2 = numbers[count // 2]
        median = (middle1 + middle2) / 2
    else:
        median = numbers[count // 2]
    return median


def find_mode(numbers: list) -> int:
    """Function to find the mode of a list of numbers
    parameters
    ----------      
    numbers : list
        list of numbers
    returns
    -------
    int
        mode of the numbers in the list

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers (int or float)")
    
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    frecuency = {}
    for num in numbers:
        if num in frecuency:
            frecuency[num] += 1
        else:
            frecuency[num] = 1
    max_count = max(frecuency.values())
    moda = [num for num, count in frecuency.items() if count == max_count]
    if len(moda) > 1:
        raise ValueError("No unique mode found")
    return moda[0]


def factorial(n: int) -> int:
    """Function to calculate the factorial of a number
    parameters
    ----------      
    n : int
        number to calculate the factorial of
    returns
    -------
    int
        factorial of the number

    """
    if not isinstance(n, (int)):  
        raise TypeError("The input must be a number (int)")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    i = 1
    factorial = 1
    while (i <= n):
        factorial = factorial * i
        i = i + 1

    return factorial


def is_prime(n: int) -> bool:
    """Function to check if a number is prime
    parameters
    ----------      
    n : int
        number to check
    returns
    -------
    bool
        True if prime, False otherwise

    """
    if not isinstance(n, (int)):  
        raise TypeError("The input must be a number (int)")
    
    if n <= 1 or (n > 3 and (n % 2 == 0 or n % 3 == 0)):
        return False

    return all(n % i != 0 and n % (i + 2) != 0 for i in range(5, int(n ** 0.5) + 1, 6))



def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome
    parameters
    ----------      
    word : str
        word to check
    returns
    -------
    bool
        True if palindrome, False otherwise

    """
    if not isinstance(word, (str)):  
        raise TypeError("The input must be a string")
    if len(word) == 0:
        raise ValueError("The word is empty")
    
    word = word.lower()
    return word == word[::-1]


def reverse_string(string: str) -> str:
    """Function to reverse a string
    parameters
    ----------      
    string : str
        string to reverse
    returns
    -------
    str
        reversed string

    """
    if not isinstance(string, (str)):  
        raise TypeError("The input must be a string")
    if len(string) == 0:
        raise ValueError("The string is empty")
    
    return string[::-1]


def list_sum(numbers: list) -> int:
    """Function to sum a list of numbers
    parameters
    ----------      
    numbers : list
        list of numbers
    returns
    -------
    int
        sum of the numbers in the list

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers (int or float)")
    
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    return sum(numbers)


def list_product(numbers: list) -> int:
    """Function to multiply a list of numbers
    parameters
    ----------      
    numbers : list
        list of numbers
    returns
    -------
    int
        product of the numbers in the list

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers (int or float)")
    
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    
    multiplier = 1
    for num in numbers:
        multiplier *= num
    return multiplier


