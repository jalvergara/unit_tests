"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import (
    add, 
    divide, 
    validate_no_null_values, 
    db_query, 
    subtract,
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
    list_product
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


# Alejandro Vergara
def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(2, 1) == 1
    assert subtract(-1, -1) == 0


def test_square():
    assert square(2) == 4
    assert square(-2) == 4
    assert square(5) == 25


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(40) == True


def test_find_max():
    assert find_max([7,6,4,3,8,1,2]) == 8
    assert find_max([7,6,4,-1,2,10.5]) == 10.5


def test_find_min():
    assert find_min([7,6,4,3,8,1,2]) == 1
    assert find_min([7,6,4,-1,2,10.5]) == -1


def test_find_mean():
    assert find_mean([1,2,3,4,5,6,7,8]) == 4.5 
    with pytest.raises(
        ZeroDivisionError
    ):
        find_mean([])

def test_find_median():
    assert find_median([1,2,3,4,5,6,7,8,9]) == 5
    with pytest.raises(
        ZeroDivisionError
        ):
        find_median([])
    assert find_median([1,2,3,4,5,6,7,8]) == 4.5



def test_find_mode():
    assert find_mode([1,2,3,4,5,5,6,7,8,9,10]) == 5
    assert find_mode([1,2,3,4,5,6,7,8,8,9.0]) == 8
    with pytest.raises(
        RuntimeError
    ):
        find_mode([])


def test_factorial():
    assert factorial(0) == 1
    assert factorial(19) == 121645100408832000
    with pytest.raises(
        ValueError
    ):
        factorial(-1)


def test_is_prime():
    assert is_prime(4) == False
    assert is_prime(2) == True
    assert is_prime(1) == False

def test_is_palindrome():
    assert is_palindrome("ama") == True
    assert is_palindrome("amor") == False


def test_reverse_string():
    assert reverse_string("hola mudo") == "odum aloh"
    assert reverse_string("ama") == "ama"


def test_list_sum():
    assert list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 45
    assert list_sum([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 0
    assert list_sum([]) == 0
    


def test_list_product():
    assert list_product([1, 2, 3]) == 6
    assert list_product([1, 2, -3]) == -6
    assert list_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 0
    assert list_product([]) == 0
