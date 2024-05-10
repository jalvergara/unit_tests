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


# Mariana Mera 
def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0


def test_square():
    assert square(5) == 25
    assert square(2) == 4
    assert square(0) == 0



def test_is_even():
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(6) == True
    assert is_even(1) == False



def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-5, -3, 0, 5, 10]) == 10
    assert find_max([10]) == 10
    assert find_max([-10, -5, -3, -1]) == -1

    try:
        find_max([])
    except ValueError as e:
        assert str(e) == "The list is empty"


def test_find_min():
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([-5, -3, 0, 5, 10]) == -5
    assert find_min([10]) == 10
    assert find_min([-10, -5, -3, -1]) == -10

    try:
        find_min([])
    except ValueError as e:
        assert str(e) == "The list is empty"


def test_find_mean():
    assert find_mean([]) == 0
    assert find_mean([5]) == 5
    assert find_mean([1, 2, 3, 4, 5]) == 3
    assert find_mean([-1, -2, -3, -4, -5]) == -3
    assert find_mean([1.5, 2.5, 3.5, 4.5, 5.5]) == 3.5


def test_find_median():
    assert find_median([]) == 0
    assert find_median([5]) == 5
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([-5, -4, -3, -2, -1]) == -3


def test_find_mode():
    assert find_mode([]) == []
    assert find_mode([1, 2, 2, 3, 4, 5, 5, 5]) == [5]
    assert find_mode([1, 2, 2, 3, 3, 4, 4, 5, 5]) == [2, 3, 4, 5]
    assert find_mode([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120  
    assert factorial(10) == 3628800


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(1) == False
    assert is_prime(4) == False



def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("rotor") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False



def test_reverse_string():
    assert reverse_string("a") == "a"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"


def test_list_sum():
    assert list_sum([]) == 0
    assert list_sum([5]) == 5
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([-1, -2, -3, -4, -5]) == -15


def test_list_product():
    assert list_product([]) == 1
    assert list_product([5]) == 5
    assert list_product([1, 2, 3, 4, 5]) == 120
    assert list_product([-1, -2, -3, -4, -5]) == -120
