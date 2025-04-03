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


# Gabriel Martinez
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2     
    assert subtract(0, 0) == 0      

def test_square():
    assert square(3) == 9           
    assert square(-2) == 4          
    assert square(0) == 0            

def test_is_even():
    assert is_even(4) == True        
    assert is_even(7) == False       
    assert is_even(0) == True       

def test_find_max():
    assert find_max([1, 2, 3, 4]) == 4 
    assert find_max([-1, -2, -3]) == -1   
    assert find_max([0]) == 0              

def test_find_min():
    assert find_min([1, 2, 3, 4]) == 1    
    assert find_min([-1, -2, -3]) == -3   
    assert find_min([0]) == 0              

def test_find_mean():
    assert find_mean([1, 2, 3, 4]) == 2.5 
    assert find_mean([0]) == 0.0            
    assert find_mean([]) == 0.0             

def test_find_median():
    assert find_median([1, 2, 3, 4, 5]) == 3  
    assert find_median([1, 2, 3, 4]) == 2.5   
    assert find_median([]) == 0.0              # Empty list (assuming 0.0)

def test_find_mode():
    assert find_mode([1, 2, 2, 3, 3, 3]) == 3
    assert find_mode([1, 1, 2, 2]) == 1        
    assert find_mode([]) == None                

def test_factorial():
    assert factorial(5) == 120          
    assert factorial(0) == 1            
    assert factorial(1) == 1           

def test_is_prime():
    assert is_prime(7) == True         
    assert is_prime(4) == False         
    assert is_prime(1) == False         # 1 is not prime

def test_is_palindrome():
    assert is_palindrome("radar") == True   # Palindrome
    assert is_palindrome("Long life Love") == False  # Not a palindrome
    assert is_palindrome("") == True        

def test_reverse_string():
    assert reverse_string("hello") == "olleh" 
    assert reverse_string("") == ""            
    assert reverse_string("a") == "a"          

def test_list_sum():
    assert list_sum([1, 2, 3]) == 6     
    assert list_sum([]) == 0            
    assert list_sum([-1, 1]) == 0       

def test_list_product():
    assert list_product([1, 2, 3]) == 6 
    assert list_product([]) == 1          
    assert list_product([0, 1, 2]) == 0  