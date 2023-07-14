import datetime

# In-memory dict to store to-do items  
todos = {}

def add_todo(text):
  id = len(todos) + 1
  todos[id] = {
    'id': id,
    'text': text, 
    'done': False,
    'created_at': datetime.datetime.now()
  }

def show_todos():
  print('My To-Dos:')
  for todo_id in todos:
    todo = todos[todo_id]
    print(f"{todo['id']}. {todo['text']} ({todo['created_at']}) - {'Done' if todo['done'] else 'Not Done Yet'}")

def mark_done(todo_id):
  if todo_id not in todos:
    print(f"Error: todo with id {todo_id} does not exist")
  else:
    todos[todo_id]['done'] = True

# Simple CLI
while True:
  print()
  print('Menu:')
  print('1. Add New To-Do')
  print('2. Show All To-Dos')
  print('3. Mark To-Do as Done')
  print('4. Exit')
  
  option = input('Enter option: ')
  if option == '1':
    text = input('Enter to-do text: ')
    add_todo(text)
  elif option == '2':
    show_todos()
  elif option == '3':
    todo_id = int(input('Enter todo id to mark as done: '))  
    mark_done(todo_id)
  elif option == '4':
    break
  else:
    print('Invalid option selected')

print('Bye!') 