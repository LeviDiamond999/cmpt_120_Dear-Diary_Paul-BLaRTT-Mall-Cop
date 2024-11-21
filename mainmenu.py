from tinydb import TinyDB, Query
from datetime import datetime

# Initialize TinyDB
db = TinyDB('diary.json')
diary_table = db.table('diaries')
Diary = Query()

# Functions for diary management
def add_diary_entry(username):
    """Add a new diary entry."""
    print("\n=== Add Diary Entry ===")
    time = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    place = input("Enter the place: ")
    duration = input("Enter the duration: ")
    description = input("Enter the description: ")
    priority = input("Enter the priority (Low/Medium/High): ")
    
    diary_table.insert({
        "username": username,
        "time": time,
        "place": place,
        "duration": duration,
        "description": description,
        "priority": priority
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
        print(f"Place: {entry['place']}")
        print(f"Duration: {entry['duration']}")
        print(f"Description: {entry['description']}")
        print(f"Priority: {entry['priority']}")

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
    new_time = input(f"New time (current: {entry['time']}): ") or entry['time']
    new_place = input(f"New place (current: {entry['place']}): ") or entry['place']
    new_duration = input(f"New duration (current: {entry['duration']}): ") or entry['duration']
    new_description = input(f"New description (current: {entry['description']}): ") or entry['description']
    new_priority = input(f"New priority (current: {entry['priority']}): ") or entry['priority']
    
    diary_table.update({
        "time": new_time,
        "place": new_place,
        "duration": new_duration,
        "description": new_description,
        "priority": new_priority
    }, (Diary.username == username) & (Diary.description == description))
    print("Diary entry updated successfully!")

def delete_diary_entry(username):
    """Delete a diary entry."""
    print("\n=== Delete Diary Entry ===")
    view_diary_entries(username)
    description = input("\nEnter the description of the entry to delete: ")
    if diary_table.remove((Diary.username == username) & (Diary.description == description)):
        print("Diary entry deleted successfully!")
    else:
        print("No entry found with the given description.")

def search_diary_entries(username):
    """Search diary entries."""
    print("\n=== Search Diary Entries ===")
    criteria = input("Search by (time/place/duration): ").strip().lower()
    value = input(f"Enter the {criteria}: ").strip()
    entries = diary_table.search((Diary.username == username) & (Diary[criteria] == value))
    if not entries:
        print("No diary entries found.")
        return
    for i, entry in enumerate(entries, start=1):
        print(f"\nEntry {i}:")
        print(f"Time: {entry['time']}")
        print(f"Place: {entry['place']}")
        print(f"Duration: {entry['duration']}")
        print(f"Description: {entry['description']}")
        print(f"Priority: {entry['priority']}")

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
            break
        else:
            print("Invalid choice. Please try again.")

# Example Usage
if __name__ == "__main__":
    username = "test_user"  # Replace with actual login logic
    main_menu(username)
