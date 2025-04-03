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



def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0



def test_square():
    """Test cases for the square function."""
    assert square(2) == 4
    assert square(-5) == 25 
    assert square(0) == 0


def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(0) == True
    assert is_even(2) == True
    assert is_even(-6) == True
    assert is_even(7) == False
    assert is_even(3) == False


def test_find_max():
    """Test cases for the find_max function."""
    assert find_max([1, 3, 8, 12]) == 12
    assert find_max([50, 25, 0]) == 50
    assert find_max([-802, 20, -6]) == 20

    with pytest.raises(ValueError):
        find_max([])


def test_find_min():
    """Test cases for the find_min function."""
    assert find_min([1, 3, 8, 12]) == 1
    assert find_min([50, 25, 0]) == 0
    assert find_min([-802, 20, -6]) == -802

    with pytest.raises(ValueError):
        find_min([])

def test_find_mean():
    """Test cases for the find_mean function"""
    assert find_mean([1, 3, 8, 12]) == 6
    assert find_mean([50, 25, 0]) == 25
    assert find_mean([-802, 20, -6]) == -262.6666666666667

    with pytest.raises(ValueError):
        find_mean([])

def test_find_median():
    """Tests cases for the find_median function"""
    assert find_median([1,2,3,4,5]) == 3
    assert find_median([2.0,12.11,22.3,24.12,55.22]) == 22.3
    assert find_median([6,1,2,4,5,3]) == 3.5

    with pytest.raises(ValueError):
        find_median([])

def test_find_mode():
    """Tests cases for the find_mode function"""
    assert find_mode([1,2,3,3]) == 3
    assert find_mode([2,2,2,3,4]) == 2
    assert find_mode([5,7,8,9,10,8,9,5,6,9]) == 9

    with pytest.raises(ValueError):
        find_mode([])

def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)


def test_is_prime():
    """Test cases for the is_prime function."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(13) is True
    assert is_prime(1) is False
    assert is_prime(-3) is False
    assert is_prime(29) is True


def test_is_palindrome():
    """Test cases for the is_palindrome function"""
    assert is_palindrome('kayak') is True
    assert is_palindrome('word') is False
    assert is_palindrome('repaper') is True

    with pytest.raises(TypeError):
        reverse_string(123)



def test_reverse_string():
    """Test cases for the reverse_string function."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("a") == "a"

    with pytest.raises(TypeError):
        reverse_string(123)


def test_list_sum():
    """Test cases for the list_sum function."""
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([-1, 1, 0]) == 0
    assert list_sum([10, 20, 30]) == 60

    with pytest.raises(ValueError):
        list_sum([])  

    with pytest.raises(TypeError):
        list_sum([1, "a", 3]) 


def test_list_product():
    """Test cases for the list_product function."""
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([5, -2, 3]) == -30
    assert list_product([10, 0, 3]) == 0
    assert list_product([7]) == 7

    with pytest.raises(ValueError):
        list_product([])  

    with pytest.raises(TypeError):
        list_product([1, "b", 3])
