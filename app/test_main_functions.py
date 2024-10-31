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
    assert subtract(3, 2) == 1
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0


def test_square():
    """Test cases for the square function."""
    assert square(1) == 1
    assert square(2) == 4
    assert square(-2) == 4
    assert square(0) == 0



def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(0) == True
    assert is_even(4) == True
    assert is_even(-4) == True
    assert is_even(1) == False
    assert is_even(-1) == False


def test_find_max():
    assert find_max([1, 2, 5, 7]) == 7
    assert find_max([-5, -2, -9]) == -2
    assert find_max([-1, 2, 0, 5]) == 5
    assert find_max([-1, -1, -1]) == -1
    assert find_max([11]) == 11
    
    with pytest.raises(ValueError):
        find_max([])


def test_find_min():
    assert find_min([1, 2, 5, 7]) == 1
    assert find_min([-5, -2, -9]) == -9
    assert find_min([-1, 2, 0, 5]) == -1
    assert find_min([11]) == 11
    
    with pytest.raises(ValueError):
        find_min([])

def test_find_mean():
    assert find_mean([1, 2, 5, 7]) == 3.75
    assert find_mean([-5, -2, -9]) == -5.333333333333333
    assert find_mean([-1, 2, 0, 5]) == 1.5
    assert find_mean([10]) == 10.0
    
    with pytest.raises(ValueError):
        find_mean([])


def test_find_median():
    assert find_median([1, 2, 5, 7]) == 3.5
    assert find_median([1, 3, 3, 6, 7, 8, 9]) == 6
    assert find_median([-5, -2, -9]) == -5
    assert find_median([-1, 2, 0, 5]) == 1.0
    assert find_median([11]) == 11
    assert find_median([11,11,11]) == 11
    
    with pytest.raises(ValueError):
        find_median([])



def test_find_mode():
    assert find_mode([1, 2, 2, 5, 7]) == 2
    assert find_mode([-5, -2, -9, -2]) == -2
    assert find_mode([0, 1, 0, 5]) == 0
    assert find_mode([11]) == 11
    assert find_mode([2, 2, 3, 3, 5]) in {2, 3}
    
    # Prueba para lista vacía
    with pytest.raises(ValueError):
        find_mode([])

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(10) == 3628800

    with pytest.raises(ValueError):
        factorial(-1)



def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-7) == False


def test_is_palindrome():
    assert is_palindrome("Ana") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("No lemon, no melon") == True
    assert is_palindrome("") == True
    assert is_palindrome(" ") == True
    with pytest.raises(ValueError):
        is_palindrome(None)

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Marc") == "craM"
    assert reverse_string("") == ""
    assert reverse_string("12345") == "54321"

def test_list_sum():
    assert list_sum([1, 2, 3, 4]) == 10
    assert list_sum([-1, -2, -3, -4]) == -10
    assert list_sum([0]) == 0
    with pytest.raises(ValueError):
        list_sum([])

def test_list_product():
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([-1, -2, -3, -4]) == 24
    assert list_product([0, -4, 2, 3]) == 0
    assert list_product([0]) == 0
    assert list_product([2, 2, 2]) == 8
    with pytest.raises(ValueError):
        list_product([])
