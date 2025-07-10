# Simple Calendar with Tasks and Notes
# This script lets you add tasks and notes to specific dates.
# Demonstrates dictionaries, lists, user input, and basic date handling.

calendar = {}

def add_task(date, task):
    if date not in calendar:
        calendar[date] = {'tasks': [], 'notes': []}
    calendar[date]['tasks'].append(task)
    print(f"Task added to {date}.")

def add_note(date, note):
    if date not in calendar:
        calendar[date] = {'tasks': [], 'notes': []}
    calendar[date]['notes'].append(note)
    print(f"Note added to {date}.")

def view_day(date):
    if date in calendar:
        print(f"\nTasks for {date}:")
        for idx, task in enumerate(calendar[date]['tasks'], 1):
            print(f"  Task {idx}: {task}")
        print(f"Notes for {date}:")
        for idx, note in enumerate(calendar[date]['notes'], 1):
            print(f"  Note {idx}: {note}")
    else:
        print(f"No tasks or notes for {date}.")

def main():
    print("Simple Calendar with Tasks and Notes")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Add Note")
        print("3. View Day")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            task = input("Enter task: ")
            add_task(date, task)
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            note = input("Enter note: ")
            add_note(date, note)
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            view_day(date)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
