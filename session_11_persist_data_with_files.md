```bash
# Run this command to create all required files for Session 11.
touch session11_ex1_file_read.py session11_ex1_file_read_sol.py session11_ex1_file_read_test.py \
session11_ex2_file_write.py session11_ex2_file_write_sol.py session11_ex2_file_write_test.py \
session11_ex3_append_file.py session11_ex3_append_file_sol.py session11_ex3_append_file_test.py \
session11_ex4_file_exists.py session11_ex4_file_exists_sol.py session11_ex4_file_exists_test.py \
session11_ex5_pathlib_demo.py session11_ex5_pathlib_demo_sol.py session11_ex5_pathlib_demo_test.py \
session11_ex6_dir_creation.py session11_ex6_dir_creation_sol.py session11_ex6_dir_creation_test.py \
session11_ex7_task_saver.py session11_ex7_task_saver_sol.py session11_ex7_task_saver_test.py \
session11_ex8_read_config.py session11_ex8_read_config_sol.py session11_ex8_read_config_test.py
```

---

# **Session 11: Persisting Data with Files**

**Session Goals**:

1. Learn to **open**, **read**, and **write** text files in Python.
2. Practice **appending** to existing files.
3. Use **os** or **pathlib** to **check file existence**, handle paths, and create directories.
4. Explore how to store data like “tasks” or simple key-value config lines in a file.
5. Gain comfort with **file-based** operations for future assignment stages.

Below is a set of **8 exercises** (with sample solutions and a test example) illustrating file I/O in detail.

---

## **Detailed Explanations**

### **1. Reading Files**

Python’s `open("filename", "r")` yields a file object in **read** mode. Common methods:

- `read()` for entire file as one string.
- `readlines()` for a list of lines.
- Iterating the file object in a `for` loop line by line.

**Always** consider using a **`with`** block for automatic file closure:
```python
with open("input.txt", "r") as f:
    content = f.read()
    # process content
```

### **2. Writing & Appending**

- **Write (`"w"`)**: Overwrites file if it exists, or creates a new file.
- **Append (`"a"`)**: Keeps existing content and adds new lines at the end.

```python
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

with open("output.txt", "a") as f:
    f.write("Third line\n")
```

### **3. Checking File Existence / Using `os` or `pathlib`**

- **`os.path.exists("filename")`** → `True/False`.
- **`pathlib.Path("filename").exists()`** → `True/False`.

`pathlib` is a modern, object-oriented approach to paths, letting you do things like:
```python
from pathlib import Path
p = Path("somefile.txt")
print(p.exists())
print(p.resolve())
```

### **4. Creating Directories**

- **`os.makedirs("logs", exist_ok=True)`** or
- **`Path("logs").mkdir(parents=True, exist_ok=True)`**  
Ensures a directory exists, skipping creation if it’s already present.

### **5. Storing Data (Examples: Tasks, Config)**

You can store data line by line. For example, a “tasks” file might hold:

```
Buy groceries
Finish reading book
Email manager
```

Alternatively, a “config” file might hold simple key-value pairs:

```
username=alice
timeout=30
theme=dark
```

Reading these lines back into Python data structures allows you to persist user preferences or tasks across runs.

---

## **Exercises**

Below are **8** exercises covering reading, writing, appending, checking existence, directory creation, and storing data in files.

### **Exercise 1: Basic File Read**

**Description:**

1. Create a file `sample_input.txt` with some lines of text (locally).
2. Write a Python script that **reads** the entire file and prints it out.
3. If the file doesn’t exist, handle it gracefully (print an error).

**Starter Code**:  
```python
# Save as: session11_ex1_file_read.py

def main():
    # TODO:
    # 1. Attempt to open "sample_input.txt" in read mode.
    # 2. Print its contents.
    # 3. Handle FileNotFoundError (or check existence first).
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 2: Basic File Write**

**Description:**

1. Prompt the user for lines of text in a loop until they enter an empty line or “stop”.
2. Write each line to `user_output.txt`.
3. Print a confirmation when done.

**Starter Code**:
```python
# Save as: session11_ex2_file_write.py

def main():
    # TODO:
    # 1. Collect lines in a list until user enters empty or "stop".
    # 2. Write them to "user_output.txt" in 'w' mode.
    # 3. Print "Saved lines to user_output.txt."
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 3: Appending to a File**

**Description:**

1. Prompt the user for a single line of text.
2. Append it to `journal.txt` (in “a” mode).
3. Print “Appended to journal.txt” when done.

**Starter Code**:
```python
# Save as: session11_ex3_append_file.py

def main():
    # TODO:
    # 1. Prompt user for one line of text.
    # 2. Open "journal.txt" in "a" mode.
    # 3. Write the line + "\n".
    # 4. Print confirmation.
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 4: Checking File Existence**

**Description:**

1. Prompt the user for a filename.
2. Use either **os** or **pathlib** to check if it exists.
3. Print “File exists” or “File does not exist”.

(Optional) If file exists, print its size in bytes or last modification time.

**Starter Code**:
```python
# Save as: session11_ex4_file_exists.py

def main():
    # TODO:
    # 1. import os or pathlib
    # 2. prompt user for filename
    # 3. check existence
    # 4. optional: print size or modification time
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 5: Using pathlib Demo**

**Description:**

1. Prompt for a directory name, create it if missing.
2. Create a file `example.txt` in that directory.
3. Write a sample line, then print the absolute path to `example.txt`.

**Starter Code**:
```python
# Save as: session11_ex5_pathlib_demo.py

def main():
    # TODO:
    # 1. from pathlib import Path
    # 2. prompt for a dir
    # 3. Path(dir).mkdir(exist_ok=True)
    # 4. create example.txt inside, write a line
    # 5. print absolute path
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 6: Creating Directories Recursively**

**Description:**
Similar to Exercise 5, but:

1. Prompt for a path that may include subdirectories (e.g. “logs/2023/march”).
2. Use `os.makedirs` or `Path(...).mkdir(parents=True, exist_ok=True)` to create all levels.
3. Print a success message. If the directory already exists, skip creation but still print “Directory already existed or created.”

**Starter Code**:
```python
# Save as: session11_ex6_dir_creation.py

def main():
    # TODO:
    # 1. prompt for subdirectory path
    # 2. create all levels (parents=True)
    # 3. print success
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 7: Saving a Small “Task” List**

*(This is **not** the official assignment manager—just a small example.)*

**Description:**

1. Prompt the user for tasks (one per line) until “stop”.
2. Write them to `tasks_demo.txt`.
3. Then read them back from `tasks_demo.txt` and print them to confirm.

**Starter Code**:
```python
# Save as: session11_ex7_task_saver.py

def main():
    # TODO:
    # 1. tasks = []
    # 2. collect tasks until "stop"
    # 3. write them to tasks_demo.txt
    # 4. read them back, print
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 8: Reading a Simple Config File**

**Description:**

1. Create `config_demo.txt` with lines like:
   ```
   username=alice
   theme=dark
   timeout=30
   ```
2. Write a script that opens `config_demo.txt` in read mode, parses each line as key=value, and stores them in a dictionary.  
3. Print the dictionary.

**Starter Code**:
```python
# Save as: session11_ex8_read_config.py

def main():
    """
    1. open config_demo.txt in 'r'
    2. parse each line as key=value
    3. store in a dict
    4. print the dict
    """
    # TODO: implement
    pass

if __name__ == "__main__":
    main()
```

---

## **Reference Solutions**

### **session11_ex1_file_read_sol.py**
```python
# Save as: session11_ex1_file_read_sol.py

def main():
    try:
        with open("sample_input.txt", "r") as f:
            content = f.read()
            print(content, end="")  # 'end=""' to avoid double newlines
    except FileNotFoundError:
        print("Error: 'sample_input.txt' not found. Please create it first.")

if __name__ == "__main__":
    main()
```

---

### **session11_ex2_file_write_sol.py**
```python
# Save as: session11_ex2_file_write_sol.py

def main():
    lines = []
    while True:
        user_input = input("Enter text (or 'stop' / empty to finish): ")
        if not user_input or user_input.lower() == "stop":
            break
        lines.append(user_input)

    with open("user_output.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")
    print("Saved lines to user_output.txt")

if __name__ == "__main__":
    main()
```

---

### **session11_ex3_append_file_sol.py**
```python
# Save as: session11_ex3_append_file_sol.py

def main():
    line = input("Enter a line to append: ")
    with open("journal.txt", "a") as f:
        f.write(line + "\n")
    print("Appended to journal.txt")

if __name__ == "__main__":
    main()
```

---

### **session11_ex4_file_exists_sol.py**
```python
# Save as: session11_ex4_file_exists_sol.py
import os

def main():
    fname = input("Enter a filename to check: ").strip()
    if os.path.exists(fname):
        print("File exists.")
        size = os.path.getsize(fname)
        print(f"Size: {size} bytes")
        # optional: mod_time = os.path.getmtime(fname)
    else:
        print("File does not exist.")

if __name__ == "__main__":
    main()
```

*(Alternatively, could use pathlib.)*

---

### **session11_ex5_pathlib_demo_sol.py**
```python
# Save as: session11_ex5_pathlib_demo_sol.py
from pathlib import Path

def main():
    dirname = input("Enter a directory name: ").strip()
    d = Path(dirname)
    d.mkdir(exist_ok=True)

    file_path = d / "example.txt"
    with open(file_path, "w") as f:
        f.write("Sample content.\n")

    print("Created example.txt at:", file_path.resolve())

if __name__ == "__main__":
    main()
```

---

### **session11_ex6_dir_creation_sol.py**
```python
# Save as: session11_ex6_dir_creation_sol.py
import os

def main():
    path_str = input("Enter directory path (may include subdirs): ").strip()
    os.makedirs(path_str, exist_ok=True)
    print(f"Directory '{path_str}' created (or already existed).")

if __name__ == "__main__":
    main()
```

*(Could also use Path with `parents=True`.)*

---

### **session11_ex7_task_saver_sol.py**
```python
# Save as: session11_ex7_task_saver_sol.py

def main():
    tasks = []
    while True:
        t = input("Enter a task (or 'stop' to finish): ").strip()
        if not t or t.lower() == "stop":
            break
        tasks.append(t)

    with open("tasks_demo.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

    print("Tasks saved to tasks_demo.txt. Now reading them back...")

    with open("tasks_demo.txt", "r") as f:
        lines = f.readlines()

    print("Tasks read back:")
    for line in lines:
        print(line.strip())

if __name__ == "__main__":
    main()
```

---

### **session11_ex8_read_config_sol.py**
```python
# Save as: session11_ex8_read_config_sol.py

def main():
    config = {}
    try:
        with open("config_demo.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        print("config_demo.txt not found, using default empty config.")

    print("Config dictionary:", config)

if __name__ == "__main__":
    main()
```

---

## **Autotest Example**

Below is an example autotest for **Exercise 1** (`session11_ex1_file_read.py`). It:
1. Creates `sample_input.txt`.
2. Runs the student solution and the reference solution, capturing output.
3. Compares line by line.

```python
# Save as: session11_ex1_file_read_test.py
import subprocess
import os

def run_solution(solution_file):
    completed_process = subprocess.run(
        ["python3", solution_file],
        text=True,
        capture_output=True
    )
    return completed_process.stdout.strip().split('\n')

def test_file_read(student_solution_file, reference_solution_file):
    sample_filename = "sample_input.txt"

    # create sample file
    with open(sample_filename, "w") as f:
        f.write("Hello\nWorld\n")

    ref_output = run_solution(reference_solution_file)
    student_output = run_solution(student_solution_file)

    # cleanup
    os.remove(sample_filename)

    # compare
    if ref_output != student_output:
        raise AssertionError(
            f"Mismatch reading sample_input.txt.\nExpected: {ref_output}\nGot: {student_output}"
        )

    print("File read test passed for exercise 1.")

if __name__ == "__main__":
    test_file_read("session11_ex1_file_read.py", "session11_ex1_file_read_sol.py")
```

*(You’d replicate a similar pattern for other exercises, but each may require its own approach. For instance, the “append file” test might check appended lines, the “task saver” test might check tasks_demo.txt, etc.)*

---

## **Additional Resources**

- [Python: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [os module documentation](https://docs.python.org/3/library/os.html)
- [pathlib module documentation](https://docs.python.org/3/library/pathlib.html)
- [Real Python: Working with Files in Python](https://realpython.com/read-write-files-python/)

---

## **Final Checklist for Session 11**

1. **Detailed Explanations**  
   - File reading (modes, loops, methods).
   - File writing/appending, with caution about overwriting data.
   - Checking file existence (`os.path.exists` or `pathlib.Path.exists`).
   - Directory creation with `os.makedirs` or `Path.mkdir`.
   - Small data storage demos (tasks, config).

2. **8 Exercises**  
   - Reading, writing, appending, existence check, pathlib usage, directory creation, saving tasks, reading config.

3. **Starter Code & Reference Solutions**  
   - Provided for each exercise with `# Save as:` filenames.

4. **Sample Autotest**  
   - Showcased an example for exercise 1 (file read test).

5. **No Unexplained Concepts**  
   - All file I/O features introduced.

6. **Self-Contained**  
   - Everything for practicing file read/write, directory creation, small data demonstrations is included.

---

**End of Session 11 Materials**