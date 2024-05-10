# Repository to explain about unit testing


## Function:

## Deploying:

### For Windows:

1. Create virtual env

    ``` bash
    python -m venv venv
    ```

2. Activate with :

    ``` bash
    venv/Scripts/activate
    pip install pytest, pandas, pytest-cov
    ```

3. To run the tests:

    ``` bash
    pytest app/test_main_functions.py -s -v
    ```

4. To run the coverage:

    ``` bash
    pytest --cov
    ```

### For others:

1. Create virtual env

    ``` bash
    python -m venv venv
    ```

2. Activate with :

    ``` bash
    source data_validation_env/bin/activate
    pip install pytest, pandas, pytest-cov
    ```

3. To run the tests:

    ``` bash
    pytest tests/test_main_functions.py -s -v
    ```

4. To run the coverage:

    ``` bash
    pytest --cov
    ```

## Exercise:

### Create tests:

1. Create a branch with the name: feature/function_your_name , example: git checkout -b feature/function_alejandro ✅.

2. Create a docstring for all functions.

3. Create the function described in the TODO.

4. In the test_main_functions.py create the test, please try to cover as much scenaries as posible in your test function.

5. Test your functions using in the console:  pytest app/test_main_functions.py.

6. Be sure your tests passed and take a screenshot and send it to my email with the link of your branch.

7. Add your changes (git add, git commit).

8. Push your branch: git push origin feature/your_function_name_your_name.

9. Go to the github repository and create a pull request.
