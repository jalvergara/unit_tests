"""Unit testing for the project."""

import pandas as pd
import pytest
import math
from unittest import mock
from statistics import StatisticsError

from .main import (
    add,
    divide,
    validate_no_null_values,
    db_query,
    subtract,
    square,
    is_even,
    find_max,
    find_min,
    find_mean,
    find_median,
    find_mode,
    factorial,
    is_prime,
    is_palindrome,
    reverse_string,
    list_sum,
    list_product
)

def test_add():
    """Test cases for the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    """Test cases for zero division"""

    with pytest.raises(
        ValueError
    ):
        divide(1, 0)

    assert divide(6, 2) == 3.0


def test_validate_no_null_values():
    """Test cases for the validate_no_null_values function."""
    # Create a DataFrame with no null values
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    assert validate_no_null_values(df1) is True

    # Create a DataFrame with null values
    df2 = pd.DataFrame({'A': [1, 2, None], 'B': ['a', None, 'c']})
    assert validate_no_null_values(df2) is False


def test_db_query():
    """Test case for the db_query function."""
    with mock.patch('app.main.db_query', return_value='DATA: [1, 2, 3]') as mock_db_query:
        assert db_query() == 'DATA: [1, 2, 3]'


def test_subtract():
    """Test case for the subtract function."""

    assert subtract(0,0) == 0
    assert subtract(-1,1) == -2
    assert subtract(-3,-2) == -1  


def test_square():
    """Test cases for the square function."""

    assert square(-1) == 1
    assert square(11) == 121


def test_is_even():
    """Test cases for the is_even function."""

    assert is_even(-2) is True 
    assert is_even(11) is False
    assert is_even(0) is True


def test_find_max():
    """"Tests cases for the find_max function"""

    with pytest.raises(ValueError):
        find_max([])
    
    assert find_max([3, 1, 4, 2]) == 4
    assert find_max([-5, -2, -8, -1]) == -1
    assert find_max([1.5, 2, 3.3, 0]) == 3.3
    assert find_max([10]) == 10


def test_find_min():
    """Tests cases for the find_min function"""
    
    with pytest.raises(ValueError):
        find_min([])

    assert find_min([3, 1, 4, 2]) == 1
    assert find_min([-5, -2, -8, -1]) == -8
    assert find_min([1.5, 2, 3.3, 0]) == 0
    assert find_min([10]) == 10


def test_find_mean():
    """Tests cases for the find_mean function"""
    
    with pytest.raises(ValueError):
        find_mean([])

    assert find_mean([3, 1, 4, 2]) == 2.5
    assert find_mean([-5, -2, -8, -1]) == -4
    assert find_mean([1.5, 2, 3.3, 0]) == 1.7
    assert find_mean([10]) == 10
    assert find_mean([2, 2, 2, 2]) == 2


def test_find_median():
    """Tests cases for the find_median function"""
    
    with pytest.raises(ValueError):
        find_median([])

    assert find_median([3, 1, 4]) == 3
    assert find_median([3, 1, 4, 2]) == 2.5
    assert find_median([42]) == 42
    assert find_median([1.5, 2.5, 3.5]) == 2.5
    assert find_median([-5, -1, -3]) == -3
    assert find_median([-5, -1, -3, -4]) == -3.5
    assert find_median([-4,4]) == 0
    assert find_median([1, 2, 3]) == find_median([3, 1, 2]) == 2
    assert find_median([2, 2, 2, 2]) == 2



def test_find_mode():
    """Tests cases for the find_mode function"""
    
    with pytest.raises(ValueError):
        find_mode([])
    

    assert find_mode([1, 2, 2, 3, 3, 3]) == 3
    assert find_mode([-1, -2, -3, -1]) == -1
    assert find_mode([1.5, 2.5, 1.5, 3.0]) == 1.5
    assert find_mode([1, 2, 3]) == 1
    assert find_mode([1,1,2,2]) == 1
    assert find_mode([5, 5, 5, 5]) == 5
    assert find_mode([-2, -2, 1, 1, -2]) == -2
    assert find_mode([10]) == 10
    assert find_mode([1, 2, 3]) == 1




def test_factorial():
    """Tests cases for the factorial function"""
    with pytest.raises(TypeError):
        factorial(2.5)

    with pytest.raises(ValueError):
        factorial(-1)

    assert factorial(0) == 1  
    assert factorial(1) == 1  
    assert factorial(5) == 120  
    assert factorial(10) == 3628800


def test_is_prime():
    """Tests cases for the is_prime function"""
    with pytest.raises(ValueError):
        is_prime(-2)

    with pytest.raises(ValueError):
        is_prime(0)

    with pytest.raises(ValueError):
        is_prime(1)


    assert is_prime(3) is True
    assert is_prime(12) is False


def test_is_palindrome():
    """Tests cases for the is_palindrome function"""
    with pytest.raises(TypeError):  
        is_palindrome(123)  

    with pytest.raises(ValueError):  
        is_palindrome("")  

                             
    assert is_palindrome("eye") is True
    assert is_palindrome("hi") is False
    # Test for single-character string
    assert is_palindrome("a") is True
    # Test for mixed-case palindrome
    assert is_palindrome("Racecar") is True
    # Test for phrase with spaces/punctuation
    assert is_palindrome("A man, a plan, a canal, Panama".replace(" ", "").replace(",", "").lower()) is True


def test_reverse_string():
    """Tests cases for the reverse_string function"""

    
    assert reverse_string("road") == "daor"
    assert reverse_string("madam") == "madam"
    assert reverse_string("a") == "a"
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("123!@#") == "#@!321"


def test_list_sum():
    """Tests cases for the list_sum function"""

    with pytest.raises(ValueError):  
        list_sum("")
    
    assert list_sum([1, 2, 3, 4]) == 10
    assert list_sum([-2, 4.5]) == 2.5
    assert list_sum([1.5, 2.5, 3.0]) == 7.0
    assert list_sum([1, 2.5, 3]) == 6.5
    assert list_sum([12]) == 12


def test_list_product():
    """Tests cases for the list_product function"""

    with pytest.raises(ValueError):  
        list_product("")
    
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([-2, 4.5]) == -9
    assert list_product([1.5, 2.5, 3.0]) == 11.25
    assert list_product([1, 2.5, 3]) == 7.5
    assert list_product([5]) == 5