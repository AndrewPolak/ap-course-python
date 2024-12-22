```bash
# Run this command to create all required files for Session 7.
touch session7_ex1_basic_functions.py session7_ex1_basic_functions_sol.py session7_ex1_basic_functions_test.py \
session7_ex2_docstrings.py session7_ex2_docstrings_sol.py session7_ex2_docstrings_test.py \
session7_ex3_parameters.py session7_ex3_parameters_sol.py session7_ex3_parameters_test.py \
session7_ex4_function_scope.py session7_ex4_function_scope_sol.py session7_ex4_function_scope_test.py \
session7_ex5_default_args.py session7_ex5_default_args_sol.py session7_ex5_default_args_test.py \
session7_ex6_multiple_returns.py session7_ex6_multiple_returns_sol.py session7_ex6_multiple_returns_test.py \
session7_ex7_utilities.py session7_ex7_utilities_sol.py session7_ex7_utilities_test.py \
session7_ex8_refactor.py session7_ex8_refactor_sol.py session7_ex8_refactor_test.py
```

---

# **Session 7: Structuring Code with Functions & Scope**

## **Detailed Explanations**

In this session, we move from basic statements and data structures to **modular, reusable code** using **functions**. Well-structured code saves time, reduces errors, and makes it easier to read, maintain, and test. We'll cover:

1. **Defining Functions** with `def`
2. **Parameters** (positional, keyword, default arguments)
3. **Return Values** (including multiple returns)
4. **Scope** (local vs. global)
5. **Docstrings** (documenting what functions do)
6. **Refactoring Repetitive Code** into utility functions

By mastering these topics, you’ll write more organized Python programs and avoid repeating yourself.

---

### **1. Defining Functions**

A **function** in Python is created with the `def` keyword followed by a name, parentheses (potentially with parameters), and a colon. Indented code under the definition forms the function’s body.

```python
def greet_user():
    print("Hello, user!")
```
To call (execute) this function:
```python
greet_user()
```

#### **Parameters & Arguments**

- **Parameters** are the variable names in the function definition.
- **Arguments** are the actual values passed in when calling the function.

Example:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # "Hello, Alice!"
```

---

### **2. Return Values**

Functions can return values with `return`. If no `return` is specified, the function returns `None`.

```python
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

You can return **multiple values** in Python by returning a tuple:
```python
def divmod(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divmod(13, 5)  # q=2, r=3
```

---

### **3. Scope (Local vs. Global)**

Variables inside a function have **local scope** by default:
```python
def demo_scope():
    x = 10  # local variable
    print(x)

demo_scope()
print(x)  # Error! x is not defined outside the function.
```
**Global scope** variables are defined at the top level (outside all functions). You can read global variables inside a function, but if you want to modify them, use the `global` keyword (generally discouraged except for specific cases).

**Why Scope Matters**:

- Keeps code from interfering with each other (local variables won't clash with variables from other parts of the program).
- Encourages modular, maintainable design.

---

### **4. Default & Keyword Arguments**

You can provide **default values** for parameters. If no argument is passed for that parameter, the default is used:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Bob")   # "Hello, Bob!"
greet()        # "Hello, Guest!"
```

**Keyword arguments** let you specify arguments by name, making code more readable and flexible:
```python
def multiply(x, y=1):
    return x * y

print(multiply(y=5, x=2))  # 10
```

---

### **5. Docstrings**

A **docstring** documents what your function does, what parameters it accepts, and what it returns. By convention, it’s enclosed in triple quotes immediately after the `def` line.

```python
def greet(name="Guest"):
    """
    Print a greeting to the user.

    :param name: The name of the user as a string.
    """
    print(f"Hello, {name}!")
```

Developers can then use `help(greet)` or IDE features to see this documentation.

---

### **6. Refactoring Repetitive Code**

If you find repeated snippets of code, wrap them into a function. This eliminates duplication, making changes easier and less error-prone. Example:

**Before**:
```python
username = input("Enter username: ")
if len(username) < 3:
    print("Username too short!")
# ...
name2 = input("Enter another name: ")
if len(name2) < 3:
    print("Name too short!")
```

**After**:
```python
def validate_length(s, min_len=3):
    if len(s) < min_len:
        print("Too short!")
    else:
        print("Okay.")

username = input("Enter username: ")
validate_length(username)
name2 = input("Enter another name: ")
validate_length(name2)
```

---

## **Exercises**

Below are **8** exercises to practice various aspects of functions, parameters, scope, docstrings, and refactoring. Each exercise has:

1. A **Description**  
2. **Example Input/Output** if relevant  
3. **Starter Code**  

Reference solutions and an example autotest script follow.

---

### **Exercise 1: Basic Functions**

**Description:**  
Write a function `greet_user()` that:

1. Prompts for a username.
2. Prints `"Hello, <username>!"`.

**Example Interaction:**
```
Enter username: Alice
Hello, Alice!
```

**Starter Code:**
```python
# Save as: session7_ex1_basic_functions.py
def greet_user():
    # TODO:
    # 1. Prompt for username (input).
    # 2. Print "Hello, <username>!".
    pass

def main():
    # Call greet_user() here
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 2: Docstrings & Function Purpose**

**Description:**  
Create a function `power(base, exponent)` that returns `base ** exponent`. Include a docstring describing the function. Test it by printing a few results (e.g., `power(2, 3) -> 8`).

**Example Output:**
```
2^3 = 8
5^2 = 25
```

**Starter Code:**
```python
# Save as: session7_ex2_docstrings.py
def power(base, exponent):
    """
    TODO: Describe what this function does, its params, and returns.
    """
    pass  # implement base ** exponent

def main():
    print(f"2^3 = {power(2, 3)}")
    print(f"5^2 = {power(5, 2)}")
    # Add more tests if you want

if __name__ == "__main__":
    main()
```

---

### **Exercise 3: Parameters & Return**

**Description:**  
Write a function `add_numbers(a, b)` that returns `a + b`. Prompt the user for two integers, call `add_numbers()`, and print the result.

**Example Interaction:**
```
Enter first number: 10
Enter second number: 5
Sum = 15
```

**Starter Code:**
```python
# Save as: session7_ex3_parameters.py
def add_numbers(a, b):
    # TODO: return sum of a and b
    pass

def main():
    # 1. Prompt for two integers
    # 2. Pass to add_numbers
    # 3. Print the result
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 4: Function Scope**

**Description:**  
Demonstrate local vs. global scope:

1. Define a global variable `counter = 0`.
2. Write a function `increment()` that does `counter += 1`.  
3. Observe the error. Fix it by either returning the new value or using `global` (explain which approach you choose and why).

**Starter Code:**
```python
# Save as: session7_ex4_function_scope.py
counter = 0

def increment():
    # TODO: increment the counter
    pass

def main():
    print(f"Initial counter: {counter}")
    increment()
    print(f"Counter after increment: {counter}")

if __name__ == "__main__":
    main()
```

---

### **Exercise 5: Default Arguments**

**Description:**  
Write a function `format_name(first_name, last_name="Doe")` that prints `"<first_name> <last_name>"`.  

- If `last_name` is not provided, default to `"Doe"`.  
- Test it with various calls in `main()`.

**Example Output:**
```
format_name("Alice", "Smith") -> "Alice Smith"
format_name("Bob") -> "Bob Doe"
```

**Starter Code:**
```python
# Save as: session7_ex5_default_args.py
def format_name(first_name, last_name="Doe"):
    # TODO: print or return the formatted "<first_name> <last_name>"
    pass

def main():
    print(format_name("Alice", "Smith"))
    print(format_name("Bob"))
    # add more tests

if __name__ == "__main__":
    main()
```

---

### **Exercise 6: Multiple Returns**

**Description:**  
Create a function `divide_and_mod(a, b)` that returns two values:  

- The integer division `a // b`  
- The remainder `a % b`

Prompt the user for `a` and `b`, call the function, then print both results.

**Example Interaction:**
```
Enter a: 13
Enter b: 5
Quotient = 2, Remainder = 3
```

**Starter Code:**
```python
# Save as: session7_ex6_multiple_returns.py
def divide_and_mod(a, b):
    # TODO: return (a//b, a%b)
    pass

def main():
    # 1. Prompt for a, b
    # 2. call divide_and_mod
    # 3. print the results
    pass

if __name__ == "__main__":
    main()
```

---

### **Exercise 7: Utility Function & Reuse**

**Description:**  
Write a utility function `is_valid_username(name, min_length=3)` that returns `True` if `len(name) >= min_length`, else `False`.  
In `main()`:

1. Prompt the user for a username.  
2. Use `is_valid_username` to check validity.  
3. Print `"Valid username"` or `"Invalid username"` accordingly.

**Starter Code:**
```python
# Save as: session7_ex7_utilities.py
def is_valid_username(name, min_length=3):
    # TODO: return True/False based on length check
    pass

def main():
    username = input("Enter username: ")
    if is_valid_username(username):
        print("Valid username")
    else:
        print("Invalid username")

if __name__ == "__main__":
    main()
```

---

### **Exercise 8: Refactor Repetitive Code**

**Description:**  
You have a program that does the following:

1. Prompts the user for 3 items.  
2. For each item, checks if the length < 2, prints `"Too short!"`, otherwise `"Okay."`.  
3. Finally prints `"Done."`.

**Goal:**  
Refactor the “length check” into a reusable function `check_length(item, min_length=2)`.

**Starter Code:**
```python
# Save as: session7_ex8_refactor.py

def main():
    # Original code (unrefactored example):
    #
    # item1 = input("Enter item #1: ")
    # if len(item1) < 2:
    #     print("Too short!")
    # else:
    #     print("Okay.")
    #
    # item2 = input("Enter item #2: ")
    # if len(item2) < 2:
    #     print("Too short!")
    # else:
    #     print("Okay.")
    #
    # item3 = input("Enter item #3: ")
    # if len(item3) < 2:
    #     print("Too short!")
    # else:
    #     print("Okay.")
    #
    # print("Done.")

    # TODO:
    # 1. Implement check_length(item, min_length=2).
    # 2. Rewrite the above logic using that function.
    pass

if __name__ == "__main__":
    main()
```

---

## **Reference Solutions**

### **session7_ex1_basic_functions_sol.py**
```python
# Save as: session7_ex1_basic_functions_sol.py

def greet_user():
    username = input("Enter username: ")
    print(f"Hello, {username}!")

def main():
    greet_user()

if __name__ == "__main__":
    main()
```

---

### **session7_ex2_docstrings_sol.py**
```python
# Save as: session7_ex2_docstrings_sol.py

def power(base, exponent):
    """
    Return base raised to exponent.
    :param base: number to be raised
    :param exponent: power to raise base by
    :return: base^exponent
    """
    return base ** exponent

def main():
    print(f"2^3 = {power(2, 3)}")
    print(f"5^2 = {power(5, 2)}")

if __name__ == "__main__":
    main()
```

---

### **session7_ex3_parameters_sol.py**
```python
# Save as: session7_ex3_parameters_sol.py

def add_numbers(a, b):
    return a + b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = add_numbers(x, y)
    print(f"Sum = {result}")

if __name__ == "__main__":
    main()
```

---

### **session7_ex4_function_scope_sol.py**
```python
# Save as: session7_ex4_function_scope_sol.py

counter = 0

def increment():
    global counter  # approach #1: use 'global' (less recommended in larger programs)
    counter += 1

def main():
    print(f"Initial counter: {counter}")
    increment()
    print(f"Counter after increment: {counter}")

if __name__ == "__main__":
    main()
```

*(Alternatively, you might return a new value from `increment()` and reassign in `main()`, avoiding `global`.)*

---

### **session7_ex5_default_args_sol.py**
```python
# Save as: session7_ex5_default_args_sol.py

def format_name(first_name, last_name="Doe"):
    return f"{first_name} {last_name}"

def main():
    print(format_name("Alice", "Smith"))  # "Alice Smith"
    print(format_name("Bob"))            # "Bob Doe"

if __name__ == "__main__":
    main()
```

---

### **session7_ex6_multiple_returns_sol.py**
```python
# Save as: session7_ex6_multiple_returns_sol.py

def divide_and_mod(a, b):
    return a // b, a % b

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    quotient, remainder = divide_and_mod(a, b)
    print(f"Quotient = {quotient}, Remainder = {remainder}")

if __name__ == "__main__":
    main()
```

---

### **session7_ex7_utilities_sol.py**
```python
# Save as: session7_ex7_utilities_sol.py

def is_valid_username(name, min_length=3):
    return len(name) >= min_length

def main():
    username = input("Enter username: ")
    if is_valid_username(username):
        print("Valid username")
    else:
        print("Invalid username")

if __name__ == "__main__":
    main()
```

---

### **session7_ex8_refactor_sol.py**
```python
# Save as: session7_ex8_refactor_sol.py

def check_length(item, min_length=2):
    if len(item) < min_length:
        print("Too short!")
    else:
        print("Okay.")

def main():
    item1 = input("Enter item #1: ")
    check_length(item1)

    item2 = input("Enter item #2: ")
    check_length(item2)

    item3 = input("Enter item #3: ")
    check_length(item3)

    print("Done.")

if __name__ == "__main__":
    main()
```

---

## **Autotest Example**

Below is a sample autotest script for **Exercise 1**. It demonstrates how to run both the reference solution and the student solution, compare outputs, and handle user input. For other exercises, you’d create similar test files.

```python
# Save as: session7_ex1_basic_functions_test.py
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
    test_input = "Alice\n"
    ref_output = run_solution(reference_solution_file, test_input)
    student_output = run_solution(student_solution_file, test_input)

    if len(ref_output) != len(student_output):
        raise AssertionError(
            f"Line count mismatch. Expected {len(ref_output)} lines, got {len(student_output)}."
        )

    for i, (r_line, s_line) in enumerate(zip(ref_output, student_output)):
        if r_line != s_line:
            raise AssertionError(
                f"Mismatch on line {i+1}:\n"
                f"Expected: {r_line}\n"
                f"Got:      {s_line}"
            )

    print("All tests passed for session7_ex1_basic_functions.")

if __name__ == "__main__":
    test_solutions("session7_ex1_basic_functions.py", "session7_ex1_basic_functions_sol.py")
```

*(You’d adapt the input logic or comparisons for each exercise. For instance, if an exercise prompts for multiple inputs, or prints multiple lines, you’d expand the test cases accordingly.)*

---

## **Additional Resources**

- [Python Functions Tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
- [Docstrings & PEP 257](https://peps.python.org/pep-0257/)  
- [Real Python: Python Functions 101](https://realpython.com/defining-your-own-python-function/)  

These links provide more advanced examples, style guidelines, and best practices for organizing functions.

---

## **Final Checklist**

1. **Detailed, Substantive Explanations:**  
   - Covered how to define functions, scope, parameters, returns, docstrings, and refactoring.

2. **All Concepts Used in Exercises Explained First:**  
   - Yes, we introduced function fundamentals before the exercises.

3. **7–8 Exercises (We Provided 8):**  
   - Basic function, docstrings, parameters, scope, default arguments, multiple returns, utility usage, refactoring.

4. **Starter Code in Each Exercise:**  
   - Every exercise block includes `# Save as: ...` and `TODO` comments.

5. **Reference Solutions & Autotests:**  
   - Provided solutions for each exercise. Sample autotest script shown for Exercise 1.

6. **Consistent Filenames:**  
   - `session7_ex<number>_<short_name>.py` plus `_sol.py` and `_test.py`.

7. **Links to Official Docs:**  
   - Provided Python docs for functions, docstrings, and Real Python references.

8. **No Unexplained Concepts:**  
   - All function/parameter/return concepts are explained.

9. **Self-Contained:**  
   - Explanations → Exercises (with starter code) → Solutions → Example test → Additional resources all included.

**End of Session 7 Materials**