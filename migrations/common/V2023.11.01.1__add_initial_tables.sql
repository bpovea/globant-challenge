--
-- creates departments, jobs and employees tables
--

set schema 'challenge_data';

CREATE TABLE challenge_data.departments (
    id INTEGER PRIMARY KEY,
    department VARCHAR(100)
);

CREATE TABLE challenge_data.jobs (
    id INTEGER PRIMARY KEY,
    job VARCHAR(100)
);

CREATE TABLE challenge_data.employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    hire_datetime TIMESTAMPTZ,
    department_id integer REFERENCES departments(id),
    job_id integer REFERENCES jobs(id)
);
