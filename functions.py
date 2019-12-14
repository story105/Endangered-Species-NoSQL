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
        sqlite_pandas = pd.read_sql('''SELECT o.organism, t.Tspecies, fs.federal_status, t.Tunit, t.TUSstate
                                    FROM Main as t
                                    LEFT JOIN Organism AS o
                                    ON t.Torganism = o.organism_id
                                    LEFT JOIN Federal_Status AS fs
                                    ON t.Tfederal_status = fs.federal_status_id
                                    ''', con=sqlite_conn)
        print(sqlite_pandas)
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
    sqlite_pandas = pd.read_sql('''SELECT * FROM Extinct;''', con=sqlite_conn)
    print(sqlite_pandas.head())
    print("")
