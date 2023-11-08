DROP SCHEMA IF EXISTS partners CASCADE;
CREATE SCHEMA partners;

CREATE TABLE partners.partner (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	phone VARCHAR(255),
	email VARCHAR (255)
);

SELECT * FROM partners.partner;

UPDATE partners.partner
SET name = 'NouveauNom', phone = 'NouveauNumero', email = 'nouveau@email.com'
WHERE id = 10;

INSERT INTO partners.partner (name, phone, email)
VALUES ('Mr TooMuch', +32547885412, 'TooMuch@gmail.com');