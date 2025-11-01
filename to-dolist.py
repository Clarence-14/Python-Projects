# A program with functions to manage a to-do list (add, remove, view tasks).

todo_list = [] 
def add_task(task):
    todo_list.append(task)
    print(f'Task "{task}" added to the list.')

def remove_task(task):
    try:
        todo_list.remove(task)
        print(f'Task "{task}" removed from the list.')
    except ValueError:
        print(f'Task "{task}" not found in the list.') 

def view_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

if __name__ == "__main__":      
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid input, please try again.")