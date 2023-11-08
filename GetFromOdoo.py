import xmlrpc.client 
import requests

## auth for API
auth = ('admin',b'$2y$10$t6ueu.1FuvyBf6iFegQEguq3XF1G.epvn2LvxbS5rcDsr7hvYDKtq')

## fields to connect to ODOO
url = 'https://chift-employees.odoo.com'
db = 'chift-employees'
username = 'achilledelimburgstirum@gmail.com'
password = 'mdp1234'


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#Auth to ODOO
uid = common.authenticate(db,username,password,{})
if uid:
    print("auth ok : ",uid)
else:
    print("auth KO !")
    exit(1) 

#connect to ODOO
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


# get partners in DB with API
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


## updating DB with ODOO DATA
for id in odooPartnersDict:
    OdPart = odooPartnersDict.get(id)
    DBPart = DBPartnersDict.get(id)


    #check if partner is in DB
    if DBPart == None:
        print("missing partner with id : ",id, OdPart)
        response = requests.post("http://localhost:8000/partners/", json=OdPart, auth=auth)
        print("response Code : ",response.status_code)


    # check if content DB partner is Up to date
    else:
        if  OdPart != DBPart:
            ## Update DB partner
            print("DB not up to date for partner n° :",id)
            print("IN DATA BASE : ",DBPart)
            print("IN ODOO : ",OdPart)
            response = requests.put("http://localhost:8000/partners/"+str(id), json=OdPart, auth=auth)
            print("response Code : ",response.status_code)
            ## remove id from DB DICT in order to keep the deleted ones
        DBPartnersDict.pop(id)



#Remove every useless DB Partner
for id in DBPartnersDict:
    print("DELETING personel with ID "+str(id)+ " ("+ str(DBPartnersDict.get(id))+")"+" cause : not in Odoo")
    response = requests.delete("http://localhost:8000/partners/"+str(id), auth=auth)
    print("response Code : ",response.status_code)

print("\n\n_______________END UPDATE DB ________________\n\n")

