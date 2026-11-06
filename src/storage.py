import os
import json
from .models import Task

FILENAME= "tasks.json"

def ensure_file_exists() -> None:
    if not os.path.exists(FILENAME):
        with open (FILENAME, "x", encoding="utf-8") as f:
            json.dump("[]", f, indent=4)





def read_data() -> list[Task]:
    with open(FILENAME, "r", encoding="utf-8") as f:
        tasks = list(json.load(f))
        return [Task.from_dict(task) for task in tasks]



def write_data(tasks: list[Task]) -> None:
    serialized_task = [task.to_dict() for task in tasks]
    with open(FILENAME, "w", encoding="utf-8")as f:
        json.dump(serialized_task, f, indent=4)
 