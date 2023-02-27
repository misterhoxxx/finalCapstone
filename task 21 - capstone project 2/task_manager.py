import datetime


# ====Login Section====

users = []
with open("user.txt", "r") as user:
    for line in user.readlines():
        username = line.split(",")[0].strip()
        password = line.split(",")[1].strip()
        users.append({"username": username, "password": password})


user_logged_in = False

while not user_logged_in:
    username = input("enter your username here: ").lower()
    password = input("enter a valid password here: ").lower()
    for user in users:
        if user["username"] == username and user["password"] == password:
            user_logged_in = True
    if not user_logged_in:
        print("details incorrect please try again")
print("successfully logged in")

while True:
    if username == "admin":
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        ds - view stats
        e - Exit
        : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

    if menu == 'r':

        with open("user.txt", "a") as file:
            user = input("enter your username here: ").lower().strip()
            password = input("enter your password here: ").strip()
            password1 = input("re-enter the password: ").strip()
            password_confirmed = password == password1
            if password_confirmed:
                file.writelines(["", f"{user}, {password}\n"])
            else:
                print("passwords do not mathc, try again!!")

    elif menu == 'a':

        with open("tasks.txt", "a") as file:
            user = input("who is the task assigned to: ")
            task_title = input("what is the task: ")
            task_description = input("describe the task here: ")
            date_due = input("due date in DD/MM/YYYY: ")
            status = input("is the task complete, (yes/no): ")
            today = datetime.date.today()
            file.writelines(["", f"{user}, {task_title}, {task_description}, {date_due}, {status}, {today}\n"])

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    with open("tasks.txt", "r") as file:
        data = file.read()
        tasks = data.split("\n")

        for task in tasks:
            task_info = task.split(",")
            if len(task_info) < 6:
                continue
            assigned_to = task_info[0]
            task_name = task_info[1]
            task_description = task_info[2]
            date_assigned = task_info[3]
            due_date = task_info[4]
            status = task_info[5]

            print("Task:\t\t\t\t\t" + task_name)
            print("Assigned to:\t\t\t" + assigned_to)
            print("Date assigned:\t\t\t" + date_assigned)
            print("Due Date:\t\t\t\t" + due_date)
            print("Task complete? \t\t\t" + status)
            print("Task description:\t\t" + task_description)

    if menu == 'vm':

        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(", ")
            assigned_to = data[0]
            task = data[1]
            task_description = data[2]
            date_assigned = data[3]
            due_date = data[4]
            task_complete = data[5]

            if assigned_to == user_logged_in:
                print("Task:\t\t\t\t\t" + task)
                print("Assigned to:\t\t\t" + assigned_to)
                print("Date assigned:\t\t\t" + date_assigned)
                print("Due Date:\t\t\t\t" + due_date)
                print("Task complete? \t\t\t" + task_complete)
                print("Task description:\t\t" + task_description)

    elif menu == 'ds':

        with open("user.txt", "r") as file:
            users = file.readlines()
            number_of_users = len(users)
        print("the number of users is:", number_of_users)

        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            number_of_tasks = len(tasks)
        print("the total number of tasks is:", number_of_tasks)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


# format the file so only user admin can register users
with open("user.txt", "r") as file:
    lines = file.readlines()
    first_line = lines[0].strip()

with open("user.txt", "w") as file:
    file.write(first_line)

# hi have made the changes, please get back to me with any further corrections.


