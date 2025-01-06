import mysql.connector

# Connect to MySQL
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='sfyt'  # Replace 'sfyt' with your MySQL root user's password
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE sfytco")

print("Database 'sfytco' created successfully!")
