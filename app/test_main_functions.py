"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract, \
    square, is_even, find_max, find_min, find_mean, find_median, find_mode, \
    factorial, is_prime, is_palindrome, reverse_string, list_sum, list_product


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
    """ Test cases for the subtract function."""

    assert subtract(8, 2) == 6
    assert subtract(-2, -3) == 1
    assert subtract(0, 0) == 0
    assert subtract(-7, 3) == -10


def test_square():
    """Test cases for the square function."""
    
    with pytest.raises(TypeError):  
        square("a")

    assert square(4) == 16
    assert square(-3) == 9
    assert square(0) == 0


def test_is_even():
    """Test cases for the is_even function."""

    with pytest.raises(TypeError):
        is_even("a")

    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(-2) is True


def test_find_max():
    """Test cases for the find_max function."""
    with pytest.raises(
        ValueError
    ):
        find_max([])
    with pytest.raises(
        TypeError
    ):
        find_max("a")
    with pytest.raises(
        TypeError
    ):
        find_max([1, "b", "a"])
    
    assert find_max([1, 2, 3]) == 3
    assert find_max([-1, -2, -3]) == -1
    assert find_max([0, 0, 0]) == 0


def test_find_min():
    """Test cases for the find_min function."""
    with pytest.raises(
        ValueError
    ):
        find_min([])
    with pytest.raises(
        TypeError
    ):
        find_min("a")
    with pytest.raises(
        TypeError
    ):
        find_min([1, "b", "a"])

    assert find_min([1, 2, 3]) == 1
    assert find_min([-1, -2, -3]) == -3
    assert find_min([0, 0, 0]) == 0


def test_find_mean():
    """Test cases for the find_mean function."""
    with pytest.raises(
        ValueError
    ):
        find_mean([])
    with pytest.raises(
        TypeError
    ):
        find_mean("a")  
    with pytest.raises(
        TypeError
    ):
        find_mean([1, "b", "a"])

    assert find_mean([1, 2, 3]) == 2.0
    assert find_mean([-1, -2, -3]) == -2.0
    assert find_mean([0, 0, 0]) == 0.0


def test_find_median():
    """Test cases for the find_median function."""
    with pytest.raises(
        ValueError
    ):
        find_median([])
    with pytest.raises(
        TypeError
    ):
        find_median("a")
    with pytest.raises(
        TypeError
    ):
        find_median([1, "b", "a"])

    assert find_median([1, 2, 3]) == 2.0
    assert find_median([2,3,6,5]) == 4.0
    assert find_median([-1, 2, 3, -4]) == 0.5


def test_find_mode():
    """Test cases for the find_mode function."""
    with pytest.raises(
        ValueError
    ):
        find_mode([])

    with pytest.raises(
        ValueError
    ):
        find_mode([1, 2, 3])
    
    with pytest.raises(
        ValueError
    ):
        find_mode([1, 1, 2, 2])
    
    with pytest.raises(
        TypeError
    ):
        find_mode("a")
    
    with pytest.raises(
        TypeError
    ):
        find_mode([1, "b", "a"])

    assert find_mode([1, 2, 3, 2]) == 2
    assert find_mode([1, 2, 3, 4, 1]) == 1 
    assert find_mode([1, 2, 3, 3, 3]) == 3


def test_factorial():
    """Test cases for the factorial function."""
    with pytest.raises(
        ValueError
    ):
        factorial(-1)
    with pytest.raises(
        TypeError
    ):
        factorial("a")
    
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_is_prime():
    """Test cases for the is_prime function."""
    with pytest.raises(
        TypeError
    ):
        is_prime("a")
    

    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False


def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    with pytest.raises(
        ValueError
    ):
        is_palindrome("")
    with pytest.raises(
        TypeError
    ):
        is_palindrome(123)

    assert is_palindrome("ana") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("oso") is True


def test_reverse_string():
    """Test cases for the reverse_string function."""
    with pytest.raises(
        ValueError
    ):
        reverse_string("")
    with pytest.raises(
        TypeError
    ):
        reverse_string(123)

    assert reverse_string("escuela") == "aleucse"
    assert reverse_string("a") == "a"
    assert reverse_string("123") == "321"


def test_list_sum():
    """Test cases for the list_sum function."""
    with pytest.raises(
        ValueError
    ):
        list_sum([])
    with pytest.raises(
        TypeError
    ):
        list_sum("a")
    with pytest.raises(
        TypeError
    ):
        list_sum([1, "b", "a"])

    assert list_sum([1, 2, 3]) == 6
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([0, 0, 0]) == 0


def test_list_product():
    """Test cases for the list_product function."""
    with pytest.raises(
        ValueError
    ):
        list_product([])
    with pytest.raises(
        TypeError
    ):
        list_product("a")   
    with pytest.raises(
        TypeError
    ):
        list_product([1, "b", "a"])

    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([-1, -2, -3]) == -6
    assert list_product([0, 0, 0]) == 0
