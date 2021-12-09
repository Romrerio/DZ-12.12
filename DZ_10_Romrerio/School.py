import sqlite3
from sqlite3.dbapi2 import Cursor, connect

def classes():
    database_name = "School.db"
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    query_create = "CREATE TABLE IF NOT EXISTS classes (id INT, class CHAR, num_of_stud INT, teacher CHAR)"
    cursor.execute(query_create)
    querty_insert = 'INSERT INTO classes VALUES (002, "1B", 24, "Galina Evgenievna")'
    querty_seleckt = 'SELECT * FROM classes'
    cursor.execute(querty_insert)
    cursor.execute(querty_seleckt)
    connection.commit()
    connection.close()

def students():
    database_name = "School.db"
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    query_create = "CREATE TABLE IF NOT EXISTS students (id INT, familia CHAR, imya CHAR, otchestvo CHAR, class CHAR, vera_v_putina CHAR)"
    cursor.execute(query_create)
    querty_insert = 'INSERT INTO students VALUES (001, "Pupkin", "Vasya", "Dimovich", "1B","100%")'
    querty_seleckt = 'SELECT * FROM students'
    cursor.execute(querty_insert)
    cursor.execute(querty_seleckt)
    connection.commit()
    connection.close()

classes()
students()