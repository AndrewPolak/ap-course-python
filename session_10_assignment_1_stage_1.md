```bash
# Run this command to create all required files for Session 10 (Assignment #1 - Stage 1).
touch session10_todo_stage1.py session10_todo_stage1_sol.py session10_todo_stage1_test.py
```

---

# **Session 10: Assignment #1 (Stage 1) - CLI To-Do Manager**

## **Introduction & Objectives**

In **Session 10**, we begin **Assignment #1 (Stage 1)**, where you’ll build a **CLI-based To-Do Manager**. This initial stage focuses on:

1. Creating a **simple command-line interface** (CLI) loop that prompts the user for commands.  
2. Managing tasks **in memory** (no file I/O yet).  
3. Implementing **add** and **remove** operations on tasks.  
4. Optionally listing or clearing tasks (if desired).  

By the end of this session (Stage 1 of the assignment), you’ll have a minimal **interactive** to-do system that can add and remove tasks in a **running session**. Future stages (Sessions 11, 14, 19, 25, etc.) will enhance this tool with persistence, argument parsing, JSON usage, OOP refactoring, tests, and more.

---

## **Detailed Explanations**

### **CLI Basics and Command Loop**

A **command-line interface** (CLI) reads input from the user in a loop. You typically:

1. **Prompt** the user for a command.
2. **Parse** the command (e.g., `add <task>`, `remove <task>`, `list`, `quit`).
3. **Dispatch** the logic to the appropriate function or code block.

**Example**:
```python
while True:
    cmd = input("Enter command: ")
    if cmd == "quit":
        break
    # else parse and handle
```
This approach allows an interactive session, where the user can type commands until they type something like `quit` to exit.

### **In-Memory Task Management**

We’ll store tasks in a **Python list** (or dictionary if you prefer). For Stage 1:
- **Add**: append a new task to the list (or check duplicates if you wish).
- **Remove**: search for a matching task string and remove it if found.
- **Optional**: list all tasks, or check if a task exists.

```python
tasks = []

# Add
tasks.append("Buy groceries")
# Remove
tasks.remove("Buy groceries")  # or do checks first
```

Because we’re only storing tasks in memory, all tasks vanish once the program ends. Future stages will add persistence.

### **Sample Workflow**

- User starts the program.  
- Program shows a prompt: `Enter command (add/remove/list/quit):`  
- If user enters `add Buy milk`, the program appends `"Buy milk"` to `tasks`.  
- If user enters `remove Buy milk`, the program finds and removes that item.  
- If user enters `list`, the program prints each task.  
- If user enters `quit`, the loop ends.  

We’ll keep it minimal in Stage 1, focusing on correctness and clarity.

### **Potential Edge Cases**

- Removing a task that doesn’t exist (handle gracefully).  
- Adding an empty or blank task (you might choose to reject or allow it).  
- No tasks present yet when the user tries `list` or `remove`.  

Handling these edge cases well is part of writing a user-friendly CLI.

---

## **Assignment #1, Stage 1: CLI To-Do Manager**

This stage implements a **bare-bones** to-do manager with in-memory tasks. Future sessions will expand it.

### **Requirements**

1. **Command Loop**: Repeatedly prompt the user for a command.  
2. **Add Command**: `add <task_description>` should add the task to an internal list.  
3. **Remove Command**: `remove <task_description>` should remove the matching task if it exists.  
4. **(Optional) List Command**: Print all current tasks.  
5. **Quit Command**: `quit` ends the program.  

Feel free to add more commands or minor features if you like, but these are the core requirements for Stage 1.

### **Exercise (session10_todo_stage1.py)**

**Starter Code**:
```python
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
    # 2. Start a while True loop to prompt the user for a command.
    # 3. Parse the input (e.g., split on spaces).
    # 4. Handle commands: add, remove, list, quit.
    # 5. Print helpful messages/feedback for each operation.
    pass

if __name__ == "__main__":
    main()
```

**Key Steps**  

1. **Initialize** `tasks = []`.  
2. Inside a `while True:` loop:
   - `user_input = input("Enter command: ").strip()`
   - If `user_input == "quit"`, break the loop.
   - Otherwise, parse `user_input.split(maxsplit=1)`.
     - If it starts with `"add "`, the second part is the task to add.
     - If it starts with `"remove "`, the second part is the task to remove.
     - If it’s `"list"`, print out tasks.
3. **Edge Cases**: If remove is called with a missing task, decide whether to print an error or silently ignore.

---

## **Reference Solution (session10_todo_stage1_sol.py)**
```python
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
```

---

## **Autotest Example (session10_todo_stage1_test.py)**

Below is a basic autotest script to demonstrate how you might test the CLI. It feeds commands as input and compares outputs line-by-line. Realistically, you may want more robust or advanced test logic as the project grows.

```python
# Save as: session10_todo_stage1_test.py
import subprocess

def run_solution(solution_file, input_data):
    completed_process = subprocess.run(
        ["python3", solution_file],
        input=input_data,
        text=True,
        capture_output=True
    )
    # We won't fail if returncode != 0, because the user might 'quit' or partial logic. 
    # But we could if we want strict checking:
    # if completed_process.returncode != 0:
    #     raise RuntimeError(f"Solution {solution_file} crashed.\nStderr: {completed_process.stderr.strip()}")
    return completed_process.stdout.strip().split('\n')

def test_todo_stage1(student_solution_file, reference_solution_file):
    test_input = (
        "add Buy milk\n"
        "add Go jogging\n"
        "list\n"
        "remove Buy milk\n"
        "list\n"
        "quit\n"
    )
    # Run both solutions
    ref_output = run_solution(reference_solution_file, test_input)
    student_output = run_solution(student_solution_file, test_input)

    # Compare line counts
    min_len = min(len(ref_output), len(student_output))
    for i in range(min_len):
        r_line = ref_output[i]
        s_line = student_output[i]
        if r_line != s_line:
            raise AssertionError(
                f"Output mismatch on line {i+1}:\n"
                f"Expected: {r_line}\n"
                f"Got:      {s_line}"
            )

    # If there's extra lines from either, we won't fail them automatically 
    # but you could add stricter checks if desired.

    print("CLI To-Do Manager (Stage 1) test passed for main commands.")

if __name__ == "__main__":
    test_todo_stage1("session10_todo_stage1.py", "session10_todo_stage1_sol.py")
```

**Note**: This test is somewhat simplistic. As the to-do manager gains complexity (e.g., file I/O, arguments, JSON storage), your tests will become more elaborate.

---

## **Additional Tips**

1. **Command Parsing**: If you find string splitting cumbersome, consider libraries like `argparse` (though that’s more for command-line arguments than an interactive loop).  
2. **User Feedback**: Provide clear messages when tasks are added or removed, or if a command is unknown.  
3. **Future Expansion**: In future sessions, you’ll add more features:  
   - **File Persistence** (Session 14, etc.)  
   - **JSON Format**  
   - **OOP Refactoring**  
   - **Type Hints & Tests**  

For Stage 1, keep it simple and functional.

---

## **Final Checklist for Session 10**

1. **Detailed Explanations Provided**  
   - Introduced how to build a simple CLI, store tasks in memory, parse commands, handle add/remove tasks.
2. **Assignment #1: Stage 1 Requirements**  
   - Minimal CLI with `add`, `remove`, (optional `list`), `quit`.
   - In-memory storage for tasks.
3. **Starter Code**  
   - Provided in `session10_todo_stage1.py`.
4. **Reference Solution**  
   - In `session10_todo_stage1_sol.py`, featuring a sample command loop.
5. **Sample Autotest**  
   - `session10_todo_stage1_test.py` feeding known commands, comparing output line-by-line.
6. **No Unexplained Concepts**  
   - All relevant CLI loop, string splitting, in-memory data structures covered in previous sessions.
7. **Self-Contained**  
   - Everything needed to implement Stage 1 of the CLI To-Do Manager is here.

**End of Session 10 Materials (Assignment #1, Stage 1).**