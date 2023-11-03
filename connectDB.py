import psycopg2



class Employe:
    def __init__(self,id,nom,num_pro,email,departement):
        self.id = id
        self.nom = nom
        self.num_pro = num_pro
        self.email = email
        self.departement = departement

try:
    # connection a la db
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Achille.500"
        )


    cursor = conn.cursor()

    # get all employees
    print('get all employees')
    # the request to execute
    cursor.execute('SELECT * FROM employees.employe')
    # getting the answer to the request
    employees = cursor.fetchall()
    # print answer
    print(employees)

    # get one employees
    print('get 1st employe name')
    # the request to execute
    cursor.execute('SELECT * FROM employees.employe WHERE id = 1')
    # getting the answer to the request
    rs = cursor.fetchone()
    employe1 = Employe(rs[0],rs[1],rs[2],rs[3],rs[4])
    # print answer

    print(employe1.nom)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

conn.close()

