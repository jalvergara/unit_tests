"""Unit testing for the project."""

import pandas as pd
import pytest
import logging as loggin

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract,square, is_even, find_max, find_min, find_mean, find_median, find_mode, factorial, is_prime, is_palindrome, reverse_string, list_sum, list_product


# def test_add():
#     """Test cases for the add function."""
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0


# def test_divide():
#     """Test case for zero division"""

#     with pytest.raises(
#         ValueError
#     ):
#         divide(1, 0)

#     assert divide(6, 2) == 3.0


# def test_validate_no_null_values():
#     """Test cases for the validate_no_null_values function."""
#     # Create a DataFrame with no null values
#     df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
#     assert validate_no_null_values(df1) is True

#     # Create a DataFrame with null values
#     df2 = pd.DataFrame({'A': [1, 2, None], 'B': ['a', None, 'c']})
#     assert validate_no_null_values(df2) is False


# def test_db_query():
#     """Test case for the db_query function."""
#     with mock.patch('app.main.db_query', return_value='DATA: [1, 2, 3]') as mock_db_query:
#         assert db_query() == 'DATA: [1, 2, 3]'


# Emmanuel's functions
def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(3, 2) == 1


def test_square():
    assert square(2) == 4
    assert square(-2) == 4
    assert square(0) == 0
    assert square(3) == 9



def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(5) == False
    assert is_even(0) == True
    assert is_even(-2) == True


def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([2, 4, 6, 8, 10, 12]) == 12
    assert find_max([3, 5, 7, 9, 11, 13, 15]) == 15
    assert find_max([10, 20, 30, 40, 50, 60, 70, 80]) == 80




def test_find_min():
    assert find_min([4, 6, 10, 0, 34, 56]) == 0
    assert find_min([2, 4, 6, 8, 10, 12]) == 2
    assert find_min([56, 100, 34, 57, 90]) == 34
    assert find_min([10, 20, 30, 40, 50, 60, 70, 80]) == 10


def test_find_mean():
    assert find_mean([1, 2, 3, 4, 5]) == 3.0
    assert find_mean([2, 4, 6, 8, 10, 12]) == 7.0
    assert find_mean([3, 5, 7, 9, 11, 13, 15]) == 9.0
    assert find_mean([10, 20, 30, 40, 50, 60, 70, 80]) == 45.0


def test_find_median():
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([2, 4, 6, 8, 10, 12]) == 7
    assert find_median([3, 5, 7, 9, 11, 13, 15]) == 9
    assert find_median([10, 20, 30, 40, 50, 60, 70, 80]) == 45


def test_find_mode():
    assert find_mode([1, 2, 3, 4, 5, 1]) == 1
    assert find_mode([2, 2, 4, 2, 6, 8, 10, 12]) == 2
    assert find_mode([3, 5, 7, 9, 11, 13, 15, 9, 9, 11, 13]) == 9


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False


def test_is_palindrome(): 
    assert is_palindrome('hello') == False
    assert is_palindrome('madam') == True
    assert is_palindrome('civic') == True
    assert is_palindrome('level') == True


def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('aloha') == 'ahola'
    assert reverse_string('water') == 'retaw'
    assert reverse_string('first') == 'tsrif'



def test_list_sum():
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([2, 4, 6, 8, 10, 12]) == 42
    assert list_sum([3, 5, 7, 9, 11, 13, 15]) == 63
    assert list_sum([10, 20, 30, 40, 50, 60, 70, 80]) == 360



def test_list_product():
    assert list_product([1, 2, 3, 4, 5]) == 120
    assert list_product([2, 4, 6, 8, 10, 12]) == 46080
    assert list_product([3, 5, 7, 9, 11, 13, 15]) == 2027025
    assert list_product([10, 20, 30, 40, 50, 60, 70, 80]) == 4032000000000
