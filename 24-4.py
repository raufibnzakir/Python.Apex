def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")