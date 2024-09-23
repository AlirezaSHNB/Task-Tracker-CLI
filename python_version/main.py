import task

def main():
    print("Task Tracker CLI is running.")
    print("Type 'help' to see available commands or 'exit' to quit.")

    while True:
        command_input = input(">> ").strip().lower()
        
        # Split the command and arguments
        command_parts = command_input.split(" ")
        command = command_parts[0]
        args = command_parts[1:]

        if command == "exit":
            print("Exiting Task Tracker CLI.")
            break
        
        elif command == "help":
            print("""
Available commands:
    add <description>          - Add a new task
    list [status]              - List tasks (optional: filter by status: todo, in-progress, done)
    update <id> <description>  - Update task description
    delete <id>                - Delete a task
    mark <id> <status>         - Mark a task (in-progress or done)
    exit                       - Exit the application
    help                       - Show this help message
            """)
        
        elif command == "add" and args:
            description = " ".join(args)
            task_id = task.add_task(description)
            print(f"Task added successfully (ID: {task_id})")
        
        elif command == "list":
            status = args[0] if args else None
            tasks = task.list_tasks(status)
            if tasks:
                for t in tasks:
                    print(f"ID: {t['id']} | Description: {t['description']} | Status: {t['status']}")
            else:
                print("No tasks found.")
        
        elif command == "update" and len(args) >= 2:
            task_id = int(args[0])
            description = " ".join(args[1:])
            success = task.update_task(task_id, description)
            if success:
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Task {task_id} not found")
        
        elif command == "delete" and len(args) == 1:
            task_id = int(args[0])
            success = task.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully")
            else:
                print(f"Task {task_id} not found")
        
        elif command == "mark" and len(args) == 2:
            task_id = int(args[0])
            status = args[1]
            if status in ["in-progress", "done"]:
                success = task.mark_task(task_id, status)
                if success:
                    print(f"Task {task_id} marked as {status}")
                else:
                    print(f"Task {task_id} not found")
            else:
                print("Invalid status. Use 'in-progress' or 'done'.")
        
        else:
            print("Invalid command. Type 'help' for a list of available commands.")
        
if __name__ == "__main__":
    main()
