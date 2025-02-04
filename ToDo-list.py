import json
import os

# Storing
TASKS_FILE = "tasks.json"

# Loading
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Saving
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Displaying
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{index}. [{status}] {task['task']}")

# Addition
def add_task(tasks):
    task_desc = input("Enter the task: ")
    tasks.append({"task": task_desc, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Updation
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_index]["task"] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Deletion
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Tracking
def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            print("Exiting... Thank You!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
