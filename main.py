import db


def interatc():
    option = input('''Pick from following option:
                   1. Display
                   2. Insert
                   3. Update  ''')
    if option == "Display":
        table_name = input("enter table name: ")
        db.display(table_name)
    if option == "Insert":
        db.insert()
    if option == "Modify":
        db.modify()
    else:
        print("Exit")

if __name__ == "__main__":
    interatc()