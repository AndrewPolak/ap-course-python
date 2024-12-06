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
