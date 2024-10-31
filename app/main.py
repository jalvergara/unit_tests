""" main functions to explain unit testing"""

import pandas as pd

def add(a: int, b: int) -> int:
    """Function to add two numbers

    Parameters
    ----------
    a : int
        first digit to add
    b : int
        second digit to add

    Returns
    -------
    int
        a '+' b
    """
    return a + b


def divide(a: int, b: int) -> float:
    """_summary_

    Parameters
    ----------
    a : int
        first digit
    b : int
        second digit

    Returns
    -------
    float
        a divided by b

    Raises
    ------
    ValueError
        Zero division
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")

    return a / b


# Function to validate that a Pandas DataFrame has no null values
def validate_no_null_values(df: pd.DataFrame) -> bool:
    """_summary_

    Parameters
    ----------
    df : pd.DataFrame
        dataframe to validate

    Returns
    -------
    bool
        True if no null values, False otherwise
    """
    return not df.isnull().values.any()


def db_query() -> str:
    """function to mock a database query

    Returns
    -------
    str
        mocked database query
    """
    return "DATA: [1, 2, 3]"


# Alejandro Vergara
def subtract(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Invalid type: both a and b must be integers")
    return a - b

def square(a: int) -> int:
    if not isinstance(a, int):
        raise TypeError("Invalid type: a must be an integer")
    return a ** 2


def is_even(x: int) -> bool:
    if not isinstance(x, int):
        raise TypeError("Invalid type: x must be an integer")    
    return x % 2 == 0


def find_max(numbers: list) -> int:
    #verificar que todos los elementos de la lista sean números
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    if not numbers:  # Verifica si la lista está vacía
        raise ValueError("The list is empty")
    elif len(numbers) == 1:  # Verifica si la lista tiene un solo elemento
        raise ValueError("The list has only one element")
    else:
        max_number = numbers[0]  # Asigna el primer número como el máximo inicial
        for number in numbers:
            if number > max_number:
                max_number = number  # Actualiza max_number si se encuentra un número mayor
        return max_number


def find_min(numbers: list) -> int:
    #verificar que todos los elementos de la lista sean números
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    if not numbers:  # Verifica si la lista está vacía
        raise ValueError("The list is empty")
    elif len(numbers) == 1:  # Verifica si la lista tiene un solo elemento
        raise ValueError("The list has only one element")
    else:
        min_number = numbers[0]  # Asigna el primer número como el mínimo inicial
        for number in numbers:
            if number < min_number:
                min_number = number  # Actualiza min_number si se encuentra un número menor
        return min_number


def find_mean(numbers: list) -> float:
    #verificar que todos los elementos de la lista sean números
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
        
    if not numbers:  # Verifica si la lista está vacía
        raise ValueError("The list is empty")
    
    elif len(numbers) == 1:
        return numbers[0]  # Retorna el único número en la lista
    
    else:
        total_sum = 0
        count = 0
        for number in numbers:
            total_sum += number
            count += 1
        # Calcula y retorna la media
        return total_sum / count


def find_median(numbers: list) -> float:
    #verificar que todos los elementos de la lista sean números
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
        
    if not numbers:  # Verifica si la lista está vacía
        raise ValueError("The list is empty")
    
    elif len(numbers) == 1:
        return numbers[0]
    
    else:
        # Ordenar la lista manualmente
        sorted_numbers = sorted(numbers)  # Esto usa sort pero no depende de bibliotecas externas
        n = len(sorted_numbers)

        # Calcular y retornar la mediana
        mid = n // 2
        if n % 2 == 1:  # Si el número de elementos es impar
            return sorted_numbers[mid]
        else:  # Si el número de elementos es par
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

def find_mode(numbers: list) -> int:
    #verificar que todos los elementos de la lista sean números
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    
    if not numbers:  # Verifica si la lista está vacía
        raise ValueError("The list is empty")
    
    elif len(numbers) == 1:
        return numbers[0]
    else:
        # Crear un diccionario para contar la frecuencia de cada número
        frequency = {}
        for number in numbers:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1

        # Encontrar el número con la frecuencia más alta
        max_count = max(frequency.values())
        mode_values = [key for key, count in frequency.items() if count == max_count]

        # Si hay múltiples modas, retornar el primero; de lo contrario, retornar el valor único
        return mode_values[0] if len(mode_values) == 1 else mode_values
    

def factorial(n: int) -> int:
    # verificar que sea entero
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    elif n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 1
    else:
        # Calcular factorial manualmente
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    elif n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n < 2:
        False
    else:
        # Verificar si n tiene divisores diferentes de 1 y n
        for i in range(2, int(n**0.5) + 1):  # Solo hasta la raíz cuadrada de n
            if n % i == 0:
                return False
        return True


def is_palindrome(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    elif not word:
        raise ValueError("word must not be empty")
    else:
        # Compara la palabra o frase tal como está con su reverso
        return word == word[::-1]


def reverse_string(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("string must be a string")
    elif not string:
        raise ValueError("string must not be empty")
    else:
        return string[::-1]


def list_sum(numbers: list) -> int:
    # Verificar que todos los elementos de la lista sean números
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    elif len(numbers) == 1:
        return numbers[0]
    else:
        # Sumar los elementos manualmente
        total = 0
        for number in numbers:
            total += number
        return total


def list_product(numbers: list) -> int:
    # Verificar que todos los elementos de la lista sean números
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    elif len(numbers) == 1:
        return numbers[0]
    else:
        # Sumar los elementos manualmente
        total = 0
        for number in numbers:
            total *= number
        return total

