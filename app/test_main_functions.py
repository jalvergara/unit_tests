"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query
from .main import find_mean

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
    # TODO: write the tests cases for the subtract function
    pass


# Samuel Patino
def test_square():
    # TODO: write the tests cases for the square function
    pass


# Sebastian Diaz
def test_is_even():
    # TODO: write the tests cases for the is_even function
    pass


# Andres enriquez
def test_find_max():
    # TODO: write the tests cases for the find_max function
    pass


# Juan Felipe Zambrano
def test_find_min():
    # TODO: write the tests cases for the find_min function
    pass


# Kevin Artunduaga
def test_find_mean():
    """Test case for the find_mean function."""

    # Case 1 
    numbers = [1, 2, 3, 4, 5]
    result = find_mean(numbers)

    assert result == 3.0

    # Case 2
    numbers = [-1, 0, 1]
    result = find_mean(numbers)
    assert result == 0.0

    # Case 3
    numbers = [-5, -3, -2, -1, 0]
    result = find_mean(numbers)
    assert result == -2.2

# Camila Cardona
def test_find_median():
    # TODO: write the tests cases for the find_median function
    pass


# Juan Camilo Vargas
def test_find_mode():
    # TODO: write the tests cases for the find_mode function
    pass


# Samuel Pinzon
def test_factorial():
    # TODO: write the tests cases for the factorial function
    pass


# Atenea Rojas
def test_is_prime():
    # TODO: write the tests cases for the is_prime function
    pass


# Gustavo Chipatinza
def test_is_palindrome():
    # TODO: write the tests cases for the is_palindrome function
    pass


# Santiago Murgueitio
def test_reverse_string():
    # TODO: write the tests cases for the reverse_string function
    pass


# Maria Angelica Portocarrero
def test_list_sum():
    # TODO: write the tests cases for the list_sum function
    pass


# Angie Manzano
def test_list_product():
    # TODO: write the tests cases for the list_product function
    pass
