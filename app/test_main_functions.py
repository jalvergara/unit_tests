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
    """Test cases for the substract function."""
    assert subtract(2, 4) == -2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0



def test_square():
    """Test cases for the square function."""
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0



def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(-2) is True
    assert is_even(0) is True

def test_find_max():
    """Test cases for the find_max function."""
    numbers1 = [1, 2, 3, 4, 5]
    assert find_max(numbers1) == 5

    numbers2 = [-1, -2, -4, -6]
    assert find_max(numbers2) == -1

    with pytest.raises(
        ValueError
    ):
        find_max([])


def test_find_min():
    """Test cases for the find_min function."""

    with pytest.raises(
        ValueError
    ):
        find_min([])

    numbers1 = [1, 2, 4, 7, 3]
    assert find_min(numbers1) == 1

    numbers2 = [-3, -6, -2, -7]
    assert find_min(numbers2) == -7


def test_find_mean():
    """Test cases for the find_mean function."""

    with pytest.raises(
        ValueError
    ):
        find_min([])
    
    numbers1 = [2, 6, 7, 3, 10, 5]
    assert find_mean(numbers1) == 5.5

    numbers2 = [-3, 6, -2, 8]
    assert find_mean(numbers2) == 2.25


def test_find_median():
    """Test cases for the find_median function."""

    with pytest.raises(
        ValueError
    ):
        find_median([])
    
    numbers1 = [2, 6, 7, 3, 10, 5]
    assert find_median(numbers1) == 5.5

    numbers2 = [-3, 6, -2, 8]
    assert find_mean(numbers2) == 2.25


def test_find_mode():
    """Test cases for the find_median function."""

    with pytest.raises(
        ValueError
    ):
        find_mode([])
    
    numbers = [2, 6, 2, 3, 10, 5, 4, 2, 6, 3, 11, 9]
    assert find_mode(numbers) == 2


def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(0) == 1
    assert factorial(2) == 2


def test_is_prime():
    """Test cases for the is_prime function."""
    assert is_prime(2) is True
    assert is_prime(0) is False
    assert is_prime(6) is False
    assert is_prime(-1) is False


def test_is_palindrome():
    """Test cases for the is_palindrome function."""

    with pytest.raises(
        ValueError
    ):
        is_palindrome("")

    assert is_palindrome("civic") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("1235") is False


def test_reverse_string():
    """Test cases for the reverse_string function."""
    
    with pytest.raises(
        ValueError
    ):
        reverse_string("")

    assert reverse_string("hello") == "olleh"
    assert reverse_string("5287353") == "3537825"


def test_list_sum():
    """Test cases for the list_sum function."""

    with pytest.raises(
        ValueError
    ):
        list_sum([])
    
    numbers1 = [1, 6, 4, 8, 3, 6, 2]
    assert list_sum(numbers1) == 30

    numbers2 = [3, 7, -2, 7, -8, 9, 11, 4, -5]
    assert list_sum(numbers2) == 26


def test_list_product():
    """Tests cases for the list_product function."""

    with pytest.raises(
        ValueError
    ):
        list_product([])
    
    numbers1 = [5, 7, 2, 8, 4, 5, 3]
    assert list_product(numbers1) == 33600

    numbers2 = [3, 6, -4, 1, 6]
    assert list_product(numbers2) == -432

    numbers3 = [4, 8, -2, 5, 0]
    assert list_product(numbers3) == 0