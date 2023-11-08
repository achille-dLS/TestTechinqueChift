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
SET nom = 'NouveauNom', num_pro = 'NouveauNumero', email = 'nouveau@email.com'
WHERE id = 10;