Voici le fichier README.md corrigé avec l'orthographe et la mise en page améliorés :

# Test Technique Chift
Test technique pour l'entretien chez Chift.

## Contenu de la Base de Données
- Une table "partner" dans un schéma "partners" doit être créée localement en utilisant le fichier "init.sql".
- Le fichier "init.sql" contient également des ajouts de tables et des modifications pour tester l'API.

## L'API
L'API offre les fonctionnalités CRUD classiques :
- "getall" : Récupère tous les éléments.
- "getone" : Récupère un élément par son identifiant.
- "add" : Ajoute un nouvel élément.
- "update" : Met à jour un élément.
- "delete" : Supprime un élément.

La sécurité est mise en place pour les requêtes de type "add," "update," et "delete."

## Le Script Principal
Le script principal réalise les étapes suivantes :
1. Récupère les données depuis Odoo.
2. Récupère les données depuis la base de données en utilisant l'API.
3. Met à jour la base de données via l'API pour qu'elle corresponde aux données d'Odoo.

## Ce Qu'il Manque
Il manque les éléments suivants :
- La répétition du script avec un système de planification (cron).
- Le déploiement de l'application sur une solution d'hébergement, car des services tels qu'Azure et Google Cloud Platform exigent une carte bancaire Mastercard pour l'authentification, que je ne possède pas actuellement.
