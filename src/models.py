import datetime
from typing import Literal
from .utils import generate_uid



class Task:
    def __init__(
            self, 
            description: str, 
            status: Literal[ "todo" , "done"],

            task_id: str = None, 
            createdAt: str = None,
            updatedAt: str = None,
        ):
        self.id= task_id if task_id else generate_uid()
        self.description= description.strip()
        self.status= status
        now= datetime.datetime.now().isoformat()
        self.createdAt = createdAt if createdAt else now
        self.updatedAt = updatedAt if updatedAt else now

    def to_dict(self):
        return{
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt":self.updatedAt,

        }   
    @classmethod 
    def from_dict(cls, task: dict[str, str]):
        return cls(
            task_id=task.get("id", None),
            description = task.get("description", ""),
            status = task.get("status", "todo"),
            createdAt = task.get("createdAt", "None"),
            updatedAt =task.get("updatedAt", None),
        )

    def __str__(self):
         return f"> ID: {self.id} | {self.description} | {self.status.capitalize()}"


class TaskNotFound(Exception):
        """Throw this error when the task is not found."""
        pass



       


               


