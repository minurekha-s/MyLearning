# Task Manager Project
# This script lets users add tasks with due dates, view tasks, mark them as complete, and get reminders for tasks due today.

import csv
import os
from datetime import datetime

CSV_FILE = "tasks.csv"

def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, due_date, "Incomplete"])
    print("Task added!")

def show_tasks():
    print("\nAll Tasks:")
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for idx, row in enumerate(reader, 1):
            desc, due, status = row
            print(f"{idx}. {desc} | Due: {due} | Status: {status}")

def mark_complete():
    show_tasks()
    task_num = int(input("Enter the task number to mark as complete: "))
    tasks = []
    with open(CSV_FILE, "r") as file:
        tasks = list(csv.reader(file))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1][2] = "Complete"
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    task_num = int(input("Enter the task number to delete: "))
    tasks = []
    with open(CSV_FILE, "r") as file:
        tasks = list(csv.reader(file))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def remind_today():
    today = datetime.today().strftime("%Y-%m-%d")
    print("\nTasks Due Today:")
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            desc, due, status = row
            if due == today and status == "Incomplete":
                print(f"- {desc}")
                found = True
        if not found:
            print("No tasks due today!")

def main():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            pass  # Create the file if it doesn't exist
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Remind Tasks Due Today")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            remind_today()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()