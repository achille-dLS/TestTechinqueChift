# TestTechinqueChift
test technique pour entretien chift

# contenu de la DB
une table partner dans un shema partners. a créer en local avec init.sql
Init.sql contient aussi un ajout de table et modification pour tester l'API

# l'API
Possède les crud classique (getall, getone, add, update, delete)
sécurité mise sur les requêtes de type :  add, update et delete

# le script principal
récupère les données de Odoo
récupère les données de la DB via l'API
mets la DB a jour via l'API pour qu'elles correspondent a celles de Odoo

# ce qu'il manque
la répétition du script avec un cron
déploiment de l'app sur une solution d'hébergement car les app comme Azure et goolge cloud platform demandent une carte bancaire mastercard pour l'authentification et je n'en ai pas
