import os

class TodoList:
    def __init__(self, filename='todo_list.txt'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to a file."""
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
            return
        print("Your To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f'Task "{removed_task}" removed.')
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
