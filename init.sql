DROP SCHEMA IF EXISTS employees CASCADE;
CREATE SCHEMA employees;

CREATE TABLE employees.employe (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	phone VARCHAR(255),
	email VARCHAR (255)
);

SELECT * FROM employees.employe;

UPDATE employees.employe
SET nom = 'NouveauNom', num_pro = 'NouveauNumero', email = 'nouveau@email.com'
WHERE id = 10;