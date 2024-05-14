class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "✓" if task["completed"] else " "
                print(f"{index}. [{status}] {task['task']}")
    def mark_as_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")
def main():
    todo_list = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.mark_as_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
