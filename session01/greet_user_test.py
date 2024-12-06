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
