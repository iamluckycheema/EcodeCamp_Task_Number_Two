# Import the os module to interact with the operating system
import os

# Define the file name to store tasks
TASKS_FILE = 'tasks.txt'

# Function to load tasks from the tasks file
def load_tasks():
    """
    Load tasks from the tasks file.

    Returns:
        list: A list of tasks.
    """
    try:
        # Check if the tasks file exists
        if os.path.exists(TASKS_FILE):
            # Open the tasks file in read mode
            with open(TASKS_FILE, 'r') as file:
                # Read the tasks from the file and split them into a list
                tasks = file.read().splitlines()
        else:
            # If the file does not exist, return an empty list
            tasks = []
        return tasks
    except Exception as e:
        # Handle any exceptions that occur while loading tasks
        print(f"\nERROR: Failed to load tasks - {str(e)}")
        return []

# Function to save tasks to the tasks file
def save_tasks(tasks):
    """
    Save tasks to the tasks file.

    Args:
        tasks (list): A list of tasks.
    """
    try:
        # Open the tasks file in write mode
        with open(TASKS_FILE, 'w') as file:
            # Join the tasks list into a string and write it to the file
            file.write('\n'.join(tasks))
    except Exception as e:
        # Handle any exceptions that occur while saving tasks
        print(f"\nERROR: Failed to save tasks - {str(e)}")

# Function to add a new task to the tasks list
def add_task(task):
    """
    Add a new task to the tasks list.

    Args:
        task (str): The task to add.
    """
    # Check if the task is not empty
    if not task:
        print("\nERROR: Task cannot be empty.")
        return
    # Load the existing tasks
    tasks = load_tasks()
    # Append the new task to the list
    tasks.append(task)
    # Save the updated tasks list
    save_tasks(tasks)
    # Print a success message
    print(f'\nSUCCESS: Task added: {task}')

# Function to remove a task from the tasks list
def remove_task(task_number):
    """
    Remove a task from the tasks list.

    Args:
        task_number (int): The task number to remove.
    """
    # Load the existing tasks
    tasks = load_tasks()
    # Check if there are tasks to remove
    if not tasks:
        print("\nERROR: No tasks to remove.")
        return
    # Check if the task number is valid
    if task_number < 1 or task_number > len(tasks):
        print("\nERROR: Invalid task number.")
        return
    # Remove the task from the list
    removed_task = tasks.pop(task_number - 1)
    # Save the updated tasks list
    save_tasks(tasks)
    # Print a success message
    print(f'\nSUCCESS: Task Removed: {removed_task}')

# Function to display the tasks list
def display_tasks():
    """
    Display the tasks list.
    """
    # Load the existing tasks
    tasks = load_tasks()
    # Check if there are tasks to display
    if tasks:
        # Print the tasks list
        print("\nYour to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        # Print a message if the tasks list is empty
        print("\nYour to-do list is empty.")

# Main function to run the to-do list application
def main():
    while True:
        # Print the main menu
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        # Get the user's choice
        choice = input('Choose an option: ')

        # Handle the user's choice
        if choice == '1':
            # Add a new task
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            # Remove a task
            display_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("\nERROR: Invalid task number.")
        elif choice == '3':
            # Display the tasks list
            display_tasks()
        elif choice == '4':
            # Exit the application
            print("\nSUCCESS: Exiting the To-Do List Application.")
            break
        else:
            # Handle invalid choices
            print("\nERROR: Invalid option. Please try again.")

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()