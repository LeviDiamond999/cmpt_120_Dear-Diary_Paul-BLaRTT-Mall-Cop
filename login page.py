from tinydb import TinyDB, Query
from hashlib import sha256

# Initialize database
db = TinyDB('users.json')
users_table = db.table('users')
User = Query()

# Utility functions
def hash_password(password):
    """Hash a password using SHA-256."""
    return sha256(password.encode()).hexdigest()

def add_user(username, password, is_admin=False):
    """Add a new user to the database."""
    if users_table.search(User.username == username):
        print("Username already exists.")
        return False
    hashed_password = hash_password(password)
    users_table.insert({"username": username, "password": hashed_password, "is_admin": is_admin})
    print("User added successfully!")
    return True

def validate_user(username, password):
    """Validate user credentials."""
    hashed_password = hash_password(password)
    user = users_table.get(User.username == username)
    if user and user['password'] == hashed_password:
        return user['is_admin']
    return None

# Login function
def login():
    """Login page for users."""
    print("=== Login Page ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    is_admin = validate_user(username, password)
    if is_admin is not None:
        if is_admin:
            print(f"Welcome Admin {username}!")
        else:
            print(f"Welcome {username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Sign-up function
def signup():
    """Sign-up page for new users."""
    print("=== Sign-Up Page ===")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match!")
        return False
    is_admin = input("Is this an admin account? (yes/no): ").strip().lower() == "yes"
    return add_user(username, password, is_admin)

# Example usage
if __name__ == "__main__":
    print("Welcome to the Diary Management System!")
    while True:
        print("\nOptions:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")
        if choice == '1':
            login()
        elif choice == '2':
            signup()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
