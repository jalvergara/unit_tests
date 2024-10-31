"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import *


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
    """Test cases for the subtract function."""
    assert subtract(5, 3) == 2

def test_square():
    """Test cases for the square function."""
    assert square(5) == 25

def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(4) is True

def test_find_max():
    """Test cases for the find_max function."""
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_min():
    """Test cases for the find_min function."""
    assert find_min([1, 2, 3, 4, 5]) == 1

def test_find_mean():
    """Test cases for the find_mean function."""
    assert find_mean([1, 2, 3, 4, 5]) == 3.0

def test_find_median():
    """Test cases for the find_median function."""
    assert find_median([1, 2, 3, 4, 5]) == 3

def test_find_mode():
    """Test cases for the find_mode function."""
    assert find_mode([1, 2, 2, 3, 4, 5]) == 2

def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(5) == 120

def test_is_prime():
    """Test cases for the is_prime function."""
    assert is_prime(7) is True

def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    assert is_palindrome('racecar') is True

def test_reverse_string():
    """Test cases for the reverse_string function."""
    assert reverse_string('hello') == 'olleh'

def test_list_sum():
    """Test cases for the list_sum function."""
    assert list_sum([1, 2, 3, 4, 5]) == 15

def test_list_product():
    """Test cases for the list_product function."""
    assert list_product([1, 2, 3, 4, 5]) == 120