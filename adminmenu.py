from tinydb import TinyDB, Query
import datetime
import loginpage


# Initialize TinyDB dairy entries
db = TinyDB('diary.json')
diary_table = db.table('diaries')
Diary = Query()
# Initialize database
database = TinyDB('database.json')
users_table = database.table('users')  # Table for user credentials
User = Query()
today=datetime.date.today()

def add_user():
    name = input("Enter the username: ")
    passwrd = input("Enter the password: ")

    if not users_table.search(User.username == name):
        users_table.insert({'username': name, 'password': passwrd, 'is_admin': False})
        print(f"Account created with username: {name} and password: {passwrd}")
    

def view_diary_entries():
    """View all diary entries for the current user."""
    print("\n=== View Diary Entries ===")
    entries = diary_table
    if not entries:
        print("No diary entries found.")
        return
    for i, entry in enumerate(entries, start=1):
        print(f"\nEntry {i}:")

        print(f"User: {entry['username']}")
        print(f"Time: {entry['time']}")
        
        print(f"Title: {entry['title']}")
        print(f"Entry: {entry['entry']}")
        

def delete_diary_entry():
    """Delete a diary entry."""
    print("\n=== Delete Diary Entry ===")
    view_diary_entries()
    title = input("\nEnter the title of the entry to delete: ")
    if diary_table.remove(Diary.title == title):
        print("Diary entry deleted successfully!")
    else:
        print("No entry found with the given title.")

def search_diary_entries():
    """Search diary entries."""
    print("\n=== Search Diary Entries ===")
    title = input("Search by title: ")
    entries = diary_table.search(Diary.title == title)
    if not entries:
        print("No diary entries found.")
        return
    for i, entry in enumerate(entries, start=1):
        print(f"\nEntry {i}:")
        print(f"Time: {entry['time']}")
        print(f"Title: {entry['title']}")

# Main Menu
def main_menu():
    """Main menu for the diary system."""
    while True:
        print("\n=== Main Menu ===")
        print("1. View Diary Entries")
        print("2. Delete Diary Entry")
        print("3. Search Diary Entries")
        print("4. Add User")
        print("5. Logout")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            view_diary_entries()
        elif choice == '2':
            delete_diary_entry()
        elif choice == '3':
            search_diary_entries()
        elif choice == '4':
            add_user()
        elif choice == '5':
            print("Logging out. Goodbye!")
            loginpage.login()
        else:
            print("Invalid choice. Please try again.")
            
def main():
    
    main_menu()
