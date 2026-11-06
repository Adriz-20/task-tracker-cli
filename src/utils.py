import uuid

def generate_uid() -> str:
    """
    This function generates a Unique Identifier using UUID.uuid4.
    The output UID is a combination of first and item from the uuid4
    output.
    """
    parts = str(uuid.uuid4()).split("-")
    return "".join((parts[0], parts[-1]))

def ask_task_id() -> str:
    return input("Enter Task ID:")




