from tinydb import TinyDB, Query
import datetime
import ProjectLogin


# Initialize TinyDB dairy entries
db = TinyDB('diary.json')
diary_table = db.table('diaries')
Diary = Query()

today=datetime.date.today()


# Functions for diary management
def add_diary_entry(username):
    """Add a new diary entry."""
    print("\n=== Add Diary Entry ===")
    '''
    time = input("Enter the date (MM-DD-YYYY): ")
    '''
    now=datetime.datetime.now()
    current_time=now.strftime("%H:%M")
    print(f"Current date and time: {today} {current_time}")
    title = input("Enter a title: ")
    entry = input("Journal Entry: ")
    
    
    diary_table.insert({
        "username": username,
        "time": current_time,
        "title": title,
       "entry": entry,
        
    })
    print("Diary entry added successfully!")

def view_diary_entries(username):
    """View all diary entries for the current user."""
    print("\n=== View Diary Entries ===")
    entries = diary_table.search(Diary.username == username)
    if not entries:
        print("No diary entries found.")
        return
    for i, entry in enumerate(entries, start=1):
        print(f"\nEntry {i}:")
        
        print(f"Time: {entry['time']}")
        
        print(f"Title: {entry['title']}")
        print(f"Entry: {entry['entry']}")
        

def edit_diary_entry(username):
    """Edit a diary entry."""
    print("\n=== Edit Diary Entry ===")
    view_diary_entries(username)
    description = input("\nEnter the description of the entry to edit: ")
    entry = diary_table.get((Diary.username == username) & (Diary.description == description))
    if not entry:
        print("No entry found with the given description.")
        return
    print("Leave fields blank to keep current values.")
    '''
    new_time = input(f"New time (current: {entry['time']}): ") or entry['time']
    '''
    new_titlw = input(f"New title (current: {entry['title']}): ") or entry['title']
    
    diary_table.update({
        "time": new_time,
        "title": new_title,
        
    }, (Diary.username == username) & (Diary.title == title))
    print("Diary entry updated successfully!")

def delete_diary_entry(username):
    """Delete a diary entry."""
    print("\n=== Delete Diary Entry ===")
    view_diary_entries(username)
    title = input("\nEnter the title of the entry to delete: ")
    if diary_table.remove((Diary.username == username) & (Diary.title == title)):
        print("Diary entry deleted successfully!")
    else:
        print("No entry found with the given title.")

def search_diary_entries(username):
    """Search diary entries."""
    print("\n=== Search Diary Entries ===")
    criteria = input("Search by (time/title): ").strip().lower()
    value = input(f"Enter the {criteria}: ").strip()
    entries = diary_table.search((Diary.username == username) & (Diary[criteria] == value))
    if not entries:
        print("No diary entries found.")
        return
    for i, entry in enumerate(entries, start=1):
        print(f"\nEntry {i}:")
        print(f"Time: {entry['time']}")
        print(f"Title: {entry['title']}")

# Main Menu
def main_menu(username):
    """Main menu for the diary system."""
    while True:
        print("\n=== Main Menu ===")
        print("1. Add Diary Entry")
        print("2. View Diary Entries")
        print("3. Edit Diary Entry")
        print("4. Delete Diary Entry")
        print("5. Search Diary Entries")
        print("6. Logout")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            add_diary_entry(username)
        elif choice == '2':
            view_diary_entries(username)
        elif choice == '3':
            edit_diary_entry(username)
        elif choice == '4':
            delete_diary_entry(username)
        elif choice == '5':
            search_diary_entries(username)
        elif choice == '6':
            print("Logging out. Goodbye!")
            ProjectLogin.login()
        else:
            print("Invalid choice. Please try again.")
            
def main(username):
    
    main_menu(username)
