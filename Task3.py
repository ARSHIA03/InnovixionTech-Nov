tasks = {}  

def add_task():
    task = input("Enter the task: ")
    tasks[len(tasks) + 1] = task
    print("Task added successfully!")

def delete_task():
    print("Current Tasks:")
    display_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if task_number in tasks:
        del tasks[task_number]
        print("Task deleted successfully!")
    else:
        print("Task number not found.")

def display_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        for task_num, task in tasks.items():
            print(f"{task_num}: {task}")

def menu():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()
