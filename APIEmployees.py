import psycopg2
from fastapi import FastAPI



class Employe:
    def __init__(self,id,nom,num_pro,email,departement):
        self.id = id
        self.nom = nom
        self.num_pro = num_pro
        self.email = email
        self.departement = departement

app = FastAPI()

## REQUETES API
@app.get('/')
async def root():
    return {'API working' : 'hey there buddy'}

@app.get('/employees/')
async def getAllEmployees():

    try:
        # connection a la db
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Achille.500"
            )
        cursor = conn.cursor()
        # request to execute
        cursor.execute('SELECT * FROM employees.employe')
        # getting the answer to the request
        employees = cursor.fetchall()
        cursor.close()
        return employees
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()


@app.get('/employees/{id}')
async def getEmployeById(id:int):
    try:
        # connection a la db
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Achille.500"
            )
        cursor = conn.cursor()

        
        # the request to execute
        querry = 'SELECT * FROM employees.employe WHERE id = ' + str(id)
        cursor.execute(querry)
        # getting the answer to the request
        rs = cursor.fetchone()
        employe1 = Employe(rs[0],rs[1],rs[2],rs[3],rs[4])
        cursor.close()
        return employe1
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()




    






