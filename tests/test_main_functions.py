"""Unit testing for the project."""

import pandas as pd
import pytest
from unittest import mock
import sys
sys.path.append(".")

from app.main import *


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


def test_subtract():
   assert subtract(8, 5) == 3
   assert subtract(10, 15) == -5
   assert subtract(0, 0) == 0
   assert subtract(-8, -2) == -6
   assert subtract(-10, 4) == -14


def test_square():
    # TODO: write the tests cases for the square function
    assert square(5) == 25
    assert square(1) == 1
    assert square(-7) == 49



def test_is_even():
    # TODO: write the tests cases for the is_even function
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(9) is False


def test_find_max():
    # TODO: write the tests cases for the find_max function
    assert find_max([1, 5, 3, 9]) == 9
    assert find_max([-1, -5, -3]) == -1
    assert find_max([3, 7, 12, 1]) == 12


def test_find_min():
    # TODO: write the tests cases for the find_min function
    assert find_min([1, 5, 3, 9]) == 1
    assert find_min([-1, -5, -3]) == -5
    assert find_min([-3, -7, -1]) == -7


def test_find_mean():
    # TODO: write the tests cases for the find_mean function
    assert find_mean([1, 2, 3, 4, 5]) == 3.0
    assert find_mean([10, 20, 30]) == 20.0
    assert find_mean([20, 40, 60]) == 40.0


def test_find_median():
    # TODO: write the tests cases for the find_median function
    assert find_median([1, 3, 5]) == 3
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([2, 4, 6]) == 4
    assert find_median([2, 4, 6, 8]) == 5.0


def test_find_mode():
    # TODO: write the tests cases for the find_mode function
    assert find_mode([1, 2, 2, 3, 3, 3]) == 3
    assert find_mode([4, 4, 5, 5, 5, 4]) == 4  
    assert find_mode([5, 6, 6, 7, 7, 7]) == 7
    assert find_mode([8, 8, 9, 9, 9, 8]) == 8


def test_factorial():
    # TODO: write the tests cases for the factorial function
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(6) == 720
    with pytest.raises(ValueError):
        factorial(-3)


def test_is_prime():
    # TODO: write the tests cases for the is_prime function
    assert is_prime(7) is True
    assert is_prime(10) is False
    assert is_prime(2) is True
    assert is_prime(15) is False


def test_is_palindrome():
    # TODO: write the tests cases for the is_palindrome function
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("world") is False


def test_reverse_string():
    # TODO: write the tests cases for the reverse_string function
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("98765") == "56789"

def test_list_sum():
    # TODO: write the tests cases for the list_sum function
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([4, 5, 6]) == 15
    assert list_sum([-2, -4, -6]) == -12



def test_list_product():
    # TODO: write the tests cases for the list_product function
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([-1, 2, -3]) == 6
    assert list_product([2, 3, 4, 5]) == 120
    assert list_product([-2, 3, -4]) == 24

