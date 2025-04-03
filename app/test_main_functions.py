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


# Nicolas Cuaran
def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    assert subtract(-2, -3) == 1

def test_square():
    """Test cases for the square function."""
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0



def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True

def test_find_max():
    """Test cases for the find_max function."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-10, -5, 0, -1]) == 0
    assert find_max([100]) == 100
    with pytest.raises(ValueError):
        find_max([])

def test_find_min():
    """Test cases for the find_min function."""
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([-10, -5, 0, -1]) == -10
    assert find_min([100]) == 100
    with pytest.raises(ValueError):
        find_min([])

def test_find_mean():
    """Test cases for the find_mean function."""
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([1, 2, 3, 4, 5, 6]) == 3.5
    assert find_median([10, 20, 30, 40, 50]) == 30
    assert find_median([-10, -5, 0, 5, 10]) == 0
    assert find_median([100]) == 100
    with pytest.raises(ValueError):
        find_median([])

def test_find_median():
    """Test cases for the find_median function."""
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([1, 2, 3, 4, 5, 6]) == 3.5
    assert find_median([100]) == 100
    with pytest.raises(ValueError):
        find_median([])    

def test_find_mode():
    """Test cases for the find_mode function."""
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([100]) == 100
    assert find_mode([3, 3, 3, 3, 3]) == 3
    with pytest.raises(ValueError):
        find_mode([])

def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(5) == 120
    assert factorial(7) == 5040
    with pytest.raises(ValueError):
        factorial(-3)

def test_is_prime():
    """Test cases for the is_prime function."""
    assert is_prime(3) is True
    assert is_prime(4) is False

def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    assert is_palindrome("level") is True
    assert is_palindrome("hello") is False

def test_reverse_string():
    """Test cases for the reverse_string function."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"


def test_list_sum():
    """Test cases for the list_sum function."""
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([10, -5, 3, 7]) == 15


def test_list_product():
    """Test cases for the list_product function."""
    assert list_product([1, 2, 3, 4, 5]) == 120
    assert list_product([10, -5, 3, 7]) == -1050
    assert list_product([1, 0, 2, 3]) == 0