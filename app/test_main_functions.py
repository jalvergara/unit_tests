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
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0


def test_square():
    """Test cases for the square function."""
    assert square(2) == 4
    assert square(-2) == 4
    assert square(0) == 0



def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True

def test_find_max():
    """Test cases for the find_max function."""
    with pytest.raises(
        ValueError
    ):
        numbers = []
        find_max(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = ["a","b","c"]
        find_max(numbers)
    
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([2]) == 2
    assert find_max([-2,-4,-72]) == -2


def test_find_min():
    """Test cases for the find_min function."""
    with pytest.raises(
        ValueError
    ):
        numbers = []
        find_min(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = ["a","b","c"]
        find_min(numbers)
    
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([4, 2, 9, -1, 6]) == -1
    assert find_min([4]) == 4


def test_find_mean():
    """Test cases for the find_mean function."""
    with pytest.raises(
        ValueError
    ):
        numbers = []
        find_mean(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = ["a","b","c"]
        find_mean(numbers)
     
    assert find_mean([1, 2, 3, 4, 5]) == 3
    assert find_mean([5]) == 5


def test_find_median():
    """Test cases for the find_median function."""
    with pytest.raises(
        ValueError
    ):
        numbers = []
        find_median(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = ["a","b","c"]
        find_median(numbers)
    
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([1, 2, 3, 4, 5, 6]) == 3.5


def test_find_mode():
    """Test cases for the find_mode function."""
    with pytest.raises(
        ValueError
    ):
        numbers = []
        find_mode(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = ["a","b","c"]
        find_mode(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = [1,2,3,4]
        find_mode(numbers)
    
    assert find_mode([1, 2, 2, 3, 4, 5]) == 2


def test_factorial():
    """Test cases for the factorial function."""
    with pytest.raises(
        ValueError
    ):
        factorial(-1)

    assert factorial(3) == 6
    assert factorial(0) == 1


def test_is_prime():
    """Test cases for the is_prime function."""
    with pytest.raises(
        ValueError
    ):
        is_prime(-1)
    
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(101) == True


def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    assert is_palindrome("Hola") == False
    assert is_palindrome("Radar") == True
    assert is_palindrome("madam") == True


def test_reverse_string():
    """Test cases for the reverse_string function."""
    assert reverse_string("Hola") == "aloH"
    assert reverse_string("etl!") == "!lte"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("6174") == "4716"


def test_list_sum():
    """Test cases for the list_sum function."""
    with pytest.raises(
        ValueError
    ):
        numbers = []
        list_sum(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = ["a","b","c"]
        list_sum(numbers)

    assert list_sum([1,2,3,4]) == 10
    assert list_sum([-1,-2,-3,-4])  == -10
    assert list_sum([1,2,3,-4]) == 2
    assert list_sum([1,2,-3,-4]) == -4
    assert list_sum([1,6,-3,-4]) == 0

def test_list_product():
    """Test cases for the list_product function."""
    with pytest.raises(
        ValueError
    ):
        numbers = []
        list_product(numbers)

    with pytest.raises(
        ValueError
    ):
        numbers = ["a","b","c"]
        list_product(numbers)
    
    assert list_product([1,2,3,4]) == 24
    assert list_product([1,2,3,-4]) == -24
    assert list_product([1,2,-3,-4]) == 24
    assert list_product([1,2,0,-4]) == 0
