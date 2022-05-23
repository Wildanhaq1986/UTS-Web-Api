import sqlite3
from msilib.text import tables

DATABASE_NAME = "academic.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table_students():
    tables = [
            """CREATE TABLE IF NOT EXISTS
                tbl_students(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nim TEXT NOT NULL,
                    nama TEXT NOT NULL,
                    jurusan TEXT NOT NULL,
                    alamat TEXT NOT NULL)""" 
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)


def create_table_users():
    tables = [
            """CREATE TABLE IF NOT EXISTS
                tbl_users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    uername TEXT NOT NULL,
                    password TEXT NOT NULL,
                    students_id TEXT NOT NULL,
                    FOREIGN KEY("students_id") REFERENCES "tbl_students"("id"))""" 
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)