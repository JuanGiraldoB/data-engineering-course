import sqlite3

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()

query = 'SELECT * FROM people LIMIT 10'
count = 0
for result in cursor.execute(query):
    print(result)

print()

query = """SELECT name FROM people LIMIT 10"""
for result in cursor.execute(query):
    print(result)

print()

query = """SELECT name, surname FROM people 
    WHERE name='James'
    ORDER BY name DESC"""
for result in cursor.execute(query):
    print(f"First name: {result[0]} , Lastname: {result[1]}")

print()

query = """
    SELECT name, surname FROM people
    WHERE name like '%s__'

"""
for result in cursor.execute(query):
    print(f"First name: {result[0]} , Lastname: {result[1]}")
