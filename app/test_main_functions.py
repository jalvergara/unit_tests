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



def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(2, 3) == -1
    assert subtract(-4, 4) == -8
    assert subtract(0, 0) == 0


def test_square():
    """Test cases for the square function."""
    assert square(2) == 4
    assert square(5) == 25
    assert square(10) == 100
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-7) == 49
    assert square(0) == 0



def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(7) == False
    assert is_even(11) == False
    assert is_even(0) == True
    assert is_even(-2) == True



def test_find_max():
    """Test cases for the find_max function."""

    assert find_max([9, 3, 2, 1, 4]) == 9
    assert find_max([1, 3, 2, 4, 6]) == 6
    assert find_max([1, 3, 5, 2, 4]) == 5
    assert find_max([7, 7, 7, 7, 7]) == 7
    assert find_max([]) == None
    assert find_max([4]) == 4




def test_find_min():
    """Test cases for the find_min function."""
    assert find_min([1, 3, 4, 5, 6]) == 1
    assert find_min([6, 5, 4, 3, 1]) == 1
    assert find_min([5, 4, 2, 3, 6]) == 2
    assert find_min([7, 7, 7, 7, 7]) == 7
    assert find_min([]) == None
    assert find_min([4]) == 4




def test_find_mean():
    """Test cases for the find_mean function."""
    assert find_mean([1, 2, 3, 4, 5]) == 3.0
    assert find_mean([-1, -2, -3, -4, -5]) == -3.0
    assert find_mean([-1, 2, -3, 4, -5]) == -0.6
    assert find_mean([6]) == 6.0
    assert find_mean([]) == None



def test_find_median():
    """Test cases for the find_median function."""
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([-5, -3, -1, 1, 3, 5]) == 0
    assert find_median([6]) == 6
    assert find_median([]) == None



def test_find_mode():
    """Test cases for the find_mode function."""
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([1, 2, 2, 3, 3, 4]) in [2, 3]  
    assert find_mode([2, 4, 6, 8, 10]) in [2, 4, 6, 8, 10]
    assert find_mode([5]) == 5
    assert find_mode([]) == None


def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    with pytest.raises(ValueError):
        factorial(-1)


def test_is_prime():
    """Test cases for the is_prime function."""
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(-2) == False
    assert is_prime(-3) == False
    assert is_prime(0) == False




def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    assert is_palindrome("civic") == True
    assert is_palindrome("level") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("world") == False
    assert is_palindrome("") == True   
    assert is_palindrome("a") == True 




def test_reverse_string():
    """Test cases for the reverse_string function."""
    assert reverse_string("angeles") == "selegna"
    assert reverse_string("angelito") == "otilegna"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""
    


def test_list_sum():
    """Test cases for the list_sum function."""
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([-1, -2, -3, -4, -5]) == -15
    assert list_sum([-1, 2, -3, 4, -5]) == -3
    assert list_sum([7]) == 7
    assert list_sum([]) == 0



def test_list_product():
    """Test cases for the list_product function."""
    assert list_product([1, 2, 3, 4, 5]) == 120
    assert list_product([-1, -2, -3, -4, -5]) == -120
    assert list_product([-1, 2, -3, 4, 5]) == 120
    assert list_product([7]) == 7
    assert list_product([]) == 1


