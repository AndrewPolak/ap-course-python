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
