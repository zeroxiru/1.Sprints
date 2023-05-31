from datetime import time


def get_user_task_info():
    task_title = input("Enter the name of the task title: ")
    task_status = input("Is the task don? (y/n): ")
    if task_status == "y":
        task_status = "done"
    else:
        task_status = "pending"
    task_assignee = input("Enter the name of the task assign person: ")

    task_object = {
        "task": task_title,
        "status": task_status,
        "assign_to": task_assignee
    }
    return  task_object


def add_task_info_to_list(tasks_list):
    task = get_user_task_info()
    tasks_list.append(task)

def remove_task_from_list(tasks_list):
    task_title = input("Enter the task title to remove from the list: ")

    # iterating over the list to find the task title and remove
    for i in range(len(task_title)):
        # get the task from the task list at index 1
        temp_task = tasks_list[i]
        temp_task_title = temp_task["task"]
        if task_title == temp_task_title:
            del tasks_list[i]
            break

def task_as_done(tasks_list):
    task_title = input("Enter the task title for make it as done: ")
    for task in tasks_list:
        if task["task"] == task_title:
            task["status"] = 'done'
            break
        else:
            print("task is not available in the list")

if __name__ == "__main__":
    #list of tasks
    tasks = []
    while True:
        user_input = input("Enter 'add' to add a task, 'remove' to remove "
                      "a task, 'mark' to mark a task as done,or 'show' to print or 'exit' to quit : ")
        if user_input == 'add':
            add_task_info_to_list(tasks)
        elif user_input == "remove":
            remove_task_from_list(tasks)
        elif user_input == "mark":
            task_as_done(tasks)
        elif user_input == "show":
            print(tasks)
        elif user_input == "exit":
            break
        else:
            print("invalid input. Please try again")

    # print("List of Tasks")
    # print(tasks)

