```bash
# Run this command to create all required files for Session 9.
touch session9_ex1_basic_try_except.py session9_ex1_basic_try_except_sol.py session9_ex1_basic_try_except_test.py \
session9_ex2_finally.py session9_ex2_finally_sol.py session9_ex2_finally_test.py \
session9_ex3_custom_exceptions.py session9_ex3_custom_exceptions_sol.py session9_ex3_custom_exceptions_test.py \
session9_ex4_raise_exceptions.py session9_ex4_raise_exceptions_sol.py session9_ex4_raise_exceptions_test.py \
session9_ex5_multiple_excepts.py session9_ex5_multiple_excepts_sol.py session9_ex5_multiple_excepts_test.py \
session9_ex6_wrap_file_input.py session9_ex6_wrap_file_input_sol.py session9_ex6_wrap_file_input_test.py \
session9_ex7_exception_chaining.py session9_ex7_exception_chaining_sol.py session9_ex7_exception_chaining_test.py \
session9_ex8_nested_try.py session9_ex8_nested_try_sol.py session9_ex8_nested_try_test.py
```

---

# **Session 9: Handling Errors Gracefully**

## **Detailed Explanations**

In this session, we focus on **exception handling**—the mechanism Python uses to respond to runtime errors or unexpected conditions. Properly managing errors leads to more robust, user-friendly programs. We’ll cover:

1. **try/except** blocks to catch exceptions.
2. **finally** clauses for guaranteed cleanup.
3. **Raising exceptions** (`raise`) to signal an error intentionally.
4. **Custom exception classes** for specialized error handling.
5. **Wrapping file or input parsing** in try/except for real-world examples.
6. **Multiple except blocks** and advanced flows like **exception chaining** or **nested try** blocks.

### **1. Basic try/except**

A `try/except` block allows you to **attempt** some code in the `try` portion. If an **exception** occurs, Python **jumps** to the `except` block that matches the exception type.

```python
try:
    x = int(input("Enter a number: "))
    print("Success:", x)
except ValueError:
    print("That wasn't a valid integer!")
```

- If no error occurs, `except` is skipped.
- If a `ValueError` occurs (like input being "abc"), we handle it gracefully instead of crashing.

### **2. The finally Clause**

You can use `finally` to ensure a block of code executes **whether or not** an exception occurs (e.g., closing a file or releasing a resource):

```python
try:
    file_obj = open("data.txt", "r")
    # do something
except FileNotFoundError:
    print("File not found!")
finally:
    file_obj.close()  # Always runs, even if exception or no exception
```

This is commonly replaced by the **with** statement for file handling, but `finally` is still invaluable for resources that require manual cleanup.

### **3. Raising Exceptions**

You can **raise** an exception manually with the `raise` keyword:
```python
if age < 0:
    raise ValueError("Age cannot be negative")
```
This halts normal flow and signals to upstream code that something unexpected happened.

### **4. Custom Exceptions**

You can define your own exception classes to represent domain-specific errors. This makes it clearer to callers what went wrong. For instance:
```python
class InvalidUsernameError(Exception):
    pass

def validate_username(username):
    if len(username) < 3:
        raise InvalidUsernameError("Username too short!")
```

### **5. Wrapping File/Input Parsing**

Real-world examples often involve files that might not exist, or input data in the wrong format. Wrapping these operations in try/except ensures your program can recover or give meaningful error messages.

```python
def read_numbers(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return [int(line) for line in lines]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except ValueError:
        print("File contains non-integer data.")
        return []
```

### **6. Multiple Excepts & Advanced Flows**

- **Multiple except**: You can handle different exceptions differently.  
- **Exception chaining**: Sometimes you want to raise a new exception but preserve the original.  
- **Nested try**: A `try` block within another `try` can separate different error contexts.

---

## **Exercises**

We present **8 exercises** to deepen your mastery of Python’s exception handling. Each exercise includes:

1. A **description**  
2. **Starter code** with `TODO`  
3. Later sections contain the **reference solutions** and a **sample autotest**.

---

### **Exercise 1: Basic try/except**

**Description:**  
Prompt the user for an integer. If it’s not an integer, print `"Invalid integer!"`. Otherwise, print `"You entered <num>"`.

**Example Interaction**:
```
Enter an integer: abc
Invalid integer!

Enter an integer: 42
You entered 42
```

**Starter Code**:
```python
# Save as: session9_ex1_basic_try_except.py
def main():
    # TODO:
    # 1. Prompt for an integer.
    # 2. Wrap in try/except ValueError.
    # 3. Print success or "Invalid integer!".
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 2: The finally Clause**

**Description:**  

1. Prompt the user for a filename.  
2. Try to open it in read mode.  
3. If `FileNotFoundError`, print an error.  
4. In a `finally` block, print `"Attempted file operation."` to show it always runs.

**Starter Code**:
```python
# Save as: session9_ex2_finally.py
def main():
    # TODO:
    # 1. Prompt for a filename.
    # 2. Try opening it, read or do something trivial.
    # 3. except FileNotFoundError -> print error
    # 4. finally -> print "Attempted file operation."
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 3: Custom Exceptions**

**Description:**  
Create a custom exception `NegativeNumberError`. Prompt the user for a positive integer:

1. If the user enters a negative number, raise `NegativeNumberError`.  
2. Wrap this in try/except. If caught, print the error message.

**Example**:
```
Enter a positive integer: -5
Error: Input -5 is negative!
```

**Starter Code**:
```python
# Save as: session9_ex3_custom_exceptions.py

class NegativeNumberError(Exception):
    pass

def main():
    # TODO:
    # 1. Prompt user for an integer.
    # 2. If negative, raise NegativeNumberError("Input <num> is negative!")
    # 3. Wrap in try/except.
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 4: Raising Exceptions for Validation**

**Description:**  
Create a function `validate_username(username)`:

- If `username` is empty, raise `ValueError("Username cannot be empty")`.
- If `username` has spaces, raise `ValueError("Username cannot contain spaces")`.
- Otherwise, return `"Valid username"`.
  
In `main()`, prompt for a username, call `validate_username()`, handle any ValueError by printing the error message.

**Starter Code**:
```python
# Save as: session9_ex4_raise_exceptions.py
def validate_username(username):
    # TODO:
    # 1. If empty, raise ValueError("Username cannot be empty")
    # 2. If spaces, raise ValueError("Username cannot contain spaces")
    # 3. else return "Valid username"
    pass

def main():
    # 1. Prompt for username
    # 2. try:
    #       print(validate_username(...))
    #    except ValueError as e:
    #       print("Error:", e)
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 5: Multiple except Blocks**

**Description:**  
Prompt the user for two numbers (floats). Attempt to divide the first by the second:

- If `ValueError` (bad float input), print `"Invalid float input!"`.
- If `ZeroDivisionError`, print `"Cannot divide by zero!"`.
- Otherwise, print the quotient.

**Starter Code**:
```python
# Save as: session9_ex5_multiple_excepts.py
def main():
    # TODO:
    # 1. Prompt for two floats.
    # 2. try:
    #       parse them
    #       compute division
    #    except ValueError -> "Invalid float input!"
    #    except ZeroDivisionError -> "Cannot divide by zero!"
    # 3. print result if successful
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 6: Wrapping File & Input Parsing**

**Description:**  
Prompt user for a filename that supposedly contains integers (one per line):

1. Try to open the file and read each line as an integer, storing them in a list.  
2. If `FileNotFoundError`, print `"File not found."` and return an empty list.  
3. If `ValueError`, print `"Non-integer data found."` and return empty list.  
4. Print the list if successful.

**Starter Code**:
```python
# Save as: session9_ex6_wrap_file_input.py
def read_integers_from_file(filename):
    # TODO:
    # 1. open file in read mode
    # 2. read lines, convert to int
    # 3. handle FileNotFoundError, ValueError
    pass

def main():
    fname = input("Enter filename: ")
    numbers = read_integers_from_file(fname)
    print("Numbers read:", numbers)

if __name__ == "__main__":
    main()
```

---

### **Exercise 7: Exception Chaining**

**Description:**  
Write a function `process_data(data)` that:

1. If `len(data) == 0`, raise `ValueError("No data provided")`.  
2. If data is not a list, raise `TypeError("Data must be a list")`.  

In `main()`, handle these exceptions but chain them into a new `RuntimeError` with a custom message, preserving the original. This might look like:
```python
except (ValueError, TypeError) as e:
    raise RuntimeError("Data processing failed") from e
```
Then catch that `RuntimeError` at a higher level, printing the chain of errors.

*(This is more advanced, but it demonstrates exception chaining.)*

**Starter Code**:
```python
# Save as: session9_ex7_exception_chaining.py
def process_data(data):
    # TODO:
    # 1. if len(data) == 0, raise ValueError
    # 2. if not isinstance(data, list), raise TypeError
    # 3. else return "Data processed"
    pass

def main():
    # 1. try:
    #     - ask user whether to pass an empty list, non-list, or normal list
    #     - call process_data(...) 
    #    except (ValueError, TypeError) as e:
    #        raise RuntimeError("Data processing failed") from e
    # 2. also wrap main in another try to catch that RuntimeError and print chain
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 8: Nested try Blocks**

**Description:**  
Demonstrate a scenario with nested try:

1. Outer `try` handles opening a file.  
2. Inside that block, a second `try` handles reading integers from the file.  
3. If either fails, handle it at the appropriate level. Print success if all is well.

*(Similar to previous exercises but focuses explicitly on nested structure.)*

**Starter Code**:
```python
# Save as: session9_ex8_nested_try.py
def main():
    # TODO:
    # 1. Outer try: open filename
    # 2. inner try: parse lines as integers
    # 3. catch FileNotFoundError in outer except
    # 4. catch ValueError in inner except
    pass

if __name__ == "__main__":
    main()
```

---

## **Reference Solutions**

### **session9_ex1_basic_try_except_sol.py**
```python
# Save as: session9_ex1_basic_try_except_sol.py
def main():
    try:
        num_str = input("Enter an integer: ")
        num = int(num_str)
        print(f"You entered {num}")
    except ValueError:
        print("Invalid integer!")

if __name__ == "__main__":
    main()
```

---

### **session9_ex2_finally_sol.py**
```python
# Save as: session9_ex2_finally_sol.py
def main():
    filename = input("Enter filename: ")
    file_obj = None
    try:
        file_obj = open(filename, "r")
        data = file_obj.read()
        print("File content:", data)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    finally:
        print("Attempted file operation.")
        if file_obj:
            file_obj.close()

if __name__ == "__main__":
    main()
```

---

### **session9_ex3_custom_exceptions_sol.py**
```python
# Save as: session9_ex3_custom_exceptions_sol.py

class NegativeNumberError(Exception):
    pass

def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            raise NegativeNumberError(f"Input {num} is negative!")
        print(f"Valid input: {num}")
    except NegativeNumberError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
```

---

### **session9_ex4_raise_exceptions_sol.py**
```python
# Save as: session9_ex4_raise_exceptions_sol.py
def validate_username(username):
    if not username:
        raise ValueError("Username cannot be empty")
    if " " in username:
        raise ValueError("Username cannot contain spaces")
    return "Valid username"

def main():
    username = input("Enter username: ")
    try:
        result = validate_username(username)
        print(result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
```

---

### **session9_ex5_multiple_excepts_sol.py**
```python
# Save as: session9_ex5_multiple_excepts_sol.py
def main():
    try:
        a_str = input("Enter first float: ")
        b_str = input("Enter second float: ")
        a = float(a_str)
        b = float(b_str)
        result = a / b
        print(f"Result = {result}")
    except ValueError:
        print("Invalid float input!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

if __name__ == "__main__":
    main()
```

---

### **session9_ex6_wrap_file_input_sol.py**
```python
# Save as: session9_ex6_wrap_file_input_sol.py
def read_integers_from_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return [int(line) for line in lines]
    except FileNotFoundError:
        print("File not found.")
        return []
    except ValueError:
        print("Non-integer data found.")
        return []

def main():
    fname = input("Enter filename: ")
    numbers = read_integers_from_file(fname)
    print("Numbers read:", numbers)

if __name__ == "__main__":
    main()
```

---

### **session9_ex7_exception_chaining_sol.py**
```python
# Save as: session9_ex7_exception_chaining_sol.py
def process_data(data):
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    if len(data) == 0:
        raise ValueError("No data provided")
    return "Data processed"

def main():
    try:
        # Suppose we prompt user for how to test it
        choice = input("Enter 'empty', 'nonlist', or 'good': ")
        if choice == "empty":
            user_data = []
        elif choice == "nonlist":
            user_data = "I'm not a list"
        else:
            user_data = [1,2,3]

        try:
            result = process_data(user_data)
            print(result)
        except (ValueError, TypeError) as e:
            # Chain it
            raise RuntimeError("Data processing failed") from e

    except RuntimeError as re:
        # Print the entire chain
        print("Caught RuntimeError:", re)
        print("Cause:", re.__cause__)

if __name__ == "__main__":
    main()
```

---

### **session9_ex8_nested_try_sol.py**
```python
# Save as: session9_ex8_nested_try_sol.py
def main():
    filename = input("Enter a file with integers: ")
    try:
        with open(filename, "r") as f:
            try:
                lines = f.readlines()
                numbers = [int(line) for line in lines]
                print("Read numbers:", numbers)
            except ValueError:
                print("Failed to parse integers in the file.")
    except FileNotFoundError:
        print("File does not exist.")

if __name__ == "__main__":
    main()
```

---

## **Autotest Example**

Below is a sample autotest script for **Exercise 1** (`session9_ex1_basic_try_except.py`). It feeds various inputs, compares outputs with the reference solution’s outputs.

```python
# Save as: session9_ex1_basic_try_except_test.py
import subprocess

def run_solution(solution_file, input_data):
    completed_process = subprocess.run(
        ["python3", solution_file],
        input=input_data,
        text=True,
        capture_output=True
    )
    if completed_process.returncode != 0:
        raise RuntimeError(
            f"Solution {solution_file} crashed.\nStderr: {completed_process.stderr.strip()}"
        )
    return completed_process.stdout.strip().split('\n')

def test_solutions(student_solution_file, reference_solution_file):
    # Test valid integer
    input_data = "42\n"
    ref_output = run_solution(reference_solution_file, input_data)
    student_output = run_solution(student_solution_file, input_data)
    if ref_output != student_output:
        raise AssertionError(
            f"For input {input_data.strip()}:\nExpected: {ref_output}\nGot: {student_output}"
        )

    # Test invalid integer
    input_data = "abc\n"
    ref_output = run_solution(reference_solution_file, input_data)
    student_output = run_solution(student_solution_file, input_data)
    if ref_output != student_output:
        raise AssertionError(
            f"For input {input_data.strip()}:\nExpected: {ref_output}\nGot: {student_output}"
        )

    print("All tests passed for session9_ex1_basic_try_except.")

if __name__ == "__main__":
    test_solutions("session9_ex1_basic_try_except.py", "session9_ex1_basic_try_except_sol.py")
```

*(You can adapt this approach for other exercises, including simulating file creation or using mock data.)*

---

## **Additional Resources**

- **Python Tutorial: Errors and Exceptions**  
  [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)  
- **Built-in Exceptions**  
  [https://docs.python.org/3/library/exceptions.html](https://docs.python.org/3/library/exceptions.html)  
- **Real Python: Exceptions**  
  [https://realpython.com/python-exceptions/](https://realpython.com/python-exceptions/)

Explore these references for more advanced examples (like contextlib, custom base exception hierarchies, or logging exceptions).

---

## **Final Checklist**

1. **Detailed, Substantive Explanations:**  
   - Covered try/except, finally, raise, custom exceptions, multiple except blocks, exception chaining, and nested try usage.
2. **Complete Explanations for All Concepts Used:**  
   - We introduced each concept (and typical exceptions) before showing them in exercises.
3. **7–8 Exercises Provided (We Provided 8):**  
   - Each focusing on different aspects of exception handling and real-world usage.
4. **Starter Code in Each Exercise:**  
   - Each includes `# Save as: ...` code blocks with `main()` or function definitions.
5. **Reference Solutions & Sample Autotest:**  
   - Provided solutions for each exercise, plus a sample test script for Exercise 1.
6. **Consistent Filenames:**  
   - `session9_exX_<short_name>.py`, `_sol.py`, `_test.py`.
7. **Links to Official Docs or Trusted Resources:**  
   - Python docs on errors/exceptions, Real Python references included.
8. **No Unexplained Concepts:**  
   - All exception handling features are introduced first.
9. **Self-Contained:**  
   - Explanations → Exercises → Solutions → Autotests → Resources all in one place.

**End of Session 9 Materials**