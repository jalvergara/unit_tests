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


def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(3, 2) == 1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0


def test_square():
    # TODO: write the tests cases for the square function
    assert square(1) == 1
    assert square(2) == 4
    assert square(-1) == 1
    assert square(0) == 0


def test_is_even():
    # TODO: write the tests cases for the is_even function
    assert is_even(1) == False
    assert is_even(2) == True
    assert is_even(0) == True
    assert is_even(-1) == False
    assert is_even(-2) == True


def test_find_max():
    # TODO: write the tests cases for the find_max function
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3]) == -1
    assert find_max([10]) == 10


def test_find_min():
    # TODO: write the tests cases for the find_min function
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([-1, -2, -3]) == -3
    assert find_min([10]) == 10


def test_find_mean():
    # TODO: write the tests cases for the find_mean function
    assert find_mean([1, 2, 3, 4, 5]) == 3.0
    assert find_mean([-1, 0, 1]) == 0.0
    assert find_mean([]) == 0.0


def test_find_median():
    # TODO: write the tests cases for the find_median function
    assert find_median([1, 2, 3, 4, 5]) == 3.0
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([5]) == 5.0


def test_find_mode():
    # TODO: write the tests cases for the find_mode function
    assert find_mode([1, 2, 2, 3]) == 2
    assert find_mode([1, 1, 2, 2, 3]) == 1 
    assert find_mode([]) == None


def test_factorial():
    # TODO: write the tests cases for the factorial function
    with pytest.raises(ValueError):
        factorial(-1)
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(3) == 6


def test_is_prime():
    # TODO: write the tests cases for the is_prime function
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(1) == False
    assert is_prime(-3) == False


def test_is_palindrome():
    # TODO: write the tests cases for the is_palindrome function
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True

def test_reverse_string():
    # TODO: write the tests cases for the reverse_string function
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("12345") == "54321"


def test_list_sum():
    # TODO: write the tests cases for the list_sum function
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([]) == 0
    assert list_sum([-1, -2, -3]) == -6


def test_list_product():
    # TODO: write the tests cases for the list_product function
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([1, 0, 3]) == 0
    assert list_product([]) == 1  
