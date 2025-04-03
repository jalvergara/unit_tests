"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock

from .main import add, divide, validate_no_null_values, db_query, subtract, square, is_even, find_max, find_min, find_mean, find_median, find_mode, factorial, is_prime, is_palindrome, reverse_string, list_sum, list_product


def test_add():
    """Test cases for the add function."""
    assert add(-5, -5) == -10
    assert add(-100, 100) == 0
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2, 3) == 5
    assert add(0, 5) == 5
    assert add(199, 1) == 200
    assert add(500, -250) == 250
    assert add(1000, 2000) == 3000
    assert add(999999, 1) == 1000000


def test_divide():
    """Test case for zero division"""
    assert divide(10, -2) == -5.0
    assert divide(-8, 4) == -2.0
    assert divide(0, 5) == 0.0
    assert divide(6, 2) == 3.0
    assert divide(1, 3) == 1/3
    assert divide(7, 2) == 3.5
    assert divide(-10, -2) == 5.0
    assert divide(50, 5) == 10.0
    assert divide(100, 10) == 10.0
    with pytest.raises(ValueError):
        divide(1, 0)


def test_validate_no_null_values():
    """Test cases for the validate_no_null_values function."""
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    assert validate_no_null_values(df1) is True
    df2 = pd.DataFrame({'A': [], 'B': []})
    assert validate_no_null_values(df2) is True
    df3 = pd.DataFrame({'A': [1], 'B': [2]})
    assert validate_no_null_values(df3) is True
    df4 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert validate_no_null_values(df4) is True
    df5 = pd.DataFrame({'A': [10, 20, 30], 'B': ['x', 'y', 'z']})
    assert validate_no_null_values(df5) is True
    df6 = pd.DataFrame({'A': [1, 2, None], 'B': ['a', None, 'c']})
    assert validate_no_null_values(df6) is False
    df7 = pd.DataFrame({'A': [None, None], 'B': [None, None]})
    assert validate_no_null_values(df7) is False
    df8 = pd.DataFrame({'A': [1, None], 'B': ['test', 'data']})
    assert validate_no_null_values(df8) is False
    df9 = pd.DataFrame({'A': [0], 'B': [None]})
    assert validate_no_null_values(df9) is False
    df10 = pd.DataFrame({'A': [None], 'B': [None]})
    assert validate_no_null_values(df10) is False


def test_db_query():
    """Test case for the db_query function."""
    with mock.patch('app.main.db_query', return_value='DATA: [1, 2, 3]') as mock_db_query:
        assert db_query() == 'DATA: [1, 2, 3]'


# Alejandro Vergara
def test_subtract():
    """Test case for the subtract function."""
    assert subtract(-100, 50) == -150
    assert subtract(10, 20) == -10
    assert subtract(-6, 1) == -7
    assert subtract(-10, -5) == -5
    assert subtract(0, 0) == 0
    assert subtract(8, 7) == 1
    assert subtract(999999, 999998) == 1
    assert subtract(3, -3) == 6
    assert subtract(100, 50) == 50
    assert subtract(500, 250) == 250


def test_square():
    """Test case for the square function."""
    assert square(0) == 0
    assert square(-1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    assert square(-5) == 25
    assert square(10) == 100
    assert square(15) == 225
    assert square(20) == 400


def test_is_even():
    """Test case for the is_even function."""
    assert is_even(-2) is True
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(50) is True
    assert is_even(100) is True
    assert is_even(1000) is True
    assert is_even(-3) is False
    assert is_even(1) is False
    assert is_even(101) is False
    assert is_even(999) is False



def test_find_max():
    """Test case for the find_max function."""
    assert find_max([-100, -99, -98]) == -98
    assert find_max([-10, -20, -30, -5]) == -5
    assert find_max([-1, -2, -3, -4]) == -1
    assert find_max([1]) == 1
    assert find_max([0, 4, 2, 1, 3]) == 4
    assert find_max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert find_max([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 90
    assert find_max([100, 200, 300, 400]) == 400
    assert find_max([999, 1000, 1001]) == 1001
    with pytest.raises(ValueError, match="The list is empty."):
        find_max([])


def test_find_min():
    """Test case for the find_min function."""
    assert find_min([-1, -2, -3, -4]) == -4
    assert find_min([-10, -20, -30]) == -30
    assert find_min([1, 2, 3, 4, 5, -5]) == -5
    assert find_min([0, 4, 2, 1, 3]) == 0
    assert find_min([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert find_min([5, 5, 5, 5, 5]) == 5
    assert find_min([6, 7, 6, 5, 8, 9]) == 5
    assert find_min([40, 50, 60, 70, 80, 90]) == 40
    assert find_min([100]) == 100
    with pytest.raises(ValueError, match="The list is empty."):
        find_min([])


def test_find_mean():
    """Test case for the find_mean function."""
    assert find_mean([-5, -10, -15]) == -10
    assert find_mean([0, 0, 0]) == 0
    assert find_mean([-10, 0, 10]) == 0
    assert find_mean([1]) == 1
    assert find_mean([3, 3, 3, 3, 3]) == 3
    assert find_mean([1, 2, 3, 4, 5]) == 3
    assert find_mean([10, 20, 30]) == 20
    assert find_mean([100, 200, 300, 400]) == 250
    assert find_mean([7, 45, 3, 4, 2025]) == 416.8
    with pytest.raises(ValueError, match="The list is empty."):
        find_mean([])


def test_find_median():
    """Test case for the find_median function."""
    assert find_median([-3, -2, -1, 0, 1, 2, 3]) == 0
    assert find_median([1, 1, 1, 1, 1]) == 1
    assert find_median([3, 1, 2]) == 2
    assert find_median([1, 3, 2]) == 2
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    assert find_median([5, 10, 15]) == 10
    assert find_median([10, 20, 30, 40, 50]) == 30
    assert find_median([100]) == 100
    with pytest.raises(ValueError, match="The list is empty."):
        find_median([])


def test_find_mode():
    """Test cases for the find_mode function."""
    assert find_mode([-1, -2, -3, -3, -4, -5, -6]) == -3
    assert find_mode([-1, -1, 0, 1, 1, 1]) == 1
    assert find_mode([2, 3, 2, 3, 2]) == 2
    assert find_mode([3, 3, 3, 3]) == 3
    assert find_mode([1, 2, 3, 3, 4, 5, 6]) == 3
    assert find_mode([7, 7, 8, 8, 9, 9, 9]) == 9
    assert find_mode([1, 1, 2, 2, 3, 3, 4]) in [1,2,3]
    assert find_mode([5, 5, 5, 6, 6, 6, 7]) in [5,6]
    assert find_mode([10, 10, 20, 20, 30, 30, 30]) == 30
    with pytest.raises(ValueError, match="The list is empty."):
        find_mode([])



def test_factorial():
    """Test cases for the is_prime function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040
    assert factorial(8) == 40320
    assert factorial(9) == 362880
    assert factorial(10) == 3628800
    assert factorial(11) == 39916800


def test_is_prime():
    """Test cases for the is_palindrome function."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True
    assert is_prime(17) is True
    assert is_prime(19) is True
    assert is_prime(29) is True
    assert is_prime(101) is True
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(18) is False
    assert is_prime(20) is False
    assert is_prime(35) is False
    assert is_prime(100) is False


def test_is_palindrome():
    """Test cases for the reverse_string function."""
    assert is_palindrome("") is True
    assert is_palindrome("ana") is True
    assert is_palindrome("madam") is True
    assert is_palindrome("12321") is True
    assert is_palindrome("abcba") is True
    assert is_palindrome("hannah") is True
    assert is_palindrome("reconocer") is True
    assert is_palindrome("ETL") is False
    assert is_palindrome("yaxul") is False
    assert is_palindrome("abcdef") is False


def test_reverse_string():
    """Test cases for the list_sum function."""
    assert reverse_string("Yaxul") == "luxaY"
    assert reverse_string("ETL") == "LTE"
    assert reverse_string("April") == "lirpA"
    assert reverse_string("Class") == "ssalC"
    assert reverse_string("Data Engenieer & IA") == "AI & reeinegnE ataD"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("git") == "tig"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""


def test_list_sum():
    """Test cases for the list_product function."""
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([-5, 5, -5, 5]) == 0
    assert list_sum([0, 0, 0, 0]) == 0
    assert list_sum([0]) == 0
    assert list_sum([1, 1, 1, 1]) == 4
    assert list_sum([7]) == 7
    assert list_sum([10, -10, 10]) == 10
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([100, 200, 300]) == 600
    with pytest.raises(ValueError, match="The list is empty."):
        list_sum([])


def test_list_product():
    """Test cases for the list_product function."""
    assert list_product([-1, -2, -3, 4]) == -24
    assert list_product([10, 0, 5]) == 0
    assert list_product([1, -1, 1, -1]) == 1
    assert list_product([5]) == 5
    assert list_product([1, 2, 3, 4]) == 24
    assert list_product([-2, 3, -4]) == 24
    assert list_product([1, 2, 3, 4, 5]) == 120
    assert list_product([7, 7, 7]) == 343
    assert list_product([100, 200, 300]) == 6000000
    with pytest.raises(ValueError, match="The list is empty."):
        list_product([])