"""Unit testing for the project."""

import pandas as pd
import pytest

from unittest import mock
from .main import add, divide, validate_no_null_values, db_query, subtract, reverse_string, list_sum, find_median, is_palindrome, factorial, find_mode, find_max


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


# Alejandro Vergara
def test_subtract():
    """Test cases for the subtract function."""
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0


# Samuel Patino
def test_square():
    # TODO: write the tests cases for the square function
    pass


# Sebastian Diaz
def test_is_even():
    # TODO: write the tests cases for the is_even function
    pass


# Andres enriquez
'''Pruebas para la función find_max'''
def test_find_max():
    '''Prueba 1: Verificar si encuentra el número máximo en una lista no vacía'''
    numbers1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result1 = find_max(numbers1)
    assert result1 == 9  

    '''Prueba 2: Verificar si maneja correctamente una lista vacía'''
    numbers2 = []
    try:
        result2 = find_max(numbers2)
        assert False  
    except ValueError:
        assert True  

    '''Prueba 3: Verificar si maneja correctamente una lista con un solo elemento'''
    numbers3 = [42]
    result3 = find_max(numbers3)
    assert result3 == 42  

    '''Prueba 4: Verificar si encuentra el número máximo en una lista con números negativos'''
    numbers4 = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
    result4 = find_max(numbers4)
    assert result4 == -1  


# Juan Felipe Zambrano
def test_find_min():
    # TODO: write the tests cases for the find_min function
    pass


# Kevin Artunduaga
def test_find_mean():
    # TODO: write the tests cases for the find_mean function
    pass


# Camila Cardona
def test_find_median():
    """Test case for the find_median function."""

    # Create a list with an odd number of elements
    numbers = [1, 3, 2, 4, 5]
    expected_result = 3.0
    result = find_median(numbers)
    assert result == expected_result

    # Create a list with an even number of elements
    numbers = [1, 2, 3, 4]
    expected_result = 2.5
    result = find_median(numbers)
    assert result == expected_result

    # Create a list with no elements
    numbers = []
    try:
        find_median(numbers)
    except ValueError as e:
        assert str(e) == "No median for empty list"



# Juan Camilo Vargas
def test_find_mode():
    """Test case to find the mode of a list of numbers"""
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([1, 1, 2, 2, 3, 3, 4, 4]) in [1, 2, 3, 4]
    assert find_mode([1, 2, 3, 4, 5]) == 1
    assert find_mode([]) is None


# Samuel Pinzon
def test_factorial():
    """Test cases for the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

    with pytest.raises(
        ValueError
    ):
        factorial(-1)


# Atenea Rojas
def test_is_prime():
    # TODO: write the tests cases for the is_prime function
    pass


# Gustavo Chipatinza
def test_is_palindrome():
    """Test cases for the is_palindrome function."""
    assert is_palindrome("racecar") is True  # esta frase corta es un palindrome
    assert is_palindrome("hello") is False   # no es un palindrome
    assert is_palindrome("A man a plan a canal Panama") is True  # esta frase larga es un palindrome
    # Casos de cadenas vacías
    assert is_palindrome("") is True  # Una cadena vacía es un palíndromo
    assert is_palindrome(" ") is True  # Espacio en blanco es un palíndromo
    assert is_palindrome("  ") is True  # Espacios en blanco múltiples son un palíndromo
    # Casos de mayúsculas y minúsculas
    assert is_palindrome("racecar") is True  # Minúsculas, un palíndromo
    assert is_palindrome("Racecar") is True  # Primera letra mayúscula, un palíndromo
    assert is_palindrome("rAcEcar") is True  # Varias mayúsculas, un palíndromo
    # Casos con caracteres especiales
    assert is_palindrome("!A man a plan a canal Panama!") is True  # Puntuación y mayúsculas
    assert is_palindrome("Was it a car or a cat I saw?") is False  # Otra frase con puntuación
    assert is_palindrome("No 'x' in Nixon") is False  # Comillas simples
    #casos numeros
    assert is_palindrome("12321") is True  # Números, un palíndromo
    assert is_palindrome("123221821") is False  # Números, un palíndromo




# Santiago Murgueitio
def test_reverse_string():
    """
    Test cases for the reverse_string function.
    1) A regular string
    2) An empty string
    3) A string of numbers
    4) A string with Spaces, numbers, and different characteres
    """
    assert reverse_string('Hi there!') == '!ereht iH'
    assert reverse_string('') == ''
    assert reverse_string('1234') == '4321'
    assert reverse_string('SoY  Un $Tr1ng') == 'gn1rT$ nU  YoS'

# Maria Angelica Portocarrero
def test_list_sum():
    # Test case 1: List is empty
    assert list_sum([]) == 0

    # Test case 2: List with one single number
    assert list_sum([10]) == 10

    # Test case 3: List with positive numbers
    assert list_sum([1, 2, 3, 4, 5]) == 15

    # Test case 4: List with negative numbers
    assert list_sum([-1, -2, -3, -4, -5]) == -15

    # Test case 5: List with mixed positive and negative numbers
    assert list_sum([-1, 2, -3, 4, -5]) == -3    

    # Test case 6: List with decimals
    assert list_sum([0.5, 1.5, 2.5]) == 4.5

    # Test case 7: List with both integers and decimals
    assert list_sum([1, 2.5, 3, 4.5]) == 11.0

    # Test case 8: List with large numbers
    assert list_sum([10**6, 2 * 10**6, 3 * 10**6]) == 6 * 10**6

# Angie Manzano
def test_list_product():
    # TODO: write the tests cases for the list_product function
    pass
