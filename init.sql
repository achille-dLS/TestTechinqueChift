DROP SCHEMA IF EXISTS employees CASCADE;
CREATE SCHEMA employees;

CREATE TABLE employees.employe (
	id SERIAL PRIMARY KEY,
	nom VARCHAR(50),
	num_pro VARCHAR(13),
	email VARCHAR (255),
	departement varchar (255)
);