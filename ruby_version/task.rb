require 'json'
require 'time'

TASKS_FILE = 'tasks.json'

# Ensure the file exists, if not, create an empty one
def ensure_file_exists
  unless File.exist?(TASKS_FILE)
    File.open(TASKS_FILE, 'w') { |file| file.write('[]') }
  end
end

def load_tasks
  ensure_file_exists
  file_content = File.read(TASKS_FILE)
  begin
    return JSON.parse(file_content)
  rescue JSON::ParserError
    return []
  end
end

def save_tasks(tasks)
  File.open(TASKS_FILE, 'w') do |file|
    file.write(JSON.pretty_generate(tasks))
  end
end

def add_task(description)
  tasks = load_tasks
  task_id = tasks.size + 1
  now = Time.now.iso8601
  task = {
    'id' => task_id,
    'description' => description,
    'status' => "todo",
    'createdAt' => now,
    'updatedAt' => now
  }
  tasks << task
  save_tasks(tasks)
  task_id
end

def list_tasks(status=nil)
  tasks = load_tasks
  if status
    tasks.select do |task|
      task['status'] == status
    end
  else
    tasks
  end
end

def update_task(task_id, new_description)
  tasks = load_tasks
  task = tasks.find do |task|
    task['id'] == task_id
  end
  return false unless task
  task['description'] = new_description
  task['updatedAt'] = Time.now.iso8601
  save_tasks(tasks)
  true
end

def delete_task(task_id)
  tasks = load_tasks
  original_size = tasks.size
  tasks.reject! do |task|
    task['id'] == task_id
  end
  if original_size == tasks.size
    false
  else
    save_tasks(tasks)
    true
  end
end

def mark_task(task_id, status)
  tasks = load_tasks
  task = tasks.find do |task|
    task['id'] == task_id
  end
  return false unless task
  task['status'] = status

  task['updatedAt'] = Time.now.iso8601
  save_tasks(tasks)
  true
end