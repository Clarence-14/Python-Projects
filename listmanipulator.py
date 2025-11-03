# A program that lets the user create a list by adding items, then performs operations like reversing, sorting, and accessing elements.

user_list = []
def add_item(item):
    user_list.append(item)
    print(f'Item "{item}" added to the list.')

def reverse_list():
    user_list.reverse()
    print("List reversed.")

def sort_list():
    user_list.sort()
    print("List sorted.")

def access_element(index):
    try:
        element = user_list[index]
        print(f'Element at index {index}: "{element}"')
    except IndexError:
        print(f'Index {index} is out of range.')
        
def view_list():
    if not user_list:
        print("The list is empty.")
    else:
        print("Current List:")
        for idx, item in enumerate(user_list):
            print(f"{idx}: {item}")

if __name__ == "__main__":      
    while True:
        print("\nList Manipulator")
        print("1. Add Item")
        print("2. Reverse List")
        print("3. Sort List")
        print("4. Access Element")
        print("5. View List")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            reverse_list()
        elif choice == '3':
            sort_list()
        elif choice == '4':
            index = int(input("Enter the index of the element to access: "))
            access_element(index)
        elif choice == '5':
            view_list()
        elif choice == '6':
            print("Exiting List Manipulator.")
            break
        else:
            print("Invalid input, please try again.")

