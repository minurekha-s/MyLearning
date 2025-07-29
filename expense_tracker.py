# Expense Tracker Project
# This script lets users add expenses, saves them to a CSV file, and visualizes spending by category.

import csv
import os
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (e.g., Food, Transport, Entertainment): ")
    description = input("Enter description: ")
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])
    print("Expense added!")

def show_summary():
    expenses = {}
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            amount, category, _ = row
            expenses[category] = expenses.get(category, 0) + float(amount)
    print("\nExpense Summary by Category:")
    for cat, amt in expenses.items():
        print(f"{cat}: ${amt:.2f}")

def plot_expenses():
    expenses = {}
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            amount, category, _ = row
            expenses[category] = expenses.get(category, 0) + float(amount)
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    plt.bar(categories, amounts)
    plt.xlabel("Category")
    plt.ylabel("Total Spent ($)")
    plt.title("Expenses by Category")
    plt.show()

def main():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            pass  # Create the file if it doesn't exist
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Plot Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            plot_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()