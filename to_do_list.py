import os

# Function to display the menu options
def display_menu():
    print("\nCommand Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

# Function to view the current To-Do List
def view_todo_list():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nTo-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List is empty.")

# Function to add a task to the To-Do List
def add_task():
    task = input("\nEnter the task to add: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

# Function to mark a task as done
def mark_task_as_done():
    view_todo_list()
    try:
        task_number = int(input("\nEnter the number of the task to mark as done: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].strip() + " - Done\n"
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to remove a task from the To-Do List
def remove_task():
    view_todo_list()
    try:
        task_number = int(input("\nEnter the number of the task to remove: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_as_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
