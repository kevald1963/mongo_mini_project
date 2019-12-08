import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        #print("Connected successfully to MongoDB!")
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

def get_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")

    try:
        doc = coll.find_one({'first': first.title(), 'last': last.title()})
    except:
        print("Error on searching for document.")

    # Handle a 'not found' condition. This is not an error as such. The record just isn't there!
    if not doc:
        print("")
        print("Sorry, no results found for " + first.title() + " " + last.title() + ".")

    return doc

def find_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != '_id':
                print(key + ": " + value)

def edit_record():
    doc = get_record()
    if doc:
        # Define an empty dictionary in which to build the update record.
        update_doc = {}
        print("")
        for key, value in doc.items():
            if key != '_id':
                # Populate the dictionary with each entered value.
                # Set the new value to title case before storing in dictionary.
                new_value = input(key.title() + " [ " + value.title() + " ] : ")
                update_doc[key] = new_value.title() 
                # Not every value may be changed, so revert to the original value is set to null.
                if update_doc[key] == "":
                    update_doc[key] = value
        
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated.")
        except:
            print("Error on updating document.")

def delete_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != '_id':
                print(key + ": " + value)

        print("")
        confirmation = input("Is this the document you want to delete?\n(Y or N) ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.delete_one(doc)
                print("Document deleted.")
            except:
                print("Error on deleting document.")
        else:
            print("Document not deleted!")

def add_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    hair_colour = input("Enter hair colour: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")

    new_doc = {'first': first.title(), 
               'last': last.title(),
               'dob': dob,
               'gender': gender.upper(),
               'hair_colour': hair_colour.title(),
               'occupation': occupation.title(),
               'nationality': nationality.title()}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted.")
    except:
        print("Error on inserting document.")

def main_loop():
    while True:
        # Call the menu defined above.
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            find_record()
        elif option == '3':
            edit_record()
        elif option == '4':
            delete_record()
        elif option == '5':
            conn.close
            break
        else:    
            print("Invalid option") 
        print("")

# Connect to the database passing in the environment variable set up with the connection string.
conn = mongo_connect(MONGODB_URI)

# Set collection name on this database.
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
