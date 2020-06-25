# Contributing

Pull requests are welcome!

This package uses the following for development:

| Package         | Purpose              |
| -------         | -------              |
| pytest          | Testing              |
| vulture         | Dead code detection  |
| mypy            | Static type checking |
| pylint & flake8 | Linting              |
| coverage        | Test coverage        |
| tox             | Test automation      |

Use the following command to install them.

    pip install -r requirements-dev.txt

## Tests (pytest)

Make sure to add tests for any new piece of code using pytest.

## Static type checking (mypy)

Use type annotations for every function definition and apply mypy for static type checking.

## Linting (pylint and flake8)

Use both pylint and flake8 for linting.

## Dead code detection (vulture)

Vulture to check for dead code.

