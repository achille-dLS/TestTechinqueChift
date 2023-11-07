import xmlrpc.client 
import json
import requests

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
    odooPartnersDict[id] = p

# get partners in DB
response = requests.get('http://127.0.0.1:8000/partners')
DBPartners = response.json()
print("get partners From BD : OK \n\n ")


#place partners in Dictionary
DBPartnersDict = {}
for p in DBPartners:
    id = p[0]
    DBPartnersDict[id] = p


print("updating DB....")

for id in odooPartnersDict:
    OdPart = odooPartnersDict.get(id)
    BdPart = DBPartnersDict.get(id)
    #check if all partners are in DB
    if OdPart['id']!=BdPart[0]:
        OdPart = odooPartnersDict.get(id)
        if 'phone' not in OdPart or not isinstance(OdPart['phone'], str):
            OdPart['phone'] = ''
        if 'email' not in OdPart or not isinstance(OdPart['email'], str):
            OdPart['email'] = ''
        print("missing partner with id : ",id, odooPartnersDict.get(id))
        response = requests.post("http://localhost:8000/partners/", json=odooPartnersDict.get(id))
        print("response Code : ",response.status_code)
    # check if content BD partner are Up to date
    if OdPart != BdPart:
            print("DB not up to date for partner n° :",id)


print("\n\n_______________END UPDATE DB ________________\n\n")

