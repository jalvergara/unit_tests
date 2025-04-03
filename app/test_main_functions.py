"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import (
    add, divide, validate_no_null_values, db_query, subtract, square, 
    is_even, find_max, find_min, find_mean, find_median, find_mode, 
    factorial, is_prime, is_palindrome, reverse_string, list_sum, list_product
)


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


# Daniel Contreras
def test_subtract():
    """test cases for the subtract function"""
    assert subtract(2, 1) == 1
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0


def test_square():
    """test cases for the square function"""
    assert square(2) == 4
    assert square(0) == 0
    assert square(-3) == 9


def test_is_even():
    """"test cases for the is_even function"""
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True


def test_find_max():
    """test cases for the find_max function"""
    assert find_max([2, 5, 8]) == 8
    assert find_max([0, 0, 0]) == 0
    assert find_max([-1, -5, -7]) == -1


def test_find_min():
    assert find_min([2, 5, 8]) == 2
    assert find_min([0, 0, 0]) == 0
    assert find_min([-1, -5, -7]) == -7


def test_find_mean():
    assert find_mean([2, 5, 8]) == 5.0
    assert round(find_mean([-1, -6, 6]), 2) == -0.33


def test_find_median():
    """test cases for the fnd_median function"""
    assert find_median([2, 5, 8]) == 5
    assert find_median([0, 0, 0]) == 0
    assert find_median([8, 4]) == 6
    assert find_median([1]) == 1


def test_find_mode():
    assert find_mode([10, 5, 23, 3, 5]) == 5
    assert find_mode([-3, 5, 7, -3, -4]) == -3
    assert find_mode([3, 5, 6]) == "No hay números repetidos"



def test_factorial():
    """test cases for the factorial function"""
    assert factorial(5) == 120
    assert factorial(0) == 1

    with pytest.raises(ValueError, match="El factorial no está definido para *."):
        factorial(-3)


def test_is_prime():
    """test cases for the is_prime function"""
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(7) == True
    assert is_prime(0) == False
    assert is_prime(-1) == False


def test_is_palindrome():
    """test cases for the is_palindrome function"""
    assert is_palindrome("radar") == True
    assert is_palindrome("casa") == False
    assert is_palindrome("ana") == True
    assert is_palindrome("15") == False


def test_reverse_string():
    """test cases for the reverse_string function"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("radar") == "radar"
    assert reverse_string("35") == "53"


def test_list_sum():
    """test cases for the list_sum function"""
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([0, 0, 0]) == 0
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([]) == 0


def test_list_product():
    """test cases for the list_product function"""
    assert list_product([1, 2, 3]) == 6
    assert list_product([0, 0, 0]) == 0
    assert list_product([5, 12, 4]) == 240