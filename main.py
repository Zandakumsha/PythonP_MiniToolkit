to_do_list = []

def add_task(task=None, *args, **kwargs):
    """Add a task from an argument or user input."""
    if task is None:
        task = input("Enter a task: ").strip()
    if not task:
        print("No task entered. Please try again.")
        return
    status = kwargs.get('status', 'pending')
    to_do_list.append({'Task': task, 'status': status})
    print("New Task added Successfully.")


def view_task(*args, **kwargs):
    """View tasks. Supports optional kwargs for future customization."""
    print("Your Todo List:")
    if len(to_do_list) == 0:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}: {task['Task']} - {task['status']}")
    print("\n")


def remove_task(task_number=None, *args, **kwargs):
    """Remove a task by number, or ask the user if not provided."""
    if len(to_do_list) == 0:
        print("List IS Empty.")
        return
    if task_number is None:
        try:
            task_number = int(input("Enter the task number that you want to remove: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        task_number = int(task_number) - 1

    if 0 <= task_number < len(to_do_list):
        removed_task = to_do_list.pop(task_number)
        print(f"Task removed successfully: {removed_task['Task']}.")
    else:
        print("Invalid task number.")


def mark_done(task_number=None, *args, **kwargs):
    """Mark a task done by number, or ask the user if not provided."""
    if len(to_do_list) == 0:
        print("No tasks in the list.")
        return
    if task_number is None:
        try:
            task_number = int(input("Enter the number of the task to mark as done: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        task_number = int(task_number) - 1

    if 0 <= task_number < len(to_do_list):
        done_task = to_do_list[task_number]
        done_task['status'] = kwargs.get('status', 'done')
        print(f"Task '{done_task['Task']}' marked as done.")
    else:
        print("Invalid task number.")


def menu():
    while True:
       print("Welcome to the menu!")
       print("1. Add a New Task")
       print("2. View Tasks")
       print("3. Remove a Task")
       print("4. Mark Task as Done")
       print("5. Exit")

       choice = input("Please enter a choice(1-5): ")
       if choice == '1':
           add_task()
       elif choice == '2':
           view_task()
       elif choice == '3':
           remove_task()
       elif choice == '4':
           mark_done()
       elif choice == '5':
           print("Exiting the Application... Goodbye!")
           break
       else:
           print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

