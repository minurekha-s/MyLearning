# Simple To-Do List App

# This script demonstrates lists, loops, user input, and if/else statements in Python.

todo_list = []

while True:
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        if not todo_list:
            print("No tasks in your list.")
        else:
            print("Your tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
    elif choice == '2':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == '3':
        if not todo_list:
            print("No tasks to remove.")
        else:
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
            try:
                remove_idx = int(input("Enter the number of the task to remove: "))
                if 1 <= remove_idx <= len(todo_list):
                    removed = todo_list.pop(remove_idx - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number from 1 to 4.")
