from src.cli import get_menu
from src.storage import ensure_file_exists
from src.tracker import TaskTracker
from src.utils import ask_task_id
from src.models import Task

def print_tasks(tasks: list[Task]) -> None:

    for task in tasks:
        print(task)    


def main():
    menu = get_menu()
    tracker = TaskTracker()

    while True:
        print(menu)

        user_inp = int(input(">>"))

        match user_inp:
            case 1: 
                description = input("Enter task description:")
                task=tracker.add(description)
                print("New Task Added with ID: {task.id}")

            case 2:
                task_id = ask_task_id()
                description = input("Enter new description:")

                tracker.update(task_id, description)

            case 3:
                task_id = ask_task_id()    
                tracker.delete(task_id)

            case 4:
                task_id = ask_task_id()   
                new_status=tracker.toggle_status(task_id) 
                print(f"New Status is {new_status.capitalize()}\n")

            case 5:   
                all_tasks=tracker.list_tasks() 
                print_tasks(all_tasks)

            case 6:  
                done_tasks=tracker.list_tasks("done") 
                print_tasks(done_tasks) 
                
                

            case 7:   
                todo_tasks=tracker.list_tasks("todo")  
                print_tasks(todo_tasks)
                         

            case 8:
                print("Task Tracker Ended. Good Buy!")
                break          


# problem
if __name__== "__main__":
    ensure_file_exists()
    main()
