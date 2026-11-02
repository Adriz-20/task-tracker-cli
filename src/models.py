import datetime
from utils import generate_uid
from typing import Literal

class Task:
    def __init__(
            self, 
            description: str, 
            status: Literal[ "todo" , "done"],
        ):
        self.id= generate_uid()
        self.description= description.strip()
        self.status= status
        now= datetime.datetime.now()
        self.createedAt = now
        self.updateAt =now

class TaskTracker:
    def __init__(self):
        pass        
