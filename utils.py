import os
import json

TASKS_FILE = 'tasks.json'

# Load tasks from storage
def load_tasks():
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
    except FileNotFoundError:
        return []

# Save Tasks to Storage
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Get all lists
def get_lists():
    tasks = load_tasks()
    lists = set(task['list'] for task in tasks)
    return lists

# Add new task
def add_task(task, list_name):
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False, 'list': list_name})
    save_tasks(tasks)

# Remove a task
def remove_task(task_id, list_name):
    tasks = load_tasks()
    tasks = [task for task in tasks if not (task['list'] == list_name and tasks.index(task) == task_id - 1)]
    save_tasks(tasks)

# Toggle a task
def toggle_task_completion(task_id, list_name):
    tasks = load_tasks()
    for task in tasks:
        if task['list'] == list_name and tasks.index(task) == task_id - 1:
            task['completed'] = not task['completed']
            break
    save_tasks(tasks)
