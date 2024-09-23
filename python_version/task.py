import json
import os
from datetime import datetime

# Define the path to the JSON file
TASKS_FILE = "tasks.json"

# Ensure the file exists, if not, create an empty one
def ensure_file_exists():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as file:
            json.dump([], file)

# Load tasks from the JSON file
def load_tasks():
    ensure_file_exists()
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)  # Try to load the JSON data
        except json.JSONDecodeError:
            return []  # If the file is empty or invalid, return an empty list

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    now = datetime.now().isoformat()
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)
    save_tasks(tasks)
    return task_id

# List tasks based on status
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    return tasks

# Update a task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            return True
    return False

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(new_tasks):
        return False  # No task was deleted
    save_tasks(new_tasks)
    return True

# Mark a task as in-progress or done
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            return True
    return False
