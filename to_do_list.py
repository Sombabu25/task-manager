
# empty list to add , view  and delete tasks
tasks=[]


# to add tasks to the list
def add_task():
    task=input("enter task to add:")
    tasks.append(task)
    print("task added successfully\n")


# to view tasks in the list
def view_task():
    print("-----------------available tasks-----------------------")
    for x in tasks:
        print(x)
    print("----------------------------------------")

# to delete task from the list
def delete_task():
    task=input("enter task to delete:")

    # to handle invalid tasks that doesn't exist
    if task not in tasks:
        print("Sorry this task doesn't exits\n")

    else:  
        tasks.remove(task)
        print(f"{task}  removed from the list\n")

# to display number of remaining tasks
def pending_tasks():
    print("Remaining tasks are:",len(tasks))    


while True:
    choice=input("choose an option:\n1.adding task\n2.view the task\n3.remove task\n4. Number of Remaining Tasks\n")
    if choice == "1":
        add_task()
    elif choice =="2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        pending_tasks()

    else:
        print("OOPS Invalid Choice\n")
        continue
