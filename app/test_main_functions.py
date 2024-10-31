"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract,square,is_even,find_max,find_min,find_mean,find_median,find_mode,factorial,is_prime,is_palindrome,reverse_string,list_sum,list_product   


def test_add():
    """Test cases for the add function."""
    assert add(2, 3) == 5  # Test adding positive numbers
    assert add(-1, 1) == 0  # Test adding a negative and positive number
    assert add(0, 0) == 0  # Test adding zeros


def test_divide():
    """Test case for zero division."""
    with pytest.raises(ValueError):  # Expecting ValueError on division by zero
        divide(1, 0)
    assert divide(6, 2) == 3.0  # Test normal division


def test_validate_no_null_values():
    """Test cases for DataFrame validation."""
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})  # DataFrame with no nulls
    assert validate_no_null_values(df1) is True  # Should return True

    df2 = pd.DataFrame({'A': [1, 2, None], 'B': ['a', None, 'c']})  # DataFrame with nulls
    assert validate_no_null_values(df2) is False  # Should return False


def test_db_query():
    """Test case for the db_query function."""
    with mock.patch('app.main.db_query', return_value='DATA: [1, 2, 3]') as mock_db_query:
        assert db_query() == 'DATA: [1, 2, 3]'  # Check the mocked return value


def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(5, 3) == 2  # Test normal subtraction
    assert subtract(-1, -1) == 0  # Test subtracting equal negatives
    assert subtract(0, 0) == 0  # Test subtracting zeros
    with pytest.raises(TypeError):  # Expecting TypeError for non-integer input
        subtract(1.5, 1)


def test_square():
    """Test cases for the square function."""
    assert square(3) == 9  # Test squaring a positive number
    assert square(-4) == 16  # Test squaring a negative number
    with pytest.raises(TypeError):  # Expecting TypeError for non-integer input
        square('a')


def test_is_even():
    """Test cases for the is_even function."""
    assert is_even(2) is True  # Test an even number
    assert is_even(3) is False  # Test an odd number
    assert is_even(0) is True  # Test zero
    with pytest.raises(TypeError):  # Expecting TypeError for non-integer input
        is_even('a')


def test_find_max():
    """Test cases for finding the maximum value."""
    assert find_max([1, 2, 3]) == 3  # Test max in positive numbers
    assert find_max([-1, -2, -3]) == -1  # Test max in negative numbers
    with pytest.raises(ValueError):  # Expecting ValueError for empty list
        find_max([])
    with pytest.raises(TypeError):  # Expecting TypeError for mixed types
        find_max([1, 2, 'a'])


def test_find_min():
    """Test cases for finding the minimum value."""
    assert find_min([1, 2, 3]) == 1  # Test min in positive numbers
    assert find_min([-1, -2, -3]) == -3  # Test min in negative numbers
    with pytest.raises(ValueError):  # Expecting ValueError for empty list
        find_min([])
    with pytest.raises(TypeError):  # Expecting TypeError for mixed types
        find_min([1, 2, 'a'])


def test_find_mean():
    """Test cases for calculating the mean."""
    assert find_mean([1, 2, 3]) == 2.0  # Test mean in positive numbers
    assert find_mean([-1, 0, 1]) == 0.0  # Test mean with negative and positive
    with pytest.raises(ValueError):  # Expecting ValueError for empty list
        find_mean([])
    with pytest.raises(TypeError):  # Expecting TypeError for mixed types
        find_mean([1, 2, 'a'])


def test_find_median():
    """Test cases for calculating the median."""
    assert find_median([1, 2, 3]) == 2.0  # Test median in odd count
    assert find_median([1, 3, 2]) == 2.0  # Test median with unordered input
    assert find_median([1, 2, 3, 4]) == 2.5  # Test median in even count
    with pytest.raises(ValueError):  # Expecting ValueError for empty list
        find_median([])
    with pytest.raises(TypeError):  # Expecting TypeError for mixed types
        find_median([1, 2, 'a'])


def test_find_mode():
    """Test cases for calculating the mode."""
    assert find_mode([1, 2, 2, 3, 4]) == 2  # Test mode for single mode
    assert find_mode([1, 1, 2, 2]) == 1  # Test for multiple modes
    with pytest.raises(ValueError):  # Expecting ValueError for empty list
        find_mode([])
    with pytest.raises(TypeError):  # Expecting TypeError for mixed types
        find_mode([1, 2, 'a'])


def test_factorial():
    """Test cases for calculating the factorial."""
    assert factorial(5) == 120  # Test factorial of a positive number
    assert factorial(0) == 1  # Test factorial of zero
    with pytest.raises(ValueError):  # Expecting ValueError for negative input
        factorial(-1)
    with pytest.raises(TypeError):  # Expecting TypeError for non-integer input
        factorial(2.5)


def test_is_prime():
    """Test cases for checking prime numbers."""
    assert is_prime(2) is True  # Test first prime number
    assert is_prime(3) is True  # Test another prime number
    assert is_prime(4) is False  # Test a non-prime number
    with pytest.raises(ValueError):  # Expecting ValueError for negative input
        is_prime(-1)
    with pytest.raises(TypeError):  # Expecting TypeError for non-integer input
        is_prime('a')


def test_is_palindrome():
    """Test cases for checking palindromes."""
    assert is_palindrome("madam") is True  # Test a palindrome
    assert is_palindrome("hello") is False  # Test a non-palindrome
    with pytest.raises(ValueError):  # Expecting ValueError for empty string
        is_palindrome("")
    with pytest.raises(TypeError):  # Expecting TypeError for non-string input
        is_palindrome(123)


def test_reverse_string():
    """Test cases for reversing a string."""
    assert reverse_string("hello") == "olleh"  # Test reversing a normal string
    with pytest.raises(ValueError) as exc_info:  # Expecting ValueError for empty string
        reverse_string("")
    assert str(exc_info.value) == "string must not be empty"
    with pytest.raises(TypeError):  # Expecting TypeError for non-string input
        reverse_string(123)


def test_list_sum():
    """Test cases for summing a list."""
    assert list_sum([1, 2, 3]) == 6  # Test sum of positive numbers
    assert list_sum([-1, -2, -3]) == -6  # Test sum of negative numbers
    with pytest.raises(ValueError):  # Expecting ValueError for empty list
        list_sum([])
    with pytest.raises(TypeError):  # Expecting TypeError for mixed types
        list_sum([1, 2, 'a'])


def test_list_product():
    """Test cases for multiplying a list."""
    assert list_product([1, 2, 3]) == 6  # Test product of positive numbers
    assert list_product([1, -1, 1]) == -1  # Test product with a negative number
    with pytest.raises(ValueError):  # Expecting ValueError for empty list
        list_product([])
    with pytest.raises(TypeError):  # Expecting TypeError for mixed types
        list_product([1, 2, 'a'])