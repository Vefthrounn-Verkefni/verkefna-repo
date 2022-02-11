import mysql.connector

mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd = "password123"
                                )

my_cursor = mydb.cursor()


# my_cursor.execute("DROP DATABASE flask_database") # til þess að reseta databaseið 
my_cursor.execute("CREATE DATABASE flask_database")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
<<<<<<< HEAD
<<<<<<< HEAD
    print(db)
=======
    print(db)
    
>>>>>>> b2368efc24928e02e8c72c2403bbca619674efd2
=======
    print(db)
>>>>>>> d1c092a5e56101e9d3d742ce3b7e32581adc8a0c
