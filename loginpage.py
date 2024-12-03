from tinydb import TinyDB, Query
from getpass import getpass
import mainmenu
import adminmenu

# Initialize database
db = TinyDB('database.json')
users_table = db.table('users')  # Table for user credentials
User = Query()


# Utility functions
def initialize_admin():
    """Ensure there is an admin account."""
    if not users_table.search(User.username == 'admin'):
        users_table.insert({'username': 'admin', 'password': 'admin123', 'is_admin': True})
        print("Admin account created with username: 'admin' and password: 'admin123'")

def add_user(username, password, is_admin=False):
    """Add a new user."""
    if users_table.search(User.username == username):
        print("Error: User already exists!")
    else:
        users_table.insert({'username': username, 'password': password, 'is_admin': is_admin})
        print(f"User '{username}' added successfully.")

def validate_user(username, password):
    """Validate user credentials."""
    user = users_table.get(User.username == username)
    if user and user['password'] == password:
        return user['is_admin']
    return None

# Main login function
def login():
    print("\nWelcome to the Diary Login Page")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")  # Secure password input

    is_admin = validate_user(username, password)
    if is_admin is not None:
        if is_admin:
            print("Login successful! Welcome, Admin.")
            adminmenu.main()
        else:
            print(f"Login successful! Welcome, {username}.")
            mainmenu.main(username)
    else:
        print("Invalid username or password. Please try again.")

def admin_menu():
    """Admin-specific menu."""
    while True:
        print("\nAdmin Menu")
        print("1. Add a new user")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_username = input("Enter new username: ")
            new_password = getpass("Enter new password: ")
            is_admin = input("Is this an admin account? (yes/no): ").lower() == 'yes'
            add_user(new_username, new_password, is_admin)
        elif choice == '2':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(username):
    """Normal user-specific menu."""
    print(f"\nWelcome to your diary, {username}!")
    # Extend with diary management functions like add/view/edit/delete diary entries

# Initialize and run
if __name__ == "__main__":
    initialize_admin()  # Ensure an admin account exists
    while True:
        login()
