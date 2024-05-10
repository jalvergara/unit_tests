"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract, square, is_even, find_max, find_min, find_mean, find_median, find_mode


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
    # Test positive numbers
    assert square(2) == 4
    assert square(5) == 25
    assert square(10) == 100
    
    # Test negative numbers
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-7) == 49
    
    # Test zero
    assert square(0) == 0



def test_is_even():
    """Test cases for the is_even function."""
    # Test even numbers
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(10) == True
    
    # Test odd numbers
    assert is_even(3) == False
    assert is_even(7) == False
    assert is_even(11) == False
    
    # Test zero
    assert is_even(0) == True
    
    # Test negative even numbers
    assert is_even(-2) == True
    assert is_even(-4) == True
    assert is_even(-10) == True
    
    # Test negative odd numbers
    assert is_even(-3) == False
    assert is_even(-7) == False
    assert is_even(-11) == False



def test_find_max():
    """Test cases for the find_max function."""
    # Test when the maximum is the first element
    assert find_max([5, 3, 2, 1, 4]) == 5
    
    # Test when the maximum is the last element
    assert find_max([1, 3, 2, 4, 7]) == 7
    
    # Test when the list is empty
    assert find_max([]) == None
    
    # Test when the list has one element
    assert find_max([7]) == 7



def test_find_min():
    """Test cases for the find_min function."""
    # Test when the minimum is the first element
    assert find_min([2, 3, 4, 5, 6]) == 2
    
    # Test when the minimum is the last element
    assert find_min([6, 5, 4, 3, 1]) == 1

     # Test when the list is empty
    assert find_min([]) == None
    
    # Test when the list has one element
    assert find_min([7]) == 7



def test_find_mean():
    """Test cases for the find_mean function."""
    assert find_mean([1, 2, 3, 4, 5]) == 3.0 # Test when all elements are positive
    
    assert find_mean([-1, -2, -3, -4, -5]) == -3.0 # Test when all elements are negative
    
    # Test when the list has both positive and negative numbers
    assert find_mean([-1, 2, -3, 4, -5]) == -0.6
    
    # Test when the list has only one element
    assert find_mean([7]) == 7.0
    
    # Test when the list is empty
    assert find_mean([]) == None


def test_find_median():
    """Test cases for the find_median function."""
    # Test when the list has odd number of elements
    assert find_median([1, 2, 3, 4, 5]) == 3
    
    # Test when the list has even number of elements
    assert find_median([1, 2, 3, 4]) == 2.5


def test_find_mode():
    pass


def test_factorial():
    # TODO: write the tests cases for the factorial function
    pass


def test_is_prime():
    # TODO: write the tests cases for the is_prime function
    pass


def test_is_palindrome():
    # TODO: write the tests cases for the is_palindrome function
    pass


def test_reverse_string():
    # TODO: write the tests cases for the reverse_string function
    pass


def test_list_sum():
    # TODO: write the tests cases for the list_sum function
    pass


def test_list_product():
    # TODO: write the tests cases for the list_product function
    pass
