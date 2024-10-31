"""Unit testing for the project."""

import os 
import sys 

# Añadir el directorio raíz al sys.path para permitir importaciones
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from app.main import (  
    add, divide, validate_no_null_values, db_query, subtract, square, is_even, find_max,
    find_min, find_mean, find_median, find_mode, factorial, is_prime, is_palindrome,
    reverse_string, list_sum, list_product
)

def test_add():
    assert add(3, 4) == 7

def test_divide():
    assert divide(10, 2) == 5.0
    with pytest.raises(ValueError):
        divide(10, 0)

def test_validate_no_null_values():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert validate_no_null_values(df) is True
    df_with_null = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
    assert validate_no_null_values(df_with_null) is False

def test_db_query():
    assert db_query() == "DATA: [1, 2, 3]"

def test_subtract():
    assert subtract(10, 5) == 5

def test_square():
    assert square(5) == 25

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

def test_find_max():
    assert find_max([1, 2, 3, 4]) == 4

def test_find_min():
    assert find_min([1, 2, 3, 4]) == 1

def test_find_mean():
    assert find_mean([1, 2, 3, 4]) == 2.5

def test_find_median():
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([1, 2, 3]) == 2

def test_find_mode():
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_is_prime():
    assert is_prime(5) is True
    assert is_prime(4) is False

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_list_sum():
    assert list_sum([1, 2, 3, 4]) == 10

def test_list_product():
    assert list_product([1, 2, 3, 4]) == 24

