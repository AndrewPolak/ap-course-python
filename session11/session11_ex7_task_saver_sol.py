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