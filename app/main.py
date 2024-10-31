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
    return a -b

def square(a: int) -> int:
    return a**2


def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False


def find_max(numbers: list) -> int:
    if not numbers:
        return None  
    
    max_num = max(numbers)
    return max_num


def find_min(numbers: list) -> int:
    if not numbers:
        return None 
    
    min_num = min(numbers)
    return min_num


def find_mean(numbers: list) -> float:
    if not numbers:
        return None 
    
    average = sum(numbers) / len(numbers)
    return average


def find_median(numbers: list) -> float:
    if not numbers:
        return None  
    
    sorted_numbers = sorted(numbers) 
    mid = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    
    return median


def find_mode(numbers: list) -> int:
    if not numbers:
        return None 

    frequency_dict = {}
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1

    max_frequency = max(frequency_dict.values())

    modes = [num for num, freq in frequency_dict.items() if freq == max_frequency]

    if len(modes) == len(numbers):
        return None  
    
    return modes if len(modes) > 1 else modes[0]


def factorial(n: int) -> int:
    if n < 0:
        return None  # No existe el factorial para números negativos
    if n == 0 or n == 1:
        return 1 
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    if n <= 1:
        return False 
    elif n <= 3:
        return True 

    if n % 2 == 0 or n % 3 == 0:
        return False  
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def is_palindrome(word: str) -> bool:
    cleaned_word = word.replace(" ", "").lower()

    return cleaned_word == cleaned_word[::-1]


def reverse_string(string: str) -> str:
    return string[::-1]

def list_sum(numbers: list) -> int:

    if not numbers:
        return None
    
    return sum(numbers)
    


def list_product(numbers: list) -> int:
    if not numbers:
        return 1  # Retorna 1 para listas vacías, ya que es el elemento neutro de la multiplicación
    
    product = 1
    for num in numbers:
        product *= num
    return product
