import psycopg2
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import bcrypt

## API authentification
APIusername = "admin"  
APIpassword = "admin" 

## function to connect to DB
def connectToDB():
    conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Achille.500"
            )
    return conn

## partnerClass for POST
class Partner(BaseModel):
    id:int
    name: Optional[str] = None
    phone: Optional[str] = None
    email:Optional[str] = None
        
## DEFINE APP and Security
app = FastAPI()
security = HTTPBasic()

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == APIusername and verify_password(APIpassword,credentials.password,):
        return True
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")



## BASIC GET
@app.get('/')
async def root():
    return {'API working' : 'hey there buddy'}


## GET ALL PARTNERS
@app.get('/partners/')
async def getAllPartners():

    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # request to execute
        querry ='SELECT * FROM partners.partner'
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



## GET  PARTNER BY ID
@app.get('/partners/{id}')
async def getPartnerById(id:int):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = 'SELECT * FROM partners.partner WHERE id = ' + str(id)
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


## ADD NEW PARTNER
@app.post('/partners/')
async def addPartner(partner:Partner, authenticated: bool = Depends(authenticate_user)):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = f"INSERT INTO partners.partner (id,name,phone,email) VALUES ({partner.id}, '{partner.name}', '{partner.phone}', '{partner.email}');"
        res = cursor.execute(querry)
        conn.commit()
        cursor.close()
        conn.close()
        return res
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()
        
## UPDATE PARTNER BY ID
@app.put('/partners/{partnerID}')
async def updatePartner(partnerID:int, partner:Partner, authenticated: bool = Depends(authenticate_user)):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = f"UPDATE partners.partner SET name = '{partner.name}', phone = '{partner.phone}', email =  '{partner.email}' WHERE id = {partnerID};"
        res = cursor.execute(querry)
        conn.commit()
        cursor.close()
        conn.close()
        return res
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()


## DELETE PARTNER
@app.delete('/partners/{partnerID}')
async def deletePartner(partnerID:int, authenticated: bool = Depends(authenticate_user)):
    try:
        # connection a la db
        conn = connectToDB()
        cursor = conn.cursor()

        # the request to execute
        querry = f"DELETE FROM partners.partner WHERE id = {partnerID};"
        res = cursor.execute(querry)
        conn.commit()
        cursor.close()
        conn.close()
        return res
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()




    






