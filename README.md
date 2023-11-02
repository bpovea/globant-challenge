# Globant's Data Engineer challenge


This is a public repo that contains Globant's Data Engineering Challenge. It consists of the initial setup for a RESTful API service for loading and reporting structured employee data.

This project uses a bunch of technologies and utilities that could be used for  learning proposes, such as:
 - Docker
 - LocalStack (Mock AWS)
 - Postgres
 - Flyway migrations
 - Python - Flask API
 - Makefile
 - Pytests
 - Code Linters (Black - sqlfluff)
 - Terraform

## Requirements
- Docker
- Pipenv
- Python3.9

## Build Configuration
### Install the project dependencies:

```bash
pipenv install --dev
```

If the installation fails, make sure that `python --version` returns version **3.9.x**. Other versions will likely work, but knowing that **3.9.x** does work can save time running into cryptic errors that often occur if it does not work.

If it fails and you need to retry, it often helps to delete the `Pipfile.lock`, clear the virtual environment (`pipenv --rm`), and reinstall, specifying the version explicity: `pipenv install --dev --python 3.9`.

### Configure the Linter

The project uses the formatter and linter black. In order to run this before committing, check that you have pipenv environment for development (`pipenv shell`), and run:

```bash
make git-hooks
```
