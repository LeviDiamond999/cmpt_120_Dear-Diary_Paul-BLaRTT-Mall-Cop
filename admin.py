from tinydb import TinyDB, Query

def display_menu():
    print("\nAdmin Main Menu")
    print("1. View all diary entries")
    print("2. Add a new diary entry")
    print("3. Edit an existing diary entry")
    print("4. Delete a diary entry")
    print("5. Exit")

def view_entries(db):
    entries = db.all()
    if entries:
        print("\nDiary Entries:")
        for entry in entries:
            print(f"ID: {entry.doc_id}, Date: {entry['date']}, Content: {entry['content']}")
    else:
        print("\nNo entries found.")

def add_entry(db):
    date = input("Enter the date (YYYY-MM-DD): ")
    content = input("Enter the diary content: ")
    db.insert({"date": date, "content": content})
    print("Entry added successfully!")

def edit_entry(db):
    try:
        entry_id = int(input("Enter the ID of the entry to edit: "))
        entry = db.get(doc_id=entry_id)
        if entry:
            print(f"Current Date: {entry['date']}, Current Content: {entry['content']}")
            date = input("Enter new date (leave blank to keep current): ") or entry['date']
            content = input("Enter new content (leave blank to keep current): ") or entry['content']
            db.update({"date": date, "content": content}, doc_ids=[entry_id])
            print("Entry updated successfully!")
        else:
            print("Entry not found.")
    except ValueError:
        print("Invalid ID format. Please enter a number.")

def delete_entry(db):
    try:
        entry_id = int(input("Enter the ID of the entry to delete: "))
        if db.remove(doc_ids=[entry_id]):
            print("Entry deleted successfully!")
        else:
            print("Entry not found.")
    except ValueError:
        print("Invalid ID format. Please enter a number.")

def main():
    db = TinyDB('diary.json')

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_entries(db)
        elif choice == "2":
            add_entry(db)
        elif choice == "3":
            edit_entry(db)
        elif choice == "4":
            delete_entry(db)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
