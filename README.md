# Python Package Template

This repository contains a template for Python package development. Out of the
box, the template provides testing, linting, and formatting features with
reasonable default configurations, so users can focus right away on writing
code rather than setup.

The template was inspired in large part by this
[blog post](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/)
by Alex Mitelman.

## Requirements

Make sure you have Python 3.10 and [Poetry](https://python-poetry.org/)
installed. Instructions for installing Poetry are available
[here](https://python-poetry.org/docs/master/#installation).

## Setup

1. From this GitHub repository, click the "Use this template" button and follow
   the instructions to create your own repository based on the template.
   Alternatively, clone or download this repository and skip to Step 3 (note
   that doing so will cause the commit history of the template to be included in
   your project).
2. Clone your new repository:

   ```sh
   git clone {repo_url}
   ```

3. From the project's root directory, create a virtual environment with your
   Python executable of choice. Assuming `python`:

   ```sh
   poetry env use python
   ```

4. Install dependencies:

   ```sh
   poetry install
   ```

5. Activate the virtual environment you created in Step 3:

   ```sh
   poetry shell
   ```

6. Install pre-commit hooks:

   ```sh
   pre-commit install
   ```

7. Set pre-commit to automatically update hooks (optional):

   ```sh
   pre-commit autoupdate
   ```

Now that you're set up, you can run the package with `python -m sample_package`.

## Development Tools

The following tools are provided by default. Note that the commands listed
assume you have activated the virtual environment you created above, but you can
also run commands without activating the virtual environment by prefacing them
with `poetry run`. For example, `poetry run pytest` will run pytest within the
virtual environment without needing to explicitly activate it.

### [pytest](https://docs.pytest.org/)

Run all tests:

```sh
pytest
```

Run tests in a single file or directory:

```sh
pytest {target file or directory}
```

### [pytest-cov](https://github.com/pytest-dev/pytest-cov)

Run tests and produce coverage report:

```sh
pytest --cov
```

### [Flake8](https://flake8.pycqa.org/en/latest/)

Lint code:

```sh
flake8 {target file or directory}
```

Once pre-commit hooks are installed, Flake8 will be automatically run prior to
all commits (see pre-commit below).

### [Black](https://black.readthedocs.io/en/stable/)

Automatically format code:

```sh
black {target file or directory}
```

You can also check which files would be updated without actually making any
changes:

```sh
black {target file or directory} --check
```

Or you can check exactly what changes would be made, again without actually
making any changes:

```sh
black {target file or directory} --diff
```

Once pre-commit hooks are installed, Black will be automatically run prior to
all commits (see pre-commit below).

### [Mypy](https://mypy.readthedocs.io/en/stable/index.html)

Type check your code with:

```sh
mypy {target file or directory}
```

Once pre-commit hooks are installed, Mypy will be automatically run prior to
all commits (see pre-commit below).

Note that this template requires your code to be statically typed by default.
If you want to allow dynamic typing, set `disallow_untyped_defs = false` under
`[tool.mypy]` in pyproject.toml.

### [isort](https://pycqa.github.io/isort/)

Automatically sort imports:

```sh
isort {target file or directory}
```

Once pre-commit hooks are installed, isort will be automatically run prior to
all commits (see pre-commit below).

### [pre-commit](https://pre-commit.com/)

pre-commit allows easy configuration of pre-commit hooks. Once pre-commit hooks
are installed for this project, the following hooks will automatically be
run on staged files in the repository prior to each commit:

- trailing whitespace
- end-of-file-fixer
- check-json
- check-yaml
- check-added-large-files
- pretty-format-json
- mixed-line-ending
- flake8
- black
- mypy
- isort

If all checks pass, the commit will proceed as usual, but if any checks fail,
the commit will be rejected. If this happens, you'll need to fix all issues
before committing. This is intentional, and helps to enforce good coding
practices.

Note that some of the hooks will try to fix issues for you. If this happens, the
commit will be rejected, but the files will be modified. You can review the
changes and update manually if necessary. Or if you're happy with the automatic
changes, use `git add` to stage modified files and retry your commit.

You can also run the configured pre-commit hooks without committing using
`pre-commit run --all-files`.

[A wide variety of other hooks](https://pre-commit.com/hooks.html) can be added
by following instructions in the
[pre-commit documentation](https://pre-commit.com/index.html).

## Contact

If you have questions about this template or suggestions for improvement, please
contact [Andrew Desautels](mailto:andrew.desautels@steergroup.com).
