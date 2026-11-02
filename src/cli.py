MENU = "--- Task Tracker CLI Mini Project ---\n"

MENU_OPTIONS = (
    "Add Task",
    "Update Task",
    "Delete Task",
    "Toggle Status",
    "List all Tasks",
    "List all Done Tasks",
    "List all ToDo Tasks",
    "Quit",
    
)

def get_menu() -> str:
    menu = "---  Task Tracker CLI Mini Project  ---\n"

    for idx, val in enumerate(MENU_OPTIONS):
        menu += f" ‣ {idx + 1} - {val}\n"

    return menu   

print(get_menu()) 
