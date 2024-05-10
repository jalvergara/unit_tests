"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract, square, is_even, find_max, find_min, find_mean, find_median, find_mode, factorial, is_prime, is_palindrome, reverse_string, list_sum, list_product


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


# Vanessa Suarez
def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(8, 4) == 4
    assert subtract(0, 0) == 0


def test_square():
    """Test cases for the square function."""
    assert square(2) == 4
    assert square(1) == 1
    assert square(0) == 0



def test_is_even():
    """Test cases for the is even function."""
    assert is_even(7) is False
    assert is_even(4) is True
    assert is_even(10) is True


def test_find_max():
    """Test cases for the find max function."""
    assert find_max([5, 6, 8]) == 8
    assert find_max([10, 15, 12]) == 15
    assert find_max([80, 18, 64]) == 80


def test_find_min():
    """Test cases for the find min function."""
    assert find_min([5, 6, 8]) == 5
    assert find_min([10, 15, 12]) == 10
    assert find_min([80, 18, 64]) == 18


def test_find_mean():
    """Test cases for the find mean function."""
    assert find_mean([9, 12, 15]) == 12
    assert find_mean([2, 4, 6, 8]) == 5
    assert find_mean([5, 10, 15, 20, 25]) == 15


def test_find_median():
    """Test cases for the find median function."""
    assert find_median([9, 12, 15]) == 12
    assert find_median([2, 4, 8]) == 4
    assert find_median([5, 18, 32, 22, 25]) == 22


def test_find_mode():
    """Test cases for the find mode function."""
    assert find_mode([9, 12, 15, 9, 11, 17]) == 9
    assert find_mode([2, 4, 8, 6, 8]) == 8
    assert find_mode([5, 18, 32, 22, 18]) == 18


def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(0) == 1


def test_is_prime():
    """Test cases for the factorial function."""

    with pytest.raises(
        ValueError
    ):
        is_prime(0)

    assert is_prime(5) is True
    assert is_prime(4) is False


def test_is_palindrome():
    assert is_palindrome("allivessevilla") is True
    assert is_palindrome("somosonosomos") is True
    assert is_palindrome("trestigrescomentrigo") is False


def test_reverse_string():
    assert reverse_string("calor") == "rolac"
    assert reverse_string("palmera") == "aremlap"
    assert reverse_string("madera") == "aredam"


def test_list_sum():
    assert list_sum([9, 11, 17]) == 37
    assert list_sum([8, 6, 8]) == 22
    assert list_sum([32, 22, 18]) == 72


def test_list_product():
    assert list_product([9, 2, 7]) == 126
    assert list_product([2, 6, 8]) == 96
    assert list_product([5, 8, 2]) == 80
