# Save as: session10_todo_stage1.py
def main():
    """
    CLI To-Do Manager (Stage 1)
    - In-memory tasks
    - add <task>
    - remove <task>
    - list (optional)
    - quit
    """
    # TODO:
    # 1. Initialize an empty list for tasks.
    print("Welcome to the CLI To-Do Manager (Stage 1)")
    print("Commands: add <task>, remove <task>, list, quit")
    tasks = []
    # 2. Start a while True loop to prompt the user for a command.
    while True:
        # 3. Parse the input (e.g., split on spaces).
        # 4. Handle commands: add, remove, list, quit.
        # 5. Print helpful messages/feedback for each operation.
        command = input("Enter command: ").strip()
        split_command = command.split(' ', maxsplit=1)
        method = split_command[0].strip()
        args = split_command[1].strip() if len(split_command) > 1 else ""

        if method == "add":
            task = args
            if not task:
            # if task == "":
                print("Usage: add <task_description>")
                continue
            tasks.append(task)
            print(f"Added task: {task}")
        elif method == "remove":
            task = args
            if not task:
            # if task == "":
                print("Usage: remove <task_description>")
                continue
            if task in tasks:
                tasks.remove(task)
                print(f"Removed task: {task}")
            else:
                print(f"Error: unable to remove {task} as it does not exist")
        elif method == "list":
            if len(tasks) > 0:
                print("Current tasks: ")
                for position, task in enumerate(tasks, 1):
                    print(f"{position}. {task}")
            else:
                print("Task list is empty.")
        elif method == "quit":
            print("Exiting To-Do Manager.")
            break
        else:
            print(f"Unknown command: {command}. Try 'add', 'remove', 'list', or 'quit'.")

if __name__ == "__main__":
    main()