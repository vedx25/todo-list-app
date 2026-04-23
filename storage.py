import json

def save_to_file(tasks):
    """Saves the current task list to a JSON file."""
    with open('tasks_db.json', 'w') as f:
        json.dump(tasks, f)
    print("...System: Data persisted successfully.")

def load_from_file():
    """Loads tasks from the JSON file on startup."""
    try:
        with open('tasks_db.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
