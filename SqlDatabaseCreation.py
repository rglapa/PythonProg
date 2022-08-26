import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ruben",
    password="CENTAUR"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")