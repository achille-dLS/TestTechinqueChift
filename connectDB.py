import psycopg2
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

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

conn.close()

