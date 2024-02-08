import os

# File path for storing tasks
TASKS_FILE = "tasks.txt"

def write_tasks_to_file(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved successfully.")
    except IOError:
        print("Error: Unable to write tasks to file.")

def read_tasks_from_file():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded successfully.")
    except IOError:
        print("Error: Unable to read tasks from file.")
    return tasks

def create_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    write_tasks_to_file(tasks)

def read_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task(tasks):
    read_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[index] = new_task
            write_tasks_to_file(tasks)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_task(tasks):
    read_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            write_tasks_to_file(tasks)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def main():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w"):
            pass

    tasks = read_tasks_from_file()

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_task(tasks)
            elif choice == 2:
                read_tasks(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    main()
