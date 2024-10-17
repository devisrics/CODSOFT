tasks=[]
print("Welcome to your To-Do List!")

def create_tasks():
    task=str(input("Enter the tasks you want to add:"))
    tasks.append(task)
    print(f"Task {task} added successfully \n")

def track_tasks():
    print("your tasks are:")
    if not tasks:
        print("No Tasks Available")
    else:
        for index,track_task in enumerate(tasks):
            print(f"{index+1}.{track_task}")
    print()

def update_tasks():
    if not tasks:
        print("No tasks to update")
    else:
        try:
            upd_task=int(input("Enter the number of the task to update:"))
            if 1<=upd_task <=len(tasks):
               new_task=str(input("Enter the new tasks"))
               tasks[upd_task-1]=new_task
               print(f"Your task has been updated to {new_task} successfully\n")
            else:
                print("Invalid Task number.")
        except ValueError:
            print("Invalid Input")

def to_do_lists():
    while True:
      print("Please select one of the options below:")
      print("1. Create Task")
      print("2. Track Tasks")
      print("3. Update Task")
      print("4. Exit")

      choice=int(input("Enter your Choice"))

      if choice==1:
          create_tasks()
      elif choice==2:
          track_tasks()
      elif choice==3:
          update_tasks()
      elif choice==4:
          break
      else:
          print("Invalid Choice")
     
to_do_lists()     
