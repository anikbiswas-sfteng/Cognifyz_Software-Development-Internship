class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. Title: {task.title}, Description: {task.description}")

    def update_task(self, index, title, description):
        if index < 1 or index > len(self.tasks):
            print("Invalid task index.")
            return
        self.tasks[index - 1].title = title
        self.tasks[index - 1].description = description
        print("Task updated successfully.")

    def delete_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task index.")
            return
        del self.tasks[index - 1]
        print("Task deleted successfully.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Create a new task")
        print("2. Read tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task Title: ")
            description = input("Enter task Description: ")
            task_manager.create_task(title, description)
        elif choice == '2':
            task_manager.read_tasks()
        elif choice == '3':
            index = int(input("Enter index of the task to Update: "))
            title = input("Enter new Title: ")
            description = input("Enter new Description: ")
            task_manager.update_task(index, title, description)
        elif choice == '4':
            index = int(input("Enter index of the task to Delete: "))
            task_manager.delete_task(index)
        elif choice == '5':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
