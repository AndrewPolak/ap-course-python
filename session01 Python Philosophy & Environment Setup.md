Below is the comprehensive set of materials for **Session 1: Python Philosophy & Environment Setup**.

---

## 1. Explanations

### Python Philosophy and Differences from C

Python is often described as a high-level, interpreted language that emphasizes readability, simplicity, and developer productivity. Unlike C, which is a compiled language with a strong focus on manual memory management and type specificity, Python handles many details automatically.

**Key Philosophical Points:**

- **Readability:** Python’s syntax is designed to be clear and easy to read. The community motto, "Readability counts," is embedded in the language’s guiding principles.  
- **Batteries Included:** Python comes with a rich standard library that handles a wide range of tasks (e.g., file operations, networking, math functions) without requiring third-party dependencies.  
- **Interpreted and Dynamically Typed:** Unlike C, where you must declare variable types explicitly and compile code before running, Python allows you to write code and run it immediately. Variables can hold different data types at different times, reducing boilerplate but requiring careful consideration to avoid type-related errors.

**Practical Implications Compared to C:**

- **Typing:**  
  In C:
  ```c
  int x = 10;
  ```
  In Python:
  ```python
  x = 10
  ```
  Here, `x` can later be assigned a string without complaint from the interpreter. This makes Python flexible, but you must be mindful of what types you’re storing and using.

- **Memory Management:**  
  In C, you manually manage memory with functions like `malloc()` and `free()`. In Python, memory management is automatic (garbage collection), so you focus more on logic than on low-level resource handling.  
  However, this abstraction can mean Python is generally slower at certain tasks compared to C. If performance becomes critical, Python offers ways to integrate with C or use optimized libraries.

- **Compilation vs. Interpretation:**  
  C code is compiled into machine instructions before running. Python code is interpreted line-by-line at runtime by the Python interpreter. This makes Python code more portable and easier to run on many platforms without recompilation, but can make Python slower than C.

**Official Python Documentation:** [https://docs.python.org/3/](https://docs.python.org/3/)

---

### Setting Up a Python Environment

A Python environment isolates your project’s dependencies so that changes in one project won’t break another. This mirrors C’s use of libraries and headers, but Python provides dedicated tools to create lightweight "virtual environments".

**Why Use Virtual Environments (`venv`)?**

- **Dependency Isolation:** If you have multiple Python projects, they may depend on different versions of the same library. A virtual environment ensures each project uses its own "copy" of Python and libraries.  
- **Reproducibility:** Other team members or servers can recreate your environment from a requirements file.  
- **Cleaner Global Setup:** Avoids cluttering your system’s global Python installation.

**How to Create and Use a `venv`:**

1. **Check Your Python Installation:**
   Run `python3 --version` or `python --version` in your terminal. If it prints a version number (e.g., `Python 3.10.4`), Python is installed.

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv myenv
   ```
   This creates a folder named `myenv` containing a local copy of the Python interpreter and its standard library.

3. **Activate the Environment:**
   On Linux/macOS:
   ```bash
   source myenv/bin/activate
   ```
   On Windows:
   ```bash
   myenv\Scripts\activate
   ```
   
   Your terminal prompt should change to indicate you are inside a virtual environment. For example, it might show `(myenv)` before your command prompt.

4. **Install Dependencies:**
   While the environment is active, any `pip install` commands you run will install packages only in that environment.

5. **Deactivate the Environment:**
   To return to the system-wide Python setup:
   ```bash
   deactivate
   ```

**Further Reading on `venv`:** [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

**Alternatives to `venv`:**

- **conda:** A popular alternative for data science environments.  
- **virtualenv:** An older tool similar to `venv`, used before Python’s built-in `venv` was available.

For this course, `venv` suffices. If you encounter a project that specifically uses `conda` or `Poetry`, know that the core idea—isolating dependencies—is the same.

---

### Basic Input and Output in Python

**Printing to the Screen:**

In Python, the `print()` function displays output to the terminal. This differs from C’s `printf()`, where you must specify format specifiers. Python’s `print()` automatically handles data conversion to strings.

Example:
```python
print("Hello, World!")
print(42)
print("The value of x is:", 10)
```

All these lines automatically convert their arguments to strings and print them with a newline at the end.

**Reading Input:**

Use `input()` to read a line of text from the user:
```python
name = input("Enter your name: ")
print("Hello,", name)
```

When `input()` is called, the program waits until the user presses Enter. The returned value is always a string.

**Comparing I/O with C:**

In C:
```c
#include <stdio.h>

int main() {
    char name[50];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Hello, %s\n", name);
    return 0;
}
```
In Python, you don’t need to worry about fixed buffer sizes for simple cases:
```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Official Python I/O Documentation:** [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html)

---

### Trying It Out Interactively

To explore these concepts, try using the Python REPL (Read-Eval-Print Loop):

```bash
python3
```

Once inside the interactive shell:
```python
>>> x = 10
>>> print(x)
10
>>> name = input("Name? ")
Name? Alice
>>> print("Hi,", name)
Hi, Alice
```

This is a great way to test small code snippets quickly.

---

## 2. Exercises

These exercises will help you practice setting up a Python environment, printing output, and reading input. Make sure you’ve understood all the concepts above before starting.

### Exercise 1: Verify Python Installation

**Description:**  
Check if Python is installed and print the version. This exercise is more conceptual and does not require code submission. Just open your terminal and run a command.

**Tasks:**  
1. Run `python3 --version` (or `python --version`) in your terminal.
2. Confirm Python 3.x is installed.
3. If not installed, follow the official instructions for your platform to install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

No code files needed for this exercise.

---

### Exercise 2: Create and Activate a Virtual Environment

**Description:**  
Create a virtual environment, activate it, install a package, and then deactivate it.

**Tasks:**  
1. Run: `python3 -m venv project_env`
2. Activate the environment:
   - Linux/macOS: `source project_env/bin/activate`
   - Windows: `project_env\Scripts\activate`
3. Inside the environment, run: `pip install requests`
4. Confirm installation: `pip list`
5. Deactivate environment: `deactivate`

No code files needed for this exercise. You’ll just use your terminal.

---

### Exercise 3: Print a Custom Message

**Description:**  
Write a Python program that prints the message `"Environment setup complete!"` and then prints the Python version currently in use by reading `sys.version` from the `sys` module.

**What You’ll Practice:**  
- Basic printing
- Using standard library modules (like `sys`)

**Requirements:**  
- Print the exact message: `Environment setup complete!`
- Print the Python version (this will be a long string containing version info).

**Example Output:**
```
Environment setup complete!
You are using Python version: 3.10.4 (main, Apr 20 2022, 14:23:51) [Clang 12.0.0 (clang-1200.0.32.29)]
```

*(Note: Your actual Python version and build details may differ.)*

---

### Exercise 4: Greet the User

**Description:**  
Write a Python program that:
1. Prompts the user: `"Enter your name: "`
2. Reads the input name.
3. Prints: `"Hello, <name>, welcome to Python!"`

**Example Input:**
```
Alice
```

**Example Output:**
```
Hello, Alice, welcome to Python!
```

---

### Exercise 5: Simple Interaction

**Description:**  
Write a program that:
1. Asks the user for their favorite number.
2. Reads the number (as a string).
3. Prints: `"Your favorite number is <number>."`

Try entering different types of inputs (e.g., `42`, `forty-two`) to see how Python handles them. For now, just treat them as strings.

**Example Input:**
```
42
```

**Example Output:**
```
Your favorite number is 42.
```

---

## 3. Starter Code, Reference Solutions, and Autotests

For Exercises 3–5, we provide code files. Exercises 1 and 2 are conceptual (no code required).

### Exercise 3: Print a Custom Message

**Starter Code:**
```python
# Save as: print_message.py
# Starter code for "Print a Custom Message".
# Instructions: Print "Environment setup complete!"
# and then print your Python version from sys.version.

import sys

def main():
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    main()
```

**Reference Solution:**
```python
# Save as: print_message_sol.py
# Reference solution for "Print a Custom Message".

import sys

def main():
    print("Environment setup complete!")
    print("You are using Python version:", sys.version.strip())

if __name__ == "__main__":
    main()
```

**Autotest:**
```python
# Save as: print_message_test.py
# Autotest script for "Print a Custom Message".

import subprocess

def test_solution(solution_file):
    completed_process = subprocess.run(
        ["python3", solution_file],
        text=True,
        capture_output=True
    )
    output = completed_process.stdout.strip().split('\n')
    assert len(output) >= 2, "Expected at least two lines of output."
    assert output[0] == "Environment setup complete!", "First line does not match expected output."
    assert "Python version" in output[1], "Second line should contain 'Python version'."

if __name__ == "__main__":
    print("Testing reference solution...")
    test_solution("print_message_sol.py")
    print("All tests passed!")
```

---

### Exercise 4: Greet the User

**Starter Code:**
```python
# Save as: greet_user.py
# Starter code for "Greet the User".
# Instructions: Prompt the user for their name and print a greeting.

def main():
    # TODO: Implement solution
    # Hint: Use input() to read the user name and print() to greet.
    pass

if __name__ == "__main__":
    main()
```

**Reference Solution:**
```python
# Save as: greet_user_sol.py
# Reference solution for "Greet the User".

def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}, welcome to Python!")

if __name__ == "__main__":
    main()
```

**Autotest:**
```python
# Save as: greet_user_test.py
# Autotest script for "Greet the User".

import subprocess

def test_solution(solution_file):
    test_input = "Alice\n"
    completed_process = subprocess.run(
        ["python3", solution_file],
        input=test_input,
        text=True,
        capture_output=True
    )
    output = completed_process.stdout.strip()
    expected = "Hello, Alice, welcome to Python!"
    assert output == expected, f"Expected: '{expected}' but got: '{output}'"

if __name__ == "__main__":
    print("Testing reference solution...")
    test_solution("greet_user_sol.py")
    print("All tests passed!")
```

---

### Exercise 5: Simple Interaction

**Starter Code:**
```python
# Save as: favorite_number.py
# Starter code for "Simple Interaction".
# Instructions: Ask the user for their favorite number and print it back.

def main():
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    main()
```

**Reference Solution:**
```python
# Save as: favorite_number_sol.py
# Reference solution for "Simple Interaction".

def main():
    number = input("Enter your favorite number: ")
    print(f"Your favorite number is {number}.")

if __name__ == "__main__":
    main()
```

**Autotest:**
```python
# Save as: favorite_number_test.py
# Autotest script for "Simple Interaction".

import subprocess

def test_solution(solution_file):
    test_input = "42\n"
    completed_process = subprocess.run(
        ["python3", solution_file],
        input=test_input,
        text=True,
        capture_output=True
    )
    output = completed_process.stdout.strip()
    expected = "Your favorite number is 42."
    assert output == expected, f"Expected: '{expected}' but got: '{output}'"

    # Test another input
    test_input = "forty-two\n"
    completed_process = subprocess.run(
        ["python3", solution_file],
        input=test_input,
        text=True,
        capture_output=True
    )
    output = completed_process.stdout.strip()
    expected = "Your favorite number is forty-two."
    assert output == expected, f"Expected: '{expected}' but got: '{output}'"

if __name__ == "__main__":
    print("Testing reference solution...")
    test_solution("favorite_number_sol.py")
    print("All tests passed!")
```

---

## 4. Additional Resources

- Official Python Tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)  
- Python `venv` Guide: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)  
- Python I/O: [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html)

Try exploring these resources to deepen your understanding of Python’s environment setup and basic I/O.

---

## 5. Final Checklist

- **Detailed Explanations Provided?**  
  Yes. Explained Python’s philosophy, differences from C, memory management, and the benefits of `venv`. Covered basic print and input thoroughly.

- **All Concepts Used in Exercises Explained?**  
  Yes. We explained `print()`, `input()`, and environment setup before the exercises that require them.

- **3–5 Exercises per Concept?**  
  Yes. Exercises 1–2 (environment, conceptual), Exercise 3 (print and sys.version), Exercise 4 (input and output), Exercise 5 (further input practice). That’s 5 exercises.

- **Starter Code, Reference Solutions, and Autotests Provided?**  
  Yes. Exercises 3–5 have starter code, reference solutions, and autotests in separate code blocks.

- **Links to Official Documentation?**  
  Yes. Included links to Python docs for general Python, `venv`, and I/O.

- **No Unmet Dependencies?**  
  Yes. All introduced code and concepts appear after they are explained.

- **Self-Contained Content?**  
  Yes. All materials for Session 1 are included here: explanations, exercises, code, tests.

Everything meets the specified criteria.

---

**End of Session 1 Materials**