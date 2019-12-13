import sqlite3
import pandas as pd
from random import randint
import time, datetime
from decimal import Decimal

def function(wooo):
    print("wooo")

def create_sqlite_connection(db_filename):
    conn = None
    try:
        conn = sqlite3.connect(db_filename)
    except:
        print('connection failed')

    return conn

#print("1. View Species Information ")
#print("2. Insert New Species Data")  # what is the diff exactly?
#print("3. Update Species Data ")
#print("4. Add Extinct Species Information ")

def View_Data(sqlite_cur):
def Insert_species(sqlite_cur):
def Update_Species(sqlite_cur):
def Populate_Extinct_Species(sqlite_cur):

    # INSERT statement
    insert_sql = '''INSERT INTO goods(item_id, flavor, food, price)
                         VALUES (?,?,?,?)'''

    insert_vals = ('1', 'Strawberry', 'Ice Cream', 10.50)
    sqlite_cur.execute(insert_sql, insert_vals)

    # UPDATE statement
    update_sql = '''UPDATE goods
                       SET flavor = ?
                     WHERE item_id = ?
                 '''

    update_vals = ('Vanilla', '1')

    sqlite_cur.execute(update_sql, update_vals)

    # SELECT statement
    sqlite_cur.execute('SELECT * FROM goods;')

    result = sqlite_cur.fetchall()

    for row in result:
        print(row)

    # Load DB to pandas for analysis
    sqlite_pandas = pd.read_sql('SELECT * FROM goods;', con=sqlite_conn)

    print(sqlite_pandas.head())
