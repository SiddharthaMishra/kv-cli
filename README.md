# Command line interface for accessing the key-value server

## Dependancies

### 1. from pipenv
* install pipenv (https://github.com/pypa/pipenv)
* run ```pipenv install```

### 2. from requirements.txt
* create venv with Python >= 3.6
* run ```pip install -r requirements.txt```

## Run

* Run the main script `python main.py`

* Usage
    1. put <key> <value>
        * eg. put test "test value"
    2. get <key>
        * eg. get test
    3. watch
    4. help

    Quoted strings count as one argument