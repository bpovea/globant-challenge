# Globant's Data Engineer Challenge

This is a public repository that contains Globant's Data Engineering Challenge. It consists of the initial setup for a RESTful API service for loading and reporting structured employee data.

This project uses a variety of technologies and utilities that can be used for learning purposes, such as:

- Docker
- LocalStack (Mock AWS)
- Postgres
- Flyway migrations
- Python - Flask API
- Makefile
- Pytests [TODO]
- Code Linters (Black - sqlfluff)
- Terraform

## Requirements

- Docker
- Pipenv
- Python 3.9
- Terraform

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

## Run the project
### Make commands

Here is a brief explanation of the available make commands (be sure you are in the pipenv environment before running make commands):
- `make start`:
    - copy the .env.example file to .env file in case it doesn't exist.
    - start the local-stack container that will mock the AWS S3 service.
    - start the challenge-db which is a Postgres DB for storing the employee data.
    - Run the flyway migrations to create the initial schemas and tables.
    - Run Terraform code for creating an s3 bucket for development proposes.
    - Copy the ./data files to the s3 bucket using an AWS cli command.
    - Start the flask API service and keep it in the active console.
- `make run-section-1`: This command uses curl to create a request for populating the data in the database.
- `make run-section-2-1`:
    - This command uses curl to create a request that generates a report with the 2021 summary data for the hired employees by quarter, department and job.
    - Download the data from the output path in the local directory.
- `make run-section-2-2`:
    - This command uses curl to create a request that generates a report with the 2021 summary data for the hired employees by department.
    - Download the data from the output path in the local directory.
- `make clean`:
    - Delete local-stack challenge-db challenge-migration containers.
    - Run the `make start` command.
