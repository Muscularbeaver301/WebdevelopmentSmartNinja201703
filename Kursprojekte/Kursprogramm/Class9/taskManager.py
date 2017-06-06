myTasks = {}

while True:

    taskname = raw_input("Enter Taskname, or 'X' to finish: ")

    if taskname == 'X':
        break

    completed = raw_input("Task is completed? (y,n)")

    isCompleted = True if completed == 'y' else False

    myTasks[taskname] = isCompleted

print myTasks
