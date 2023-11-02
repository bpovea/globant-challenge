--
-- creates departments, jobs and employees tables
--

set schema 'challenge_data';

CREATE TABLE challenge_data.departments (
    id serial PRIMARY KEY,
    departament VARCHAR(100)
);

CREATE TABLE challenge_data.jobs (
    id serial PRIMARY KEY,
    job VARCHAR(100)
);

CREATE TABLE challenge_data.employees (
    id serial PRIMARY KEY,
    name VARCHAR(100),
    department_id integer REFERENCES departments(id),
    job_id integer REFERENCES jobs(id)
);
