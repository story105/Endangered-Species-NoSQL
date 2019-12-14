import sqlite3
import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 8)
pd.set_option('display.width', 1000)
from random import randint
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
    print("Type the corresponding number:")
    print("1. View ALL species information ")
    print("2. View species by STATE information ")
    print("3. View State regions ")
    print("4. View species based on threatened level ")
    try:
        choice = int(input())
    except:
        print("Invalid Choice")
        print("")
        choice = 1

    if choice == 1:
        sqlite_cur.execute('''SELECT o.organism, t.Tspecies, fs.federal_status, t.Tunit, t.TUSstate
                                    FROM Main as t
                                    LEFT JOIN Organism AS o
                                    ON t.Torganism = o.organism_id
                                    LEFT JOIN Federal_Status AS fs
                                    ON t.Tfederal_status = fs.federal_status_id
                                    ''')
        result = sqlite_cur.fetchall()
        for row in result:
            print(row)
        # to see difference
        print("")
    elif choice == 2:
        print("Please enter a state to view information for (Ex: CA): ")
        StateGiven = input().upper()
        sqlite_pandas = pd.read_sql('''SELECT *
                                    FROM Main
                                    WHERE Tunit LIKE '%''' + StateGiven + '''%';''', con=sqlite_conn)
        print(sqlite_pandas)
        print("")

    elif choice == 3:
        print("Please enter a region to view information for (Ex: Lake): ")
        RegionGiven = input().upper()
        sqlite_pandas = pd.read_sql('''SELECT *
                                    FROM Main
                                    WHERE Tunit LIKE '%''' + RegionGiven + '''%';''', con=sqlite_conn)

        print(sqlite_pandas)
        print("")
    elif choice == 4:
        print("Please type which federal protection status of species you wish to view: ")
        print("1 = Threatened ")
        print("2 = Endangered ")
        print("3 = Proposed ")
        try:
            choice2 = input()
        except:
            print("Invalid Choice")
            print("")
            choice2 = '1'

        sqlite_pandas = pd.read_sql('''SELECT t.Torganism, t.Tspecies, t.Tunit, t.TUSstate
                                    FROM Main as t
                                    WHERE Tfederal_status=''' + choice2 + ';', con=sqlite_conn)
        print(sqlite_pandas)
        print("")

    print("")
    # Load DB to pandas for analysis

#-----------------------------------------------------------------------------
def Insert_species(sqlite_cur,sqlite_conn):
    # INSERT statement
    print("Please enter the organism to insert: ")
    OrgGiven = input()
    print("Please enter the species: ")
    SpeciesGiven = input()
    print("Please denote the federal status of organism: ")
    FSGiven = input()
    print("Please input the region the organism was spotted inhabiting: ")
    RegionGiven = input()
    print("Please enter the regions state(s): ")
    StateGiven = input()

    sqlite_cur.execute('''SELECT organism_id
                        FROM Organism
                        WHERE organism = ''' + OrgGiven + ';')
    result = sqlite_cur.fetchall()

    sqlite_cur.execute('''SELECT federal_status_id
                        FROM Federal_Status
                        WHERE federal_status = ''' + FSGiven + ';')
    result2 = sqlite_cur.fetchall()

    OrgGiven = result
    FSGiven = result2
    insert_sql = '''INSERT INTO Main(Torganism, Tspecies, Tfederal_status, Tunit, TUSstate)
                         VALUES (?,?,?,?,?)'''
    insert_vals = (OrgGiven, SpeciesGiven, FSGiven, RegionGiven, StateGiven)
    sqlite_cur.execute(insert_sql, insert_vals)


#-----------------------------------------------------------------------------
def Update_Species(sqlite_cur,sqlite_conn):
    # UPDATE statement


    print("What attribute would you like to update? Ex: Region")
    choice = input()

    print("For what species?")
    choice2 = input()
    sqlite_pandas = pd.read_sql('''SELECT *
                                FROM Main
                                WHERE Tspecies LIKE '%''' + choice2 + '''%';''', con=sqlite_conn)
    print(sqlite_pandas)

    print("What is the new FS? (Ex: Endangered)")
    choice3 = input()


    choice = 'T' + choice
    update_sql = 'UPDATE Main SET ' + choice + ' = ? WHERE Tspecies = ?'
    update_vals = (choice, choice3, choice2)
    sqlite_cur.execute(update_sql, update_vals)

    sqlite_pandas = pd.read_sql('''SELECT *
                                FROM Main
                                WHERE Tspecies LIKE '%''' + choice2 + '''%';''', con=sqlite_conn)
    print(sqlite_pandas)
    print("")





#-----------------------------------------------------------------------------
def Populate_Extinct_Species(sqlite_cur,sqlite_conn):
    # INSERT statement
    insert_sql = '''INSERT INTO Extinct(extinct)
                         VALUES (?)'''
    print("Please enter organism name that is now extinct: ")
    inputtedStuff = input()
    insert_vals = [inputtedStuff]
    sqlite_cur.execute(insert_sql, insert_vals)

    print("")
    sqlite_pandas = pd.read_sql('''SELECT * FROM Extinct;''', con=sqlite_conn)
    print(sqlite_pandas.head())
    print("")
