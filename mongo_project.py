import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    print("")

    option = input("Enter option: ")
    return option

def main_loop():
    while True:
        # Call the menu defined above
        option = show_menu()
        if option == '1':
            print("Called option 1") 
        elif option == '2':
            print("Called option 2") 
        elif option == '3':
            print("Called option 3") 
        elif option == '4':
            print("Called option 4") 
        elif option == '5':
            conn.close
            break
        else:    
            print("Invalid option") 
        print("")

# Connect to the database passing in the environment variable set up with the connection string.
conn = mongo_connect(MONGODB_URI)

# Set our collection name on this database.
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
