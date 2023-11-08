import psycopg2
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import bcrypt


APIusername = "admin"  
APIpassword = b'$2y$10$t6ueu.1FuvyBf6iFegQEguq3XF1G.epvn2LvxbS5rcDsr7hvYDKtq' 

def connectToDB():
    conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Achille.500"
            )
    return conn


class Partner(BaseModel):
    id:int
    name: Optional[str] = None
    phone: Optional[str] = None
    email:Optional[str] = None
        

app = FastAPI()
security = HTTPBasic()

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == APIusername and verify_password(credentials.password, APIpassword):
        return True
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


## REQUETES API
@app.get('/')
async def root():
    return {'API working' : 'hey there buddy'}

@app.get('/partners/')
async def getAllPartners():

    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # request to execute
        querry ='SELECT * FROM employees.employe'
        cursor.execute(querry)
        
        # getting the answer to the request
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()


@app.get('/partners/{id}')
async def getPartnerById(id:int):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = 'SELECT * FROM employees.employe WHERE id = ' + str(id)
        cursor.execute(querry)

        # getting the answer to the request
        rs = cursor.fetchone()
        cursor.close()
        conn.close()
        return rs
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()

@app.post('/partners/')
async def addPartner(partner:Partner, authenticated: bool = Depends(authenticate_user)):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = f"INSERT INTO employees.employe (id,name,phone,email) VALUES ({partner.id}, '{partner.name}', '{partner.phone}', '{partner.email}');"
        res = cursor.execute(querry)
        conn.commit()
        cursor.close()
        conn.close()
        return res
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()
        
@app.put('/partners/{partnerID}')
async def addPartner(partnerID:int, partner:Partner, authenticated: bool = Depends(authenticate_user)):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = f"UPDATE employees.employe SET name = '{partner.name}', phone = '{partner.phone}', email =  '{partner.email}' WHERE id = {partnerID};"
        res = cursor.execute(querry)
        conn.commit()
        cursor.close()
        conn.close()
        return res
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()

@app.delete('/partners/{partnerID}')
async def addPartner(partnerID:int, authenticated: bool = Depends(authenticate_user)):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = f"DELETE FROM employees.employe WHERE id = {partnerID};"
        res = cursor.execute(querry)
        conn.commit()
        cursor.close()
        conn.close()
        return res
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()




    






