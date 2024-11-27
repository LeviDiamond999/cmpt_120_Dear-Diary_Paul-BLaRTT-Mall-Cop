from tinydb import TinyDB, Query

def login_page():
    db = TinyDB('users.json')
    User = Query()

    print("Welcome to the System!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = db.search((User.username == username) & (User.password == password))

    if user:
        if user[0]['role'] == 'admin':
            print("Admin login successful! Redirecting to Admin Page...")
            admin_page()
        else:
            print("Login successful! Redirecting to Main Menu...")
            main_menu()
    else:
        print("Invalid credentials. Please try again.")
        login_page()

def admin_page():
    print("\n*** Admin Page ***")
    print("1. View all users")
    print("2. Add a new user")
    print("3. Delete a user")
    print("4. Logout")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        view_users()
    elif choice == '2':
        add_user()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        print("Logging out...")
        login_page()
    else:
        print("Invalid choice. Try again.")
        admin_page()

def view_users():
    db = TinyDB('users.json')
    users = db.all()
    print("\nRegistered Users:")
    for user in users:
        print(f"Username: {user['username']}, Role: {user['role']}")
    admin_page()

def add_user():
    db = TinyDB('users.json')
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    role = input("Enter role (admin/user): ")

    db.insert({"username": username, "password": password, "role": role})
    print("User added successfully!")
    admin_page()

def delete_user():
    db = TinyDB('users.json')
    User = Query()
    username = input("Enter the username to delete: ")

    if db.remove(User.username == username):
        print("User deleted successfully!")
    else:
        print("User not found.")
    admin_page()

def main_menu():
    db = TinyDB('diary.json')
    Diary = Query()

    while True:
        print("\n*** Main Menu ***")
        print("1. View all diary entries")
        print("2. Add a new diary entry")
        print("3. Edit a diary entry")
        print("4. Delete a diary entry")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            entries = db.all()
            print("\nDiary Entries:")
            for entry in entries:
                print(f"ID: {entry.doc_id}, Title: {entry['title']}, Content: {entry['content']}")
        elif choice == '2':
            title = input("Enter entry title: ")
            content = input("Enter entry content: ")
            db.insert({"title": title, "content": content})
            print("Diary entry added successfully!")
        elif choice == '3':
            entry_id = int(input("Enter the ID of the entry to edit: "))
            title = input("Enter new title: ")
            content = input("Enter new content: ")
            db.update({"title": title, "content": content}, doc_ids=[entry_id])
            print("Diary entry updated successfully!")
        elif choice == '4':
            entry_id = int(input("Enter the ID of the entry to delete: "))
            db.remove(doc_ids=[entry_id])
            print("Diary entry deleted successfully!")
        elif choice == '5':
            print("Logging out...")
            login_page()
        else:
            print("Invalid choice. Please try again.")

# Run the program
login_page()
