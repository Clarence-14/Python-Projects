# A program to manage a contact book, allowing users to add, update, delete, and search contacts stored in a dictionary.

def add_contact(contact_book, name, phone):
    contact_book[name] = phone
    return contact_book

def update_contact(contact_book, name, phone):
    if name in contact_book:
        contact_book[name] = phone
    return contact_book

def delete_contact(contact_book, name):
    if name in contact_book:
        del contact_book[name]
    return contact_book

def search_contact(contact_book, name):
    return contact_book.get(name, "Contact not found")

if __name__ == "__main__":
    contact_book = {}
    
    while True:
        action = input("Choose an action: add, update, delete, search, or exit: ").strip().lower()
        
        if action == "add":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contact_book = add_contact(contact_book, name, phone)
            print(f"Contact {name} added.")
        
        elif action == "update":
            name = input("Enter contact name to update: ")
            phone = input("Enter new contact phone number: ")
            contact_book = update_contact(contact_book, name, phone)
            print(f"Contact {name} updated.")
        
        elif action == "delete":
            name = input("Enter contact name to delete: ")
            contact_book = delete_contact(contact_book, name)
            print(f"Contact {name} deleted.")
        
        elif action == "search":
            name = input("Enter contact name to search: ")
            result = search_contact(contact_book, name)
            print(f"Search Result: {result}")
        
        elif action == "exit":
            print("Exiting contact manager.")
            break
        
        else:
            print("Invalid action. Please try again.")