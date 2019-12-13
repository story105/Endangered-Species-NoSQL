# Make sure that its ACID property stays
# python -m pip install XXX

import tableprint as tp
import functions


def main():


    print("--- Welcome to the Endangered Species Database ---")
    print("")
    print("0. Quit")
    try:
        choice = int(input())
    except:
        print("Invalid Choice")
        choice = 0
    if choice == 0:
        tp.banner("Thank you for using our app")
    else:
        # create SQLite connection and cursor
        sqlite_conn = functions.create_sqlite_connection('../../labs/lab4_joins/lab2.db')
        sqlite_cur = sqlite_conn.cursor()
        #now use this connection and pointer to pass into the functions
    while choice != 0:
        print("--- Main Menu --- ")
        print("1. View Species Information ")
        print("2. Insert New Species Data")  # what is the diff exactly?
        print("3. Update Species Data ")
        print("4. Add Extinct Species Information ")
        print("0. Quit ")

        try:
            choice = int(input())
        except:
            print("Invalid Choice")
            choice = 420
            continue

        if choice == 1:
            functions.Create_Account();

        elif choice == 2:
            functions.sign_in();

        elif choice == 3:
            functions.add_withdrawl_balance();

        elif choice == 4:
            functions.transfer_money();

        elif choice == 0:
            tp.banner("Exiting Application") # if yours doesn' run change any tp to print
        else:
            print("Error: invalid choice received. Please re-enter an integer ")


if __name__ == "__main__":
	main()
