# Save as: session10_todo_stage1_sol.py

def main():
    tasks = []
    print("Welcome to the CLI To-Do Manager (Stage 1).")
    print("Commands: add <task>, remove <task>, list, quit")

    while True:
        user_input = input("Enter command: ").strip()
        if not user_input:
            continue  # skip empty inputs

        parts = user_input.split(maxsplit=1)
        cmd = parts[0].lower()

        if cmd == "quit":
            print("Exiting To-Do Manager.")
            break

        elif cmd == "add":
            if len(parts) < 2:
                print("Usage: add <task_description>")
                continue
            task = parts[1].strip()
            tasks.append(task)
            print(f"Added task: '{task}'")

        elif cmd == "remove":
            if len(parts) < 2:
                print("Usage: remove <task_description>")
                continue
            task = parts[1].strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Removed task: '{task}'")
            else:
                print(f"Task '{task}' not found.")

        elif cmd == "list":
            if tasks:
                print("Current tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("No tasks yet.")

        else:
            print(f"Unknown command: {cmd}. Try 'add', 'remove', 'list', or 'quit'.")

if __name__ == "__main__":
    main()