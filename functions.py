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

def View_Data(sqlite_cur,sqlite_conn):
    # SELECT statement
    print("1. View ALL information ")
    print("2. View STATE information ")
    try:
        choice = int(input())
    except:
        print("Invalid Choice")
        print("")
        choice = 1
        continue

    if choice == 1:
        sqlite_cur.execute('''SELECT m.PK, o.organism, s.species, fs.federal_status, r.unit, us.USstate
                            FROM Main as m
                            LEFT JOIN Organism AS o
                            ON m.organism_id = o.organism_id
                            LEFT JOIN Species AS s
                            ON m.species_id = s.species_id
                            LEFT JOIN Federal_Status AS fs
                            ON m.federal_status_id = fs.federal_status_id
                            LEFT JOIN Region AS r
                            ON m.unit_id = r.unit_id
                            LEFT JOIN USstate AS us
                            ON m.USstate_id = us.USstate_id
                            ''')
        result = sqlite_cur.fetchall()
    print("")
    elif choice == 2:
        print("Please enter a state to view information for (Ex: CA): ")
        StateGiven = input().upper()
        sqlite_cur.execute('''SELECT m.PK, o.organism, s.species, fs.federal_status, r.unit, us.USstate
                            FROM Main as m
                            LEFT JOIN Organism AS o
                            ON m.organism_id = o.organism_id
                            LEFT JOIN Species AS s
                            ON m.species_id = s.species_id
                            LEFT JOIN Federal_Status AS fs
                            ON m.federal_status_id = fs.federal_status_id
                            LEFT JOIN Region AS r
                            ON m.unit_id = r.unit_id
                            LEFT JOIN USstate AS us
                            ON m.USstate_id = us.USstate_id
                            WHERE us.USstate = ''' + StateGiven + ';')
        result = sqlite_cur.fetchall()

    for row in result:
        print(row)
    print("")
    print("")
    # Load DB to pandas for analysis
    sqlite_pandas = pd.read_sql('''SELECT m.PK, o.organism, s.species, fs.federal_status, r.unit, us.USstate
                                FROM Main as m
                                LEFT JOIN Organism AS o
                                ON m.organism_id = o.organism_id
                                LEFT JOIN Species AS s
                                ON m.species_id = s.species_id
                                LEFT JOIN Federal_Status AS fs
                                ON m.federal_status_id = fs.federal_status_id
                                LEFT JOIN Region AS r
                                ON m.unit_id = r.unit_id
                                LEFT JOIN USstate AS us
                                ON m.USstate_id = us.USstate_id
                                ''', con=sqlite_conn)
    print(sqlite_pandas.head())
    # to see difference
    print("")

def Insert_species(sqlite_cur,sqlite_conn):
    # INSERT statement
    insert_sql = '''INSERT INTO goods(item_id, flavor, food, price)
                         VALUES (?,?,?,?)'''

    insert_vals = ('1', 'Strawberry', 'Ice Cream', 10.50)
    sqlite_cur.execute(insert_sql, insert_vals)

def Update_Species(sqlite_cur,sqlite_conn):
    # UPDATE statement
    update_sql = '''UPDATE goods
                       SET flavor = ?
                     WHERE item_id = ?
                 '''

    update_vals = ('Vanilla', '1')

    sqlite_cur.execute(update_sql, update_vals)

def Populate_Extinct_Species(sqlite_cur,sqlite_conn):
    # INSERT statement
    insert_sql = '''INSERT INTO goods(item_id, flavor, food, price)
                         VALUES (?,?,?,?)'''

    insert_vals = ('1', 'Strawberry', 'Ice Cream', 10.50)
    sqlite_cur.execute(insert_sql, insert_vals)
