"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract, reverse_string, list_sum


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
    # TODO: write the tests cases for the find_mean function
    pass


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
    """
    Test cases for the reverse_string function.
    1) A regular string
    2) An empty string
    3) A string of numbers
    4) A string with Spaces, numbers, and different characteres
    """
    assert reverse_string('Hi there!') == '!ereht iH'
    assert reverse_string('') == ''
    assert reverse_string('1234') == '4321'
    assert reverse_string('SoY  Un $Tr1ng') == 'gn1rT$ nU  YoS'

# Maria Angelica Portocarrero
def test_list_sum():
    # Test case 1: List is empty
    assert list_sum([]) == 0

    # Test case 2: List with one single number
    assert list_sum([10]) == 10

    # Test case 3: List with positive numbers
    assert list_sum([1, 2, 3, 4, 5]) == 15

    # Test case 4: List with negative numbers
    assert list_sum([-1, -2, -3, -4, -5]) == -15

    # Test case 5: List with mixed positive and negative numbers
    assert list_sum([-1, 2, -3, 4, -5]) == -3    

    # Test case 6: List with decimals
    assert list_sum([0.5, 1.5, 2.5]) == 4.5

    # Test case 7: List with both integers and decimals
    assert list_sum([1, 2.5, 3, 4.5]) == 11.0

    # Test case 8: List with large numbers
    assert list_sum([10**6, 2 * 10**6, 3 * 10**6]) == 6 * 10**6

# Angie Manzano
def test_list_product():
    # TODO: write the tests cases for the list_product function
    pass
