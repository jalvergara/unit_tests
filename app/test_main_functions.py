"""Unit testing for the project."""

import pandas as pd
import pytest
from unittest import mock
from .main import (
    add, divide, validate_no_null_values, db_query, subtract, square,
    is_even, find_max, find_min, find_mean, find_median, find_mode,
    factorial, is_prime, is_palindrome, reverse_string, list_sum, list_product
)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    with pytest.raises(ValueError):
        divide(1, 0)
    assert divide(6, 2) == 3.0

def test_validate_no_null_values():
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    assert validate_no_null_values(df1) is True
    df2 = pd.DataFrame({'A': [1, 2, None], 'B': ['a', None, 'c']})
    assert validate_no_null_values(df2) is False

def test_db_query():
    with mock.patch('app.main.db_query', return_value='DATA: [1, 2, 3]'):
        assert db_query() == 'DATA: [1, 2, 3]'

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(10, 5) == 5

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True

def test_find_max():
    assert find_max([1, 3, 2]) == 3
    assert find_max([-1, -3, -2]) == -1

def test_find_min():
    assert find_min([1, 3, 2]) == 1
    assert find_min([-1, -3, -2]) == -3

def test_find_mean():
    assert find_mean([1, 2, 3]) == 2.0
    assert find_mean([5, 10]) == 7.5

def test_find_median():
    assert find_median([1, 3, 2]) == 2
    assert find_median([1, 2, 3, 4]) == 2.5

def test_find_mode():
    assert find_mode([1, 1, 2, 3]) == 1
    assert find_mode([1, 2, 2, 3]) == 2

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_is_prime():
    assert is_prime(5) is True
    assert is_prime(4) is False
    assert is_prime(1) is False

def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""

def test_list_sum():
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([]) == 0

def test_list_product():
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([1, 0, 3, 4]) == 0
