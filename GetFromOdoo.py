import xmlrpc.client 


url = 'https://chift-employees.odoo.com'
db = 'chift-employees'
username = 'achilledelimburgstirum@gmail.com'
password = 'mdp1234'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#Auth
uid = common.authenticate(db,username,password,{})
if uid:
    print("auth ok : ",uid) 

#connect
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# search
partnersID = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])

print(partnersID)

#read
partnersInfo = models.execute_kw(db, uid, password, 'res.partner', 'read', [partnersID], {'fields': ['id', 'name','phone', 'email']})
print(partnersInfo)