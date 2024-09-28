tasks = []
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
def view_task(tasks):
    if len(tasks) == 0:  
        print('You do not have any tasks.')
        view_add = input('Do you want to add a task? (Yes or No): ')   
        if view_add.lower() == 'yes':
             add_task(tasks)
        elif view_add.lower() == 'no':
            return
        else:
            print("Please enter 'Yes' or 'No'.") 
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    
def add_task(tasks):
   while True:
        new_task = input('ENTER NEW TASK:')
        if new_task not in tasks:
            tasks.append(new_task)
            print(f'{new_task} has been added to your list')
        else:
            print('Task is already there')


        add_more = input('Do you want to add another task? (Yes or No): ')
        if add_more.lower() == 'no':
            break
        elif add_more.lower() != 'yes':
            print("Please enter 'Yes' or 'No'.")
def remove_task(tasks):
  if len(tasks) > 0:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        remove = int(input('Please put the number of the task you want to remove: '))
        if 0 < remove <= len(tasks):
            removed = tasks.pop(remove-1)
            print(f'The task "{removed}" has been removed from the list')
        else:
            print("Invalid task number.")
            remove_task(tasks)
  else:
        print('You do not have a task to remove')

while True:
    show_menu()
    user_choice = int(input())
    if user_choice == 1:
       view_task(tasks)
    elif user_choice == 2:
       add_task(tasks)
    elif user_choice ==3:
       remove_task(tasks)
    elif user_choice ==4:
        break
    else:
        print('Please input a valid number between 1-4')



    