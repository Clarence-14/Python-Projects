# A program to manage a grocery list, allowing users to add, remove, and search for items.

def add_item(grocery_list, item):
    grocery_list.append(item)
    print(f"Added '{item}' to the grocery list.")

def remove_item(grocery_list, item):
    try:
        grocery_list.remove(item)
        print(f"Removed '{item}' from the grocery list.")
    except ValueError:
        print(f"Item '{item}' not found in the grocery list.")

def search_item(grocery_list, item):
    if item in grocery_list:
        print(f"Item '{item}' is in the grocery list.")
    else:
        print(f"Item '{item}' is not in the grocery list.")

if __name__ == "__main__":
    grocery_list = []
    print("Grocery List Manager")
    print("Options: add, remove, search, view, exit")
    
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == 'add':
            item = input("Enter item to add: ").strip()
            add_item(grocery_list, item)
        elif command == 'remove':
            item = input("Enter item to remove: ").strip()
            remove_item(grocery_list, item)
        elif command == 'search':
            item = input("Enter item to search: ").strip()
            search_item(grocery_list, item)
        elif command == 'view':
            print("Current Grocery List:", grocery_list)
        elif command == 'exit':
            print("Exiting Grocery List Manager.")
            break
        else:
            print("Invalid command. Please try again.")

            