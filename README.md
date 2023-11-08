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

### Create tests:

1. create a branch with the name: feature/your_function_name_your_name , example: git checkout -b feature/add_function_alejandro
2. create a docstring for your funciton
3. create the function described in the TODO
4. In the test_main_functions.py create the test, please try to cover as much scenaries as posible in your test function
5. test your function using in the console:  pytest app/test_main_functions.py
6. be sure your tests passed and take a screenshot and send it to my email with the link of your branch
7. add your changes (git add, git commit)
8. push your branch: git push origin feature/your_function_name_your_name
9. go to the github repository and create a pull request