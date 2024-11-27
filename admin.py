import os
import time

def print_main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================")
    print("      Admin Main Menu       ")
    print("============================")
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Edit Data")
    print("4. Search Data")
    print("5. View All Data")
    print("6. Exit")

def insert_data(data_store):
    print("\n--- Insert Data ---")
    entry = input("Enter new data: ")
    data_store.append(entry)
    print("Insertion successful!")
    time.sleep(1)

def delete_data(data_store):
    print("\n--- Delete Data ---")
    for idx, entry in enumerate(data_store):
        print(f"{idx + 1}. {entry}")
    choice = int(input("Select the number of the data to delete: ")) - 1
    if 0 <= choice < len(data_store):
        removed = data_store.pop(choice)
        print(f"Deleted: {removed}")
    else:
        print("Invalid choice!")
    time.sleep(1)

def edit_data(data_store):
    print("\n--- Edit Data ---")
    for idx, entry in enumerate(data_store):
        print(f"{idx + 1}. {entry}")
    choice = int(input("Select the number of the data to edit: ")) - 1
    if 0 <= choice < len(data_store):
        new_entry = input("Enter new data: ")
        data_store[choice] = new_entry
        print("Edit successful!")
    else:
        print("Invalid choice!")
    time.sleep(1)

def search_data(data_store):
    print("\n--- Search Data ---")
    query = input("Enter search term: ")
    results = [entry for entry in data_store if query.lower() in entry.lower()]
    if results:
        print("Search results:")
        for result in results:
            print(result)
    else:
        print("No matches found!")
    input("Press Enter to return to the menu.")

def view_all_data(data_store):
    print("\n--- All Stored Data ---")
    if data_store:
        for idx, entry in enumerate(data_store):
            print(f"{idx + 1}. {entry}")
    else:
        print("No data available.")
    input("Press Enter to return to the menu.")

def main():
    data_store = []

    while True:
        print_main_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            insert_data(data_store)
        elif choice == "2":
            delete_data(data_store)
        elif choice == "3":
            edit_data(data_store)
        elif choice == "4":
            search_data(data_store)
        elif choice == "5":
            view_all_data(data_store)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
