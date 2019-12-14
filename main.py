# python -m pip install XXX
import tableprint as tp
import functions


def main():

    print("--- Welcome to the Endangered Species Database ---")
    choice = 1
    # create SQLite connection and cursor
    sqlite_conn = functions.create_sqlite_connection('final_project.db') #change for others
    sqlite_cur = sqlite_conn.cursor()
    #now use this connection and pointer to pass into the functions
    while choice != 0:
        print("--- Main Menu --- ")
        print("1 = View Species Information ")
        print("2 = Insert New Species Data")
        print("3 = Update Species Data ")
        print("4 = Add Extinct Species Information ")
        print("0 = Quit ")

        try:
            choice = int(input())
        except:
            print("Invalid Choice")
            choice = 420
            continue

        if choice == 1:
            functions.View_Data(sqlite_cur,sqlite_conn);

        elif choice == 2:
            functions.Insert_species(sqlite_cur,sqlite_conn);

        elif choice == 3:
            functions.Update_Species(sqlite_cur,sqlite_conn);

        elif choice == 4:
            functions.Populate_Extinct_Species(sqlite_cur,sqlite_conn);

        elif choice == 0:
            tp.banner("Exiting Application") # if yours doesn' run change any tp to print
        else:
            print("Error: invalid choice received. Please re-enter an integer ")


if __name__ == "__main__":
	main()
