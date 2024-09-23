require_relative 'task'

def main
  puts "Task Tracker CLI is running."
  puts "Type 'help' to see available commands or 'exit' to quit."

  loop do
    print ">> "
    input = gets.strip
    command_parts = input.split(" ")
    command = command_parts[0]
    args = command_parts[1..-1]

    case command
    when 'exit'
      puts "Exiting Task Tracker CLI."
      break
    when 'help'
      puts """
Available commands:
    add <description>          - Add a new task
    list [status]              - List tasks (optional: filter by status: todo, in-progress, done)
    update <id> <description>  - Update task description
    delete <id>                - Delete a task
    mark <id> <status>         - Mark a task (in-progress or done)
    exit                       - Exit the application
    help                       - Show this help message
      """
    when 'add'
      if args.empty?
        puts "Error: No task description provided."
      else
        description = args.join(" ")
        task_id = add_task(description)
        puts "Task added successfully (ID: #{task_id})"
      end
    when 'list'
      status = args[0]
      tasks = list_tasks(status)
      if tasks.any?
        tasks.each do |t|
          puts "ID: #{t['id']} | Description: #{t['description']} | Status: #{t['status']}"
        end
      else
        puts "No tasks found."
      end
    when 'update'
      if args.size < 2
        puts "Error: Please provide task ID and new description."
      else
        task_id = args[0].to_i
        description = args[1..-1].join(" ")
        if update_task(task_id, description)
          puts "Task #{task_id} updated successfully"
        else
          puts "Task #{task_id} not found"
        end
      end
    when 'delete'
      if args.size != 1
        puts "Error: Please provide task ID."
      else
        task_id = args[0].to_i
        if delete_task(task_id)
          puts "Task #{task_id} deleted successfully"
        else
          puts "Task #{task_id} not found"
        end
      end
    when 'mark'
      if args.size != 2
        puts "Error: Please provide task ID and status (in-progress or done)."
      else
        task_id = args[0].to_i
        status = args[1]
        if %w[in-progress done].include?(status)
          if mark_task(task_id, status)
            puts "Task #{task_id} marked as #{status}"
          else
            puts "Task #{task_id} not found"
          end
        else
          puts "Error: Invalid status. Use 'in-progress' or 'done'."
        end
      end
    else
      puts "Invalid command. Type 'help' for a list of available commands."
    end
  end
end

main
