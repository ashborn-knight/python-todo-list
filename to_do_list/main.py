import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file (if it exists)
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print(" No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["done"] else "❌ Not done"
        print(f"{i}. {t['task']} [{status}]")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f" Task deleted: {removed['task']}")
    else:
        print(" Invalid task number!")

# Mark a task as completed
def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f" Task marked as done: {tasks[index - 1]['task']}")
    else:
        print(" Invalid task number!")

# Main program loop
def todo_app():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print(" Please enter a valid number!")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to mark as done: "))
                mark_done(index)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "5":
            print(" Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the app
todo_app()


