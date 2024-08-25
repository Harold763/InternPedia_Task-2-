import os

# File to store the tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def remove_task(tasks):
    """Remove a task from the list."""
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to remove: "))
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def to_dolist():
    """Main function to run the To-Do list application."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

to_dolist()
