"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract, square, is_even, find_max, find_min, find_mean
from .main import find_median, find_mode, factorial, is_prime, is_palindrome, reverse_string, list_sum, list_product

def test_add():
    """Test cases for the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    """Test case for zero division"""

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


# Alejandro Vergara
def test_subtract():
    assert subtract(4, 3) == 1
    assert subtract(-4, -3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0


def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-3) == 9


def test_is_even():
   assert is_even(6) is True
   assert is_even(123) is False
   assert is_even(0) is True
   assert is_even(-562) is True
   assert is_even(-89) is False


def test_find_max():
    assert find_max([2,7,5,1,9]) == 9
    assert find_max([-1,-10,-25,-100,-42]) == -1
    assert find_max([-100,-67,-32,50,91,-82,1000,0,-1,751,65]) == 1000
    assert find_max([]) == None


def test_find_min():
    assert find_min([2,7,5,1,9]) == 1
    assert find_min([-1,-10,-25,-100,-42]) == -100
    assert find_min([-100,-67,-32,50,91,-82,1000,0,-1,751,65,-891]) == -891
    assert find_min([]) == None


def test_find_mean():
    assert find_mean([12, 25, 7, 45, 30, 19]) == 23.0
    assert find_mean([-15, -34, -8, -21, -5, -19]) == -17.0
    assert find_mean([10, -3, 22, -14, 7, -9, 31, -12, 4, -6]) == 3.0
    assert find_mean([]) == None


def test_find_median():
    assert find_median([12, 25, 7, 45, 30, 19]) == 22.0
    assert find_median([-15, -34, -8, -21, -5]) == -15.0
    assert find_median([10, -3, 22, -14, 7, -9, 31, -12, 4]) == 4.0
    assert find_median([]) == None


def test_find_mode():
    assert find_mode([1, 2, 2, 3, 4]) == 2 
    assert find_mode([1, 1, 2, 2, 3, 3]) == [1, 2, 3]   
    assert find_mode([1, 2, 3, 4, 5]) == None   
    assert find_mode([]) == None


def test_factorial():
    assert factorial(5) == 120 
    assert factorial(0) == 1  
    assert factorial(1) == 1 
    assert factorial(-3) == None 


def test_is_prime():
    assert is_prime(5) == True 
    assert is_prime(10) == False 
    assert is_prime(13) == True 
    assert is_prime(1) == False
    assert is_prime(3) == True
    assert is_prime(49) == False
    assert is_prime(113) == True


def test_is_palindrome():
    assert is_palindrome("radar") == True     
    assert is_palindrome("Aloha") == False        
    assert is_palindrome("Racecar") == True     
    assert is_palindrome("Mascar") == False       



def test_reverse_string():
    assert reverse_string("hello") == "olleh"   
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("12345") == "54321"


def test_list_sum():
    assert list_sum([1,2,3,4,5,6,7]) == 28
    assert list_sum([10,20,30,40,50]) == 150
    assert list_sum([34,19,208,2109,6]) == 2376 
    assert list_sum([]) == None


def test_list_product():
    assert list_product([1, 2, 3, 4, 5]) == 120   # Output: 120 (1 * 2 * 3 * 4 * 5)
    assert list_product([10, 0.5, 3]) == 15      # Output: 15 (10 * 0.5 * 3)
    assert list_product([]) == 1
    assert list_product([5]) == 5
