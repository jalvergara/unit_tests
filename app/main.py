""" Main functions to explain unit testing """

import pandas as pd

def add(a: int, b: int) -> int:
    """ Function to add two numbers

    Parameters
    ----------
    a : int
        first digit to add
    b : int
        second digit to add

    Returns
    -------
    int
        a + b
    """
    return a + b


def divide(a: int, b: int) -> float:
    """ Function to divide two numbers

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
        Zero division error
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")

    return a / b


# Function to validate that a Pandas DataFrame has no null values
def validate_no_null_values(df: pd.DataFrame) -> bool:
    """ Validate if the DataFrame has no null values

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to validate

    Returns
    -------
    bool
        True if no null values, False otherwise
    """
    return not df.isnull().values.any()


def db_query() -> str:
    """ Function to mock a database query

    Returns
    -------
    str
        mocked database query
    """
    return "DATA: [1, 2, 3]"

def subtract(a: int, b: int) -> int:
    """ Function to subtract two numbers

    Parameters
    ----------
    a : int
        first digit to subtract
    b : int
        second digit to subtract

    Returns
    -------
    int
        a - b

    Raises
    ------
    TypeError
        Invalid type: both a and b must be integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Invalid type: both a and b must be integers")
    return a - b


def square(a: int) -> int:
    """ Function to calculate the square of a number

    Parameters
    ----------
    a : int
        number to be squared

    Returns
    -------
    int
        a squared

    Raises
    ------
    TypeError
        Invalid type: a must be an integer
    """
    if not isinstance(a, int):
        raise TypeError("Invalid type: a must be an integer")
    return a ** 2


def is_even(x: int) -> bool:
    """ Function to check if a number is even

    Parameters
    ----------
    x : int
        number to check

    Returns
    -------
    bool
        True if x is even, False otherwise

    Raises
    ------
    TypeError
        Invalid type: x must be an integer
    """
    if not isinstance(x, int):
        raise TypeError("Invalid type: x must be an integer")    
    return x % 2 == 0


def find_max(numbers: list) -> int:
    """ Function to find the maximum number in a list

    Parameters
    ----------
    numbers : list
        list of numbers to find the maximum from

    Returns
    -------
    int
        maximum number in the list

    Raises
    ------
    TypeError
        All elements in the list must be numbers
    ValueError
        The list is empty or has only one element
    """
    # Check that all elements in the list are numbers
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    if not numbers:  # Check if the list is empty
        raise ValueError("The list is empty")
    elif len(numbers) == 1:  # Check if the list has only one element
        raise ValueError("The list has only one element")
    else:
        max_number = numbers[0]  # Assign the first number as the initial maximum
        for number in numbers:
            if number > max_number:
                max_number = number  # Update max_number if a larger number is found
        return max_number


def find_min(numbers: list) -> int:
    """ Function to find the minimum number in a list

    Parameters
    ----------
    numbers : list
        list of numbers to find the minimum from

    Returns
    -------
    int
        minimum number in the list

    Raises
    ------
    TypeError
        All elements in the list must be numbers
    ValueError
        The list is empty or has only one element
    """
    # Check that all elements in the list are numbers
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    if not numbers:  # Check if the list is empty
        raise ValueError("The list is empty")
    elif len(numbers) == 1:  # Check if the list has only one element
        raise ValueError("The list has only one element")
    else:
        min_number = numbers[0]  # Assign the first number as the initial minimum
        for number in numbers:
            if number < min_number:
                min_number = number  # Update min_number if a smaller number is found
        return min_number


def find_mean(numbers: list) -> float:
    """ Function to calculate the mean of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers to calculate the mean from

    Returns
    -------
    float
        mean of the numbers in the list

    Raises
    ------
    TypeError
        All elements in the list must be numbers
    ValueError
        The list is empty
    """
    # Check that all elements in the list are numbers
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
        
    if not numbers:  # Check if the list is empty
        raise ValueError("The list is empty")
    
    elif len(numbers) == 1:
        return numbers[0]  # Return the only number in the list
    
    else:
        total_sum = 0
        count = 0
        for number in numbers:
            total_sum += number
            count += 1
        # Calculate and return the mean
        return total_sum / count


def find_median(numbers: list) -> float:
    """ Function to calculate the median of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers to calculate the median from

    Returns
    -------
    float
        median of the numbers in the list

    Raises
    ------
    TypeError
        All elements in the list must be numbers
    ValueError
        The list is empty
    """
    # Check that all elements in the list are numbers
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
        
    if not numbers:  # Check if the list is empty
        raise ValueError("The list is empty")
    
    elif len(numbers) == 1:
        return numbers[0]
    
    else:
        # Sort the list manually
        sorted_numbers = sorted(numbers)  # This uses sort but does not depend on external libraries
        n = len(sorted_numbers)

        # Calculate and return the median
        mid = n // 2
        if n % 2 == 1:  # If the number of elements is odd
            return sorted_numbers[mid]
        else:  # If the number of elements is even
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2


def find_mode(numbers: list) -> int:
    """ Function to find the mode of a list of numbers

    Parameters
    ----------
    numbers : list
        list of numbers to find the mode from

    Returns
    -------
    int
        mode of the numbers in the list

    Raises
    ------
    TypeError
        All elements in the list must be numbers
    ValueError
        The list is empty
    """
    # Check that all elements in the list are numbers
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    
    if not numbers:  # Check if the list is empty
        raise ValueError("The list is empty")
    
    elif len(numbers) == 1:
        return numbers[0]
    else:
        # Create a dictionary to count the frequency of each number
        frequency = {}
        for number in numbers:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1

        # Find the number with the highest frequency
        max_count = max(frequency.values())
        mode_values = [key for key, count in frequency.items() if count == max_count]
        
        # Return the lowest mode in case of multiple modes
        return min(mode_values) if len(mode_values) > 1 else mode_values[0]
    

def factorial(n: int) -> int:
    """ Function to calculate the factorial of a number

    Parameters
    ----------
    n : int
        number to calculate the factorial of

    Returns
    -------
    int
        factorial of n

    Raises
    ------
    ValueError
        n must be a non-negative integer
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1  # Base case for factorial
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i  # Multiply result by each number from 2 to n
        return result

def reverse_string(s: str) -> str:
    """ Function to reverse a string

    Parameters
    ----------
    s : str
        string to reverse

    Returns
    -------
    str
        reversed string

    Raises
    ------
    TypeError
        Invalid type: s must be a string
    """
    if not isinstance(s, str):
        raise TypeError("Invalid type: s must be a string")
    return s[::-1]  # Reversing string using slicing

def is_palindrome(s: str) -> bool:
    """ Function to check if a string is a palindrome

    Parameters
    ----------
    s : str
        string to check

    Returns
    -------
    bool
        True if s is a palindrome, False otherwise

    Raises
    ------
    TypeError
        Invalid type: s must be a string
    """
    if not isinstance(s, str):
        raise TypeError("Invalid type: s must be a string")
    return s == s[::-1]  # Check if string is equal to its reverse
