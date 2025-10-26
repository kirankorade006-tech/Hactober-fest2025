# todo_list.py
# Author: Your Name
# Date: October 2025
# Description: A simple command-line To-Do List App that saves tasks in a text file.
# Great for Hacktoberfest contributions! 🎃

import os

TODO_FILE = "tasks.txt"

def load_tasks():
    """Load existing tasks from the file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def save_tasks(tasks):
    """Save all tasks back to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks with numbers."""
    if not tasks:
        print("✅ No tasks yet! Add your first one below.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def main():
    tasks = load_tasks()
    while True:
        print("\n--- 📝 To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"✅ Added: {new_task}")
            else:
                print("⚠️ Task cannot be empty.")

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"🗑️ Removed: {removed}")
                else:
                    print("❌ Invalid number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "4":
            confirm = input("Are you sure you want to delete all tasks? (y/n): ").lower()
            if confirm == "y":
                tasks.clear()
                save_tasks(tasks)
                print("🧹 All tasks cleared!")

        elif choice == "5":
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("❌ Invalid option. Try again!")

if __name__ == "__main__":
    main()
