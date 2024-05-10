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


# Alejandro Vergara
def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(3, 2) == 1
    assert subtract(1, 1) == 0


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    assert square(6) == 36


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(6) == True


def test_find_max():
    assert find_max([1, 2, 3]) == 3
    assert find_max([-1, -2, -3]) == -1
    assert find_max([0, 0, 0]) == 0
    assert find_max([5, 2, 9, 1, 7]) == 9
    assert find_max([10, 20, 30, 40, 50]) == 50


def test_find_min():
    assert find_min([1, 2, 3]) == 1
    assert find_min([-1, -2, -3]) == -3
    assert find_min([0, 0, 0]) == 0
    assert find_min([5, 2, 9, 1, 7]) == 1
    assert find_min([10, 20, 30, 40, 50]) == 10


def test_find_mean():
    assert find_mean([1, 2, 3]) == 2
    assert find_mean([-1, -2, -3]) == -2
    assert find_mean([0, 0, 0]) == 0
    assert find_mean([5, 2, 9, 1, 7]) == 4.8
    assert find_mean([10, 20, 30, 40, 50]) == 30

def test_find_median():
    assert find_median([1, 2, 3]) == 2
    assert find_median([-1, -2, -3]) == -2
    assert find_median([0, 0, 0]) == 0
    assert find_median([5, 2, 9, 1, 7]) == 5
    assert find_median([10, 20, 30, 40, 50]) == 30

def test_find_mode():
    assert find_mode([1, 2, 2, 3]) == 2
    assert find_mode([1, 2, 2, 3, 3]) == 2
    assert find_mode([1, 2, 2, 3, 3, 4, 4]) == 2
    assert find_mode([1, 2, 3, 3, 3]) == 3
    assert find_mode([1, 2, 3, 4, 5, 5]) == 5


def test_factorial():
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6
    assert factorial(2) == 2
    assert factorial(1) == 1


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False


def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('level') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('madam') == True
    assert is_palindrome('python') == False

def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('python') == 'nohtyp'
    assert reverse_string('java') == 'avaj'
    assert reverse_string('django') == 'ognajd'
    assert reverse_string('ETL') == 'LTE'


def test_list_sum():
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([0, 0, 0]) == 0
    assert list_sum([5, 2, 9, 1, 7]) == 24
    assert list_sum([10, 20, 30, 40, 50]) == 150


def test_list_product():
    assert list_product([1, 2, 3]) == 6
    assert list_product([-1, -2, -3]) == -6
    assert list_product([0, 0, 0]) == 0
    assert list_product([5, 2, 9, 1, 7]) == 630
    assert list_product([10, 20, 30, 40, 50]) == 12000000
