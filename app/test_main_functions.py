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


# Samuel Escalante

def test_subtract():
    """Test case for subtract function"""
    assert subtract(3,3) == 0
    assert subtract(40,10) == 30
    assert subtract(10,40) == -30

@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        (6, 3, 3),
        (100, 10, 90),
        (-1, -1, 0),
    ],
)
def test_subtract_params(input1, input2, expected):
    assert subtract(input1, input2) == expected


def test_square():
    """Test case for square function"""
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0
    

def test_is_even():
    """Test case for is_even function"""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True


@pytest.mark.parametrize(
    "input, expected",
    [
        ([3,5,7,8], 8),
        ([1,2,3], 3),
        ([-1, -8,-10], -1),
    ],
)
def test_find_max(input, expected):
    """ Test case for find_max function"""
    assert find_max(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        ([3,5,7,8], 3),
        ([1,2,3], 1),
        ([-1, -8,-10], -10),
    ],
)
def test_find_min(input, expected):
    """ Test case for find_min function"""
    assert find_min(input) == expected
    

def test_find_mean():
    """Test case for find_mean function"""
    assert find_mean([1,2,3,4,5]) == 3
    assert find_mean([1,2,3,4,5,6,7,8,9,10]) == 5.5
    assert find_mean([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 8

@pytest.mark.parametrize(
    "input, expected",
    [
        ([1,2,3,4,5], 3),
        ([1,2,3,4,5,6,7,8,9,10], 5.5),
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 7.5),
    ],
)
def test_find_median(input, expected):
    """Test case for find_median function"""
    assert find_median(input) == expected

def test_find_mode():
    """Test case for find_mode function"""
    assert find_mode([1,2,3,4,5,6,7,8,9,10,10,10,10,10]) == 10
    assert find_mode([1,25,5,5,5,6,7,8,9,10,10,]) == 5
    

def test_factorial():
    """Test case for factorial function"""
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(0) == 1


def test_is_prime():
    """Test case for is_prime function"""
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False

def test_is_palindrome():
    """Test case for is_palindrome function"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("madam") == True


def test_reverse_string():
    """Test case for reverse_string function"""
    assert reverse_string("hello") == "olleh"


def test_list_sum():
    """Test case for list_sum function"""
    assert list_sum([1,2,3,4,5]) == 15
    assert list_sum([1,2,3,4,5,6,7,8,9,10]) == 55
    assert list_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 120


def test_list_product():
    """Test case for list_product function"""
    assert list_product([1,2,3,4,5]) == 120
    assert list_product([1,2,3,4,5,6,7,8,9,10]) == 3628800
    assert list_product([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 1307674368000
