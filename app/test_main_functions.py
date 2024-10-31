"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract,square,is_even,find_max,find_min,find_mean,find_median,find_mode,factorial,is_prime,is_palindrome,reverse_string,list_sum,list_product   


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
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
    with pytest.raises(TypeError):
        subtract(1.5, 1)


def test_square():
    assert square(3) == 9
    assert square(-4) == 16

    with pytest.raises(TypeError):
        square('a')



def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    with pytest.raises(TypeError):
        is_even('a')


def test_find_max():
    assert find_max([1, 2, 3]) == 3
    assert find_max([-1, -2, -3]) == -1

    with pytest.raises(ValueError):
        find_max([])
    with pytest.raises(TypeError):
        find_max([1, 2, 'a'])


def test_find_min():
    assert find_min([1, 2, 3]) == 1
    assert find_min([-1, -2, -3]) == -3

    with pytest.raises(ValueError):
        find_min([])
    with pytest.raises(TypeError):
        find_min([1, 2, 'a'])


def test_find_mean():
    assert find_mean([1, 2, 3]) == 2.0
    assert find_mean([-1, 0, 1]) == 0.0

    with pytest.raises(ValueError):
        find_mean([])
    with pytest.raises(TypeError):
        find_mean([1, 2, 'a'])


def test_find_median():
    assert find_median([1, 2, 3]) == 2.0
    assert find_median([1, 3, 2]) == 2.0
    assert find_median([1, 2, 3, 4]) == 2.5

    with pytest.raises(ValueError):
        find_median([])
    with pytest.raises(TypeError):
        find_median([1, 2, 'a'])


def test_find_mode():
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([1, 1, 2, 2]) == 1 # Test for multiple modes

    with pytest.raises(ValueError):
        find_mode([])
    with pytest.raises(TypeError):
        find_mode([1, 2, 'a'])


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(2.5)


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False

    with pytest.raises(ValueError):
        is_prime(-1)
    with pytest.raises(TypeError):
        is_prime('a')


def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False

    with pytest.raises(ValueError):
        is_palindrome("")
    with pytest.raises(TypeError):
        is_palindrome(123)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    # Verificar que se lanza la excepción para cadena vacía
    with pytest.raises(ValueError) as exc_info:
        reverse_string("")
    assert str(exc_info.value) == "string must not be empty"

    with pytest.raises(ValueError):
        reverse_string("")
    with pytest.raises(TypeError):
        reverse_string(123)


def test_list_sum():
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([-1, -2, -3]) == -6

    with pytest.raises(ValueError):
        list_sum([])
    with pytest.raises(TypeError):
        list_sum([1, 2, 'a'])


def test_list_product():
    assert list_product([1, 2, 3]) == 6
    assert list_product([1, -1, 1]) == -1

    with pytest.raises(ValueError):
        list_product([])
    with pytest.raises(TypeError):
        list_product([1, 2, 'a'])
