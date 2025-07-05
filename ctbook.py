def add():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")
    print("Contact has been saved!")

def view():
    print("------------ CONTACT LIST ------------")
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No contacts found.")
            else:
                for line in lines:
                    name, phone = line.strip().split(",")
                    print(f"Name: {name} | Phone: {phone}")
    except FileNotFoundError:
        print("No contact file found.")

def search():
    s = input("Enter the contact name to search: ")
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                if name.lower() == s.lower():
                    print(f"Found: {name} - {phone}")
                    found = True
                    break
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contact file found.")

def delete():
    d = input("Enter the contact name to delete: ")
    found = False
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        with open("contacts.txt", "w") as file:
            for line in lines:
                name, phone = line.strip().split(',')
                if name.lower() != d.lower():
                    file.write(line)
                else:
                    found = True
        if found:
            print(f"Contact '{d}' deleted successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contact file found.")

def clear_all():
    confirm = input("Delete all contacts? (yes/no): ")
    if confirm.lower() == "yes":
        open("contacts.txt", "w").close()
        print("All contacts deleted.")
    else:
        print("Cancelled.")

while True:
    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Clear All Contacts")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        search()
    elif choice == '4':
        delete()
    elif choice == '5':
        clear_all()
    elif choice == '6':
        print("Exiting Contact Book. Bye!")
        break
    else:
        print("Invalid choice. Please try again.")
