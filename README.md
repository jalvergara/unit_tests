# Repository to explain about unit testing

create virtual env

python -m venv venv

activate with :

source data_validation_env/bin/activate

pip install pytest, pandas, pytest-cov

to run the tests:
pytest tests/test_main_functions.py -s -v

to run the coverage:

pytest --cov

## Exercise:

### Testing a String Manipulation Function
Description: Create a function that manipulates strings (reversing a string). Write test cases to ensure the function behaves correctly.
