# Save as: session11_ex7_task_saver.py

def main():
    # TODO:
    # 1. tasks = []
    # 2. collect tasks until "stop"
    # 3. write them to tasks_demo.txt
    # 4. read them back, print
    tasks = []

    try:
        f = open("tasks_demo.txt", "w+")
    except FileNotFoundError as e:
        print(e)
        exit(1)
    
    while True:
        task = input("Enter a task: ").strip()
        if task == "stop":
            break
        f.write(task + '\n')
    
    f.seek(0, 0)

    task = f.readline()
    while task:
        print(task[:-1])
        task = f.readline()
    
    f.close()


if __name__ == "__main__":
    main()