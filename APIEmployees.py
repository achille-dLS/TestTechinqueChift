import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



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
async def addPartner(partner:Partner):
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
async def addPartner(partnerID:int, partner:Partner):
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
async def addPartner(partnerID:int):
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




    






