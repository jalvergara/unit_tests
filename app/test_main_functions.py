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
    assert subtract(5, 2) == 3
    assert subtract(-5, -2) == -3
    assert subtract(5, -2) == 7
    assert subtract(0, 0) == 0
    print("All tests passed!")


def test_square():
    """Test cases for the square function."""
    assert square(5) == 25
    assert square(-3) == 9
    assert square(0) == 0
    assert square(100) == 10000
    print("All tests passed!")


def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(-6) == True
    assert is_even(-7) == False
    assert is_even(0) == True
    print("All tests passed!")


def test_find_max():
    """Test cases for the find_max function."""
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([-4, -8, -2, -6]) == -2
    assert find_max([7]) == 7
    assert find_max([10, 4, 6, 2]) == 10
    assert find_max([3, 1, 5, 7, 9]) == 9

    try:
        find_max([])
    except ValueError as e:
        assert str(e) == "The list is empty"
    else:
        raise AssertionError("Expected the function to raise a ValueError for an empty list, but it didn't.")
    
    print("All tests passed successfully.")



def test_find_min():
    """Test cases for the find_min function."""
    assert find_min([1, 5, 3, 9, 2]) == 1
    assert find_min([-4, -8, -2, -6]) == -8
    assert find_min([7]) == 7
    assert find_min([2, 4, 6, 10]) == 2
    assert find_min([9, 7, 5, 3, 1]) == 1
    
    try:
        find_min([])
    except ValueError as e:
        assert str(e) == "The list is empty"
    else:
        raise AssertionError("Expected the function to raise a ValueError for an empty list, but it didn't.")
    
    print("All tests passed successfully.")


def test_find_mean():
    """Test cases for the find_mean function."""
    assert find_mean([]) == 0
    assert find_mean([5]) == 5
    assert find_mean([1, 2, 3, 4, 5]) == 3
    assert find_mean([-1, -2, -3, -4, -5]) == -3
    assert round(find_mean([1, -2, 3, -4, 5]), 1) == 0.6
    print("All tests passed successfully.")


def test_find_median():
    """Test cases for the find_median function."""
    assert find_median([]) == 0
    assert find_median([5]) == 5
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([-1, -2, -3, -4, -5]) == -3
    assert find_median([1, -2, 3, -4, 5]) == 1
    print("All tests passed successfully.")


def test_find_mode():
    """Test cases for the find_mode function."""
    assert find_mode([]) == 0
    assert find_mode([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]) == [3, 5]
    assert find_mode([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert find_mode([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    print("All tests passed successfully.")


def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    print("All tests passed successfully.")


def test_is_prime():
    """Test cases for the is_prime function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    print("All tests passed successfully.")


def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("madam") == True
    assert is_palindrome("") == True
    print("All tests passed successfully.")


def test_reverse_string():
    """Test cases for the reverse_string function."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("") == ""
    print("All tests passed successfully.")


def test_list_sum():
    """Test cases for the list_sum function."""
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([-1, -2, -3, -4, -5]) == -15
    assert list_sum([0, 0, 0, 0, 0]) == 0
    assert list_sum([]) == 0
    assert list_sum([10, -5, 3, -8, 20]) == 20
    print("All tests passed successfully.")


def test_list_product():
    """Test cases for the list_product function."""
    assert list_product([1, 2, 3, 4, 5]) == 120
    assert list_product([-1, -2, -3, -4, -5]) == -120
    assert list_product([1, 2, 3, 4, 5, 0]) == 0
    assert list_product([]) == 1
    assert list_product([10, -5, 3, -8, 2]) == 2400
    print("All tests passed successfully.")
