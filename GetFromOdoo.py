import xmlrpc.client 
import json
import requests
from APIEmployees import Partner

url = 'https://chift-employees.odoo.com'
db = 'chift-employees'
username = 'achilledelimburgstirum@gmail.com'
password = 'mdp1234'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#Auth
uid = common.authenticate(db,username,password,{})
if uid:
    print("auth ok : ",uid)
else:
    print("auth KO !")
    exit(1) 

#connect
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# search all partners ID
partnersID = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])
#read all partners
partnersInfo = models.execute_kw(db, uid, password, 'res.partner', 'read', [partnersID], {'fields': ['id', 'name','phone', 'email']})
print("get partners From Odoo : OK \n\n ")

#place partners in Dictionary
odooPartnersDict = {}
for p in partnersInfo:
    id = p["id"]
    if 'phone' not in p or not isinstance(p['phone'], str):
            p['phone'] = ''
    if 'email' not in p or not isinstance(p['email'], str):
            p['email'] = ''
    odooPartnersDict[id] = p

# get partners in DB
response = requests.get('http://127.0.0.1:8000/partners')
DBPartners = response.json()
print("get partners From BD : OK \n\n ")


#place partners in Dictionary
DBPartnersDict = {}
for p in DBPartners:
    id = p[0]
    DBPartnersDict[id] = {
    "id": p[0],
    "name": p[1],
    "phone": p[2],
    "email": p[3]
    }

print("updating DB....")

for id in odooPartnersDict:
    OdPart = odooPartnersDict.get(id)
    BdPart = DBPartnersDict.get(id)
    #check if all partners are in DB
    if BdPart == None or OdPart['id']!=BdPart['id']:
        print("missing partner with id : ",id, OdPart)
        response = requests.post("http://localhost:8000/partners/", json=OdPart)
        print("response Code : ",response.status_code)
    # check if content BD partner are Up to date
    elif OdPart != BdPart:
        ## update tous les champs de ce truc bidule
        print("DB not up to date for partner n° :",id)
        print("bdpart : ",BdPart)
        print("odPart : ",OdPart)
    
    ## ajouter façon de vérifier que la db ne garde pas des trucs inutile (partner qui a été supprimé)
    ## pour le moment idée : array de tous les ID de la DB, quand on en passe un, on le retire de cette liste, a la fin on fait un delete sur chaque ID qui reste dans la liste




print("\n\n_______________END UPDATE DB ________________\n\n")

