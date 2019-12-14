import sqlite3
import pandas as pd
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
        sqlite_cur.execute('''SELECT o.organism, s.species, fs.federal_status, r.unit, us.USstate
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
        print("")
    elif choice == 3:
        print("Please enter a state to view information for (Ex: CA): ")
        StateGiven = input().upper()
        sqlite_cur.execute('''SELECT r.unit
                            FROM region AS r
                            INNER JOIN Main AS m
                            ON m.unit_id = r.unit_id
                            INNER JOIN USstate AS us
                            ON m.USstate_id = us.USstate_id
                            WHERE us.USstate = ''' + StateGiven + ';')
        result = sqlite_cur.fetchall()
        print("")
    elif choice == 4:
        print("Please type which federal protection status of species you wish to view: ")
        print("1 = Threatened ")
        print("2 = Endangered ")
        try:
            choice2 = int(input())
        except:
            print("Invalid Choice")
            print("")
            choice2 = 1

        sqlite_cur.execute('''SELECT o.organism, s.species, r.unit, us.USstate
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
                            WHERE fs.federal_status_id = ''' + choice2 + ';')
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

#-----------------------------------------------------------------------------
def Insert_species(sqlite_cur,sqlite_conn):
    # INSERT statement
    insert_sql = '''INSERT INTO goods(item_id, flavor, food, price)
                         VALUES (?,?,?,?)'''

    insert_vals = ('1', 'Strawberry', 'Ice Cream', 10.50)
    sqlite_cur.execute(insert_sql, insert_vals)

    print("Please enter a state to view information for (Ex: CA): ")
    StateGiven = input()


#-----------------------------------------------------------------------------
def Update_Species(sqlite_cur,sqlite_conn):
    # UPDATE statement
    update_sql = '''UPDATE goods
                       SET flavor = ?
                     WHERE item_id = ?
                 '''

    update_vals = ('Vanilla', '1')
    sqlite_cur.execute(update_sql, update_vals)

    print("Please enter a PK to edit information for (Ex: 428 || 0 to exit): ")
    try:
        choicePK = int(input())
    except:
        print("Invalid choice")
        choicePK = 0

    if choicePK == 0:
        print("Please view table data to see PK")
    elif choicePK > 0: # any other Pk
        sqlite_cur.execute('''SELECT organism_id,species_id,federal_status_id,unit_id,state_id
                            FROM Main
                            WHERE PK = ''' + choicePK + ';')
        result = sqlite_cur.fetchall()

        for row in result: # want to draw IDs from this to insert better
            print(row)
            #  NEED IDS FROM HERE? DICT MAYBE?

        print("Please enter new organism name: ")
        orgInp = input()
        print("Please enter new species name: ")
        speciesInp = input()
        print("Please enter new federal status: ")
        fsInp = input()
        print("Please enter new region name: ")
        regionInp = input()
        print("Please enter new state organism found in: ")
        stateInp = input()

        update_sql = '''UPDATE Organism
                        SET organism = ?
                        WHERE organism_id = ?
                        '''
        update_vals = (orgInp, '1') #val from dict
        sqlite_cur.execute(update_sql, update_vals)

        update_sql = '''UPDATE Species
                        SET species = ?
                        WHERE species_id = ?
                        '''
        update_vals = (speciesInp, '1') #val from dict
        sqlite_cur.execute(update_sql, update_vals)

        update_sql = '''UPDATE Federal_Status
                        SET federal_status = ?
                        WHERE federal_status_id = ?
                        '''
        update_vals = (fsInp, '1') #val from dict
        sqlite_cur.execute(update_sql, update_vals)

        update_sql = '''UPDATE Region
                        SET unit = ?
                        WHERE unit_id = ?
                        '''
        update_vals = (regionInp, '1') #val from dict
        sqlite_cur.execute(update_sql, update_vals)

        update_sql = '''UPDATE USstate
                        SET main_id = ?
                        WHERE extinct_id = ?
                        '''
        update_vals = (stateInp, '1') #val from dict
        sqlite_cur.execute(update_sql, update_vals)


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
    sqlite_cur.execute('''SELECT * FROM Extinct;''')
    result = sqlite_cur.fetchall()
    for row in result:
        print(row)
