import sqlite3 as sql

b = sql.connect("Odamlar.db")

m = b.cursor()

m.execute('''
CREATE TABLE IF NOT EXISTS  Student(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
    kurs TEXT
)
''')

m. execute('''
CREATE TABLE IF NOT EXISTS Programist(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
    staj INTEGER
)
''')
m. execute('''
CREATE TABLE IF NOT EXISTS Bekorchi(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
    boshvaqti TEXT
)
''')
m. execute('''
CREATE TABLE IF NOT EXISTS Oqituvchi(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
    oylik INTEGER
)
''')
m. execute('''
CREATE TABLE IF NOT EXISTS abiturient(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
    yonalish TEXT
)
''')
m. execute('''
CREATE TABLE IF NOT EXISTS tikuvchi(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    ishqurol TEXT
)
''')