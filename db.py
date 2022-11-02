import sqlite3 as sql

o = sql.connect("Odam.db")
m1=o.cursor()
m1.execute('''
CREATE TABLE IF NOT EXISTS Programist(
    ism TEXT
    sohasi FLOAT,    
    maosh FLOAT,
    tajriba INTEGER
)
''')
m1.execute('''
CREATE TABLE IF NOT EXISTS Oqituvchi(
    ism TEXT,
    tajriba FLOAT
    fani TEXT,
    maosh FLOAT
)
''')





h = sql.connect("Hayvon.db")
m2 =h.cursor()
m2.execute('''
CREATE TABLE IF NOT EXISTS OT(
    ismi TEXT,
    ozuqasi TEXT,
    vazni FLOAT,
    rangi TEXT
)
''')
m2.execute('''
CREATE TABLE IF NOT EXISTS IT(
    laqabi TEXT,
    vazni  FLOAT,
    rang TEXT,
    ozuqasi TEXT
)
''')



g = sql.connect("Gul.db")
m3=g.cursor()
m3.execute('''
CREATE TABLE IF NOT EXISTS LOLA(
    rang TEXT,
    uzunligi FLOAT,
    narx FLOAT
)
''')
m3.execute('''
CREATE TABLE IF NOT EXISTS ATIRGUL(
    rang TEXT,
    uzunligi FLOAT,
    narxi FLOAT
)
''')


a = sql.connect("Avtomobil.db")
m4 = a.cursor()
m4.execute('''
CREATE TABLE IF NOT EXISTS MATIZ(
    rang TEXT,
    narx FLOAT,
    chiqganyili INTEGER
)
''')
m4.execute('''
CREATE TABLE IF NOT EXISTS MALIBU(
    rang TEXT,
    narx FLOAT,
    chiqganyili INTEGER
)
''')

