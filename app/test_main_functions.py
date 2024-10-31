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
    """Test cases for the divide function."""
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
    """Test cases for the db_query function."""
    with mock.patch('app.main.db_query', return_value='DATA: [1, 2, 3]') as mock_db_query:
        assert db_query() == 'DATA: [1, 2, 3]'


def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5

def test_square():
    """Test cases for the square function."""
    assert square(4) == 16
    assert square(-3) == 9
    assert square(0) == 0

def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(4) is True
    assert is_even(5) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False

def test_find_max():
    """Test cases for the find_max function."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-5, -2, -3, -1]) == -1
    assert find_max([7]) == 7

def test_find_min():
    """Test cases for the find_min function."""
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([-5, -2, -3, -1]) == -5
    assert find_min([7]) == 7

def test_find_mean():
    """Test cases for the find_mean function."""
    assert find_mean([1, 2, 3, 4, 5]) == 3.0
    assert find_mean([5, 5, 5, 5]) == 5.0
    assert find_mean([-2, -4, -6]) == -4.0

def test_find_median():
    """Test cases for the find_median function."""
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([5]) == 5

def test_find_mode():
    """Test cases for the find_mode function."""
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([5, 5, 5, 5]) == 5
    assert find_mode([1, 2, 3, 4, 4, 4, 4]) == 4

def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    """Test cases for the is_prime function."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(13) is True
    assert is_prime(1) is False
    assert is_prime(-3) is False

def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    assert is_palindrome('radar') is True
    assert is_palindrome('hello') is False
    assert is_palindrome('ana') is True

def test_reverse_string():
    """Test cases for the reverse_string function."""
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('') == ''
    assert reverse_string('a') == 'a'

def test_list_sum():
    """Test cases for the list_sum function."""
    assert list_sum([1, 2, 3, 4]) == 10
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([0]) == 0

def test_list_product():
    """Test cases for the list_product function."""
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([2, -2]) == -4
    assert list_product([1]) == 1
