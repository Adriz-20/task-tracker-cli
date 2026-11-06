from .models import Task, TaskNotFound
from .storage import write_data, read_data
from typing import Literal

class TaskTracker:
    def __init__(self):
        self.tasks = read_data()

    def __find_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                return task  

        raise TaskNotFound(f"Task with ID: {task_id} does not exist.")      

    def add(self, description: str) -> Task:
        new_task = Task(description, "todo")  
        self.tasks.append(new_task)

        write_data(self.tasks)

        return new_task 

    def update(self, id: str, description: str) -> Task:
        task = self.__find_task(id)
        task.description = description
        write_data(self.tasks) 

    def delete(self, id: str) -> None:
        task = self.__find_task(id)
        self.tasks.remove(task)

        write_data(self.tasks)       

    def toggle_status(self, id: str) -> str :
        task = self.__find_task(id)
        task.status = "todo" if task.status == "done" else "done"

    def list_tasks(self, status: Literal["todo", "done"] = None) -> list[Task]:
        if not status:
            return self.tasks

        result: list[Task] = []
        if status == "todo":
            for i in self.tasks:
                if i.status == "todo":
                    result.append(i)

                    

        elif status == "done":
            for i in self.tasks:
                if i.status == "done":
                    result.append(i)

        else:
            raise ValueError(f"{status} is invalid")   
        
        return result          


       
       


    