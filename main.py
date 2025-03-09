
def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
