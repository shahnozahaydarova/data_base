import sqlite3 as sql
aa = sql.connect("main.db")
malumot = aa.cursor()
malumot.execute('''
CREATE TABLE IF NOT EXISTS odamlar(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
)
''') 