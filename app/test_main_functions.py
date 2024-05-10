"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract, square, is_even, find_max


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
    assert subtract(5, 2) == 3
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0 


def test_square():
    """Test cases for the square function."""
    assert square(0) == 0
    assert square(25) == 25


def test_is_even():
    """Test cases for the is even function."""
    assert is_even(4) == True
    assert is_even(7) == False

def test_find_max():
    """Test cases for the find max function."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-5, -4, -3, -2, -1]) == -1


def test_find_min():
    # TODO: write the tests cases for the find_min function
    pass


def test_find_mean():
    # TODO: write the tests cases for the find_mean function
    pass


def test_find_median():
    # TODO: write the tests cases for the find_median function
    pass


def test_find_mode():
    # TODO: write the tests cases for the find_mode function
    pass


def test_factorial():
    # TODO: write the tests cases for the factorial function
    pass


def test_is_prime():
    # TODO: write the tests cases for the is_prime function
    pass


def test_is_palindrome():
    # TODO: write the tests cases for the is_palindrome function
    pass


def test_reverse_string():
    # TODO: write the tests cases for the reverse_string function
    pass


def test_list_sum():
    # TODO: write the tests cases for the list_sum function
    pass


def test_list_product():
    # TODO: write the tests cases for the list_product function
    pass
