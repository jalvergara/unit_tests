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
    """Casos de prueba para la función subtract."""
    assert subtract(10, 5) == 5
    assert subtract(-5, -3) == -2
    assert subtract(0, 0) == 0
    assert subtract(5, -3) == 8
    assert subtract(-3, 5) == -8
    assert subtract(1, 0) == 1
    assert subtract(0, 1) == -1
    assert subtract(1000000, 999999) == 1
    assert subtract(-1000000, -1000000) == 0


def test_square():
    """Casos de prueba para la función square."""
    assert square(5) == 25
    assert square(-5) == 25
    assert square(0) == 0
    assert square(1000) == 1000000
    assert square(-1000) == 1000000
    assert square(1) == 1
    assert square(-1) == 1 

def test_is_even():
    """Casos de prueba para la función is_even."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False
    assert is_even(1000000) is True
    assert is_even(1000001) is False

def test_find_max():
    """Casos de prueba para la función find_max."""
    assert find_max([1, 2, 3]) == 3
    assert find_max([-1, -2, -3]) == -1
    assert find_max([0, 0, 0]) == 0
    assert find_max([100, 200, 300]) == 300
    assert find_max([5]) == 5
    assert find_max([1, 2, 3, -1, 1000, 4]) == 1000

def test_find_min():
    """Casos de prueba para la función find_min."""
    assert find_min([1, 2, 3]) == 1
    assert find_min([-1, -2, -3]) == -3
    assert find_min([0, 0, 0]) == 0
    assert find_min([100, 200, 300]) == 100
    assert find_min([5]) == 5
    assert find_min([1, 2, 3, -1, 1000, 4]) == -1

def test_find_mean():
    """Casos de prueba para la función find_mean."""
    assert find_mean([1, 2, 3]) == 2.0
    assert find_mean([10, 20, 30, 40]) == 25.0
    assert find_mean([-1, -2, -3]) == -2.0
    assert find_mean([5]) == 5.0
    assert find_mean([]) == 0.0

def test_find_median():
    """Casos de prueba para la función find_median."""
    assert find_median([1, 2, 3]) == 2.0
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([10, 20, 30, 40, 50]) == 30.0
    assert find_median([5]) == 5.0
    assert find_median([-1, -2, -3, -4]) == -2.5

def test_find_mode():
    """Casos de prueba para la función find_mode."""
    assert find_mode([1, 2, 2, 3]) == 2
    assert find_mode([4, 4, 5, 5, 5]) == 5
    assert find_mode([1, 2, 3, 4, 4, 4, 2, 2, 2]) == 2
    assert find_mode([5]) == 5
    assert find_mode([]) is None

def test_factorial():
    """Casos de prueba para la función factorial."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    try:
        factorial(-5)
    except ValueError:
        assert True

def test_is_prime():
    """Casos de prueba para la función is_prime."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(18) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-3) is False

def test_is_palindrome():
    """Casos de prueba para la función is_palindrome."""
    assert is_palindrome("madam") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("a") is True
    assert is_palindrome("") is True
    assert is_palindrome("noon") is True

def test_reverse_string():
    """Casos de prueba para la función reverse_string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("12345") == "54321"

def test_list_sum():
    """Casos de prueba para la función list_sum."""
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([0, 0, 0]) == 0
    assert list_sum([100]) == 100
    assert list_sum([]) == 0

def test_list_product():
    """Casos de prueba para la función list_product."""
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([-1, 2, -3]) == 6
    assert list_product([5]) == 5
    assert list_product([1, 0, 3]) == 0
    assert list_product([]) == 0