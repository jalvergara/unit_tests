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


# Camilo Buitrago
def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(10, 3) == 7
    assert subtract(20, 15) == 5
    assert subtract(5, 2) == 3


def test_square():
    """Test cases for the square function."""
    assert square(2) == 4
    assert square(8) == 64
    assert square(5) == 25


def test_is_even():
    """Test cases for the is even function."""
    assert is_even(15) is False
    assert is_even(10) is True
    assert is_even(18) is True


def test_find_max():
    """Test cases for the find max function."""
    assert find_max([12, 44, 2]) == 44
    assert find_max([13, 15, 1]) == 15
    assert find_max([20, 8, 64]) == 64


def test_find_min():
    """Test cases for the find min function."""
    assert find_min([51, 20, 18]) == 18
    assert find_min([30, 15, 1]) == 1
    assert find_min([120, 400, 850]) == 120


def test_find_mean():
    """Test cases for the find mean function."""
    assert find_mean([30, 12, 18]) == 20
    assert find_mean([20, 4, 4, 16]) == 11
    assert find_mean([6, 12, 30, 24, 18]) == 18


def test_find_median():
    """Test cases for the find median function."""
    assert find_median([1, 3, 15]) == 3
    assert find_median([51, 2, 20]) == 20
    assert find_median([1, 2, 3, 4, 5]) == 3


def test_find_mode():
    """Test cases for the find mode function."""
    assert find_mode([1, 1, 1, 9, 18, 9]) == 1
    assert find_mode([2, 2, 3, 18, 19, 3, 3]) == 3
    assert find_mode([20, 1, 35, 20, 12]) == 20


def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(2) == 2
    assert factorial(5) == 120
    assert factorial(7) == 5040


def test_is_prime():
    """Test cases for the factorial function."""

    with pytest.raises(
        ValueError
    ):
        is_prime(0)

    assert is_prime(5) is True
    assert is_prime(29) is True
    assert is_prime(30) is False


def test_is_palindrome():
    assert is_palindrome("somos") is True
    assert is_palindrome("reconocer") is True
    assert is_palindrome("almacen") is False


def test_reverse_string():
    assert reverse_string("amor") == "roma"
    assert reverse_string("los") == "sol"
    assert reverse_string("rata") == "atar"


def test_list_sum():
    assert list_sum([10, 20, 30]) == 60
    assert list_sum([45, 15, 80]) == 140
    assert list_sum([33, 33, 33]) == 99


def test_list_product():
    assert list_product([10, 2, 2]) == 40
    assert list_product([15, 3, 2]) == 90
    assert list_product([50, 8, 10]) == 4000