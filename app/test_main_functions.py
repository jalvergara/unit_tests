"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from app.main import (
    add,
    subtract,
    divide,
    square,
    is_even,
    find_max,
    find_min,
    find_mean,
    find_median,
    find_mode,
    factorial,
    is_prime,
    is_palindrome,
    reverse_string,
    list_sum,
    list_product,
    validate_no_null_values,
    db_query
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

    df3 = pd.DataFrame()
    assert validate_no_null_values(df3) is True
    
    df4 = pd.DataFrame(columns=['A', 'B'])
    assert validate_no_null_values(df4) is True


def test_db_query():
    """Test case for the db_query function."""
    with mock.patch('app.main.db_query', return_value='DATA: [1, 2, 3]') as mock_db_query:
        assert db_query() == 'DATA: [1, 2, 3]'


# Alejandro Vergara
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0


def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0



def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(-4) is True
    assert is_even(0) is True


def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3, -4]) == -1
    with pytest.raises(ValueError):
        find_max([])


def test_find_min():
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([-1, -2, -3, -4]) == -4
    with pytest.raises(ValueError):
        find_min([])


def test_find_mean():
    assert find_mean([1, 2, 3, 4, 5]) == 3.0
    assert find_mean([-1, -2, -3, -4]) == -2.5
    with pytest.raises(ValueError):
        find_mean([])

def test_find_median():
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([-1, -2, -3, -4]) == -2.5
    with pytest.raises(ValueError):
        find_median([])


def test_find_mode():
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([1, 1, 2, 2]) in [1, 2]
    assert find_mode([-1, -1, -2, -3]) == -1
    with pytest.raises(ValueError):
        find_mode([])


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False

    assert is_prime(2) is True
    assert is_prime(3) is True

    assert is_prime(4) is False
    assert is_prime(9) is False

    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True
    assert is_prime(13) is True
    assert is_prime(17) is True
    assert is_prime(19) is True
    assert is_prime(23) is True

    assert is_prime(25) is False
    assert is_prime(27) is False
    assert is_prime(49) is False
    assert is_prime(77) is False
    assert is_prime(121) is False

def test_is_palindrome():
    assert is_palindrome("radar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True



def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_list_sum():
    assert list_sum([1, 2, 3, 4]) == 10
    assert list_sum([]) == 0
    assert list_sum([-1, -2, -3]) == -6


def test_list_product():
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([]) == 1
    assert list_product([-1, -2, -3]) == -6
