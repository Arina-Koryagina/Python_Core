f = open("task_planner.txt", "r")
tasks = [[t for t in task.replace('\n', '').split(";")] for task in f.readlines()]
f.close()

def maxLength(t: list):  # finding the longest task name
    maxLen = len(t[0][0])
    for i in range(len(t)):
        if len(t[i][0]) > maxLen:
            maxLen = len(t[i][0])
    return maxLen

def formatDate(d: list):  # turning ['yyyy-mm-dd'] date into [['yyyy'], ['mm'], ['dd']]
    the_dates = []
    for el in d:
        the_dates.append(el.split('-'))
    for i in range(len(the_dates)):
        for j in range(3):
            the_dates[i][j] = int(the_dates[i][j])
    return the_dates

def printTasks(t: list, d: list):  # printing tasks into table
    maxLen = maxLength(t)
    print("Name".center(maxLen+2) + "|  dd/mm/yyyy" + "  |  " + "lvl")  # header
    print("-"*((maxLen+2)+23))
    for i in range(len(t)):
        print(t[i][0].ljust(maxLen+1), end=' |  ')
        print(f"{str(d[i][2]).zfill(2)}/{str(d[i][1]).zfill(2)}/{d[i][0]}", end='  |  ')
        print(t[i][2].rjust(2))
    print()

def sort(t: list, mode: int):  # sort by
    if mode == 1:  # name
        name = [el[0] for el in t]
        n = name[0][0].lower()
        for j in range(len(name)):
            for i in range(len(name)-1-j):
                if ord(n) > ord(name[i][0]):
                    n = name[i][0].lower()
                    name[i], name[i+1] = name[i+1], name[i]
                    t[i], t[i+1] = t[i+1], t[i]
    if mode == 2:  # date
        date = [el[1] for el in t]
        date = formatDate(date)
        d = date[0]
        for j in range(len(date)):
            for i in range(len(date)-1-j):
                if d[0] < date[i+1][0]:
                    d = date[i+1]
                    date[i], date[i+1] = date[i+1], date[i]
                    t[i], t[i+1] = t[i+1], t[i]
                elif d[1] < date[i+1][1]:
                    d = date[i+1]
                    date[i], date[i+1] = date[i+1], date[i]
                    t[i], t[i+1] = t[i+1], t[i]
                elif d[2] < date[i+1][2]:
                    d = date[i+1]
                    date[i], date[i+1] = date[i+1], date[i]
                    t[i], t[i+1] = t[i+1], t[i]
    if mode == 3:  # level of importance
        lvl = [el[2] for el in t]
        for j in range(len(lvl)):
            for i in range(len(lvl)-1-j):
                if lvl[i] < lvl[i+1]:
                    lvl[i], lvl[i+1] = lvl[i+1], lvl[i]
                    t[i], t[i+1] = t[i+1], t[i]
    return t

def menu():  # question menu
    return int(input('"1" to add a task\n'
                     '"2" to delete a task\n'
                     '"3" to edit a task\n'
                     '"4" to sort tasks\n'
                     '"5" to save and exit\n'
                     'Enter: '))

def edit_handler(mode: int, name, date, lvl):
    if mode == 1:
        name = input("Task's new name? ")
    if mode == 2:
        date = input("When to complete (yyyy-mm-dd)? ")
    if mode == 3:
        lvl = input("How important is it (1 - least, 3 - most)? ")
    else:
        name = input("Task's new name? ")
        date = input("When to complete (yyyy-mm-dd)? ")
        lvl = input("How important is it (1 - least, 3 - most)? ")
    return [name, date, lvl]

def menu_handler(t: list, m: int):
    the_name = [el[0] for el in t]
    if m == 1:
        name = input("Task's name? ")
        date = input("When to complete (yyyy-mm-dd)? ")
        lvl = input("How important is it (1 - least, 3 - most)? ")
        t.append([name, date, lvl])
    if m == 2:
        task = input("Enter the name of a task you want to delete (pls check for mistakes!!): ")
        try:
            t.pop(the_name.index(task))
        except ValueError:
            task = input("Enter the name of a task you want to delete (pls check for mistakes!!): ")
            t.pop(the_name.index(task))
    if m == 3:
        task = input("What's the name of the task you want to edit (pls check for mistakes!!)? ")
        edit_mode = int(input('"1" - Name\n'
                              '"2" - Date\n'
                              '"3" - Level\n'
                              '"4" - Whole\n'
                              'What to you want to edit: '))
        inx = the_name.index(task)
        t.pop(inx)
        t.insert(inx, edit_handler(edit_mode, t[inx][0], t[inx][1], t[inx][2]))
    if m == 4:
        mode = int(input('"1" - Name\n'
                         '"2" - Date\n'
                         '"3" - Level\n'
                         'Sort by: '))
        t = sort(tasks, mode)
    print("Done!")
    return t

print("Welcome! Here are your tasks:")
printTasks(tasks, formatDate([el[1] for el in tasks]))
m = menu()
while m != 5:
    tasks = menu_handler(tasks, m)
    print()
    printTasks(tasks, formatDate([el[1] for el in tasks]))
    m = menu()
if m == 5:
    print("Thank you for using our task planner!")
    lines = []
    for i in range(len(tasks)):
        if i+1 == len(tasks):
            lines.append(';'.join(str(i) for i in tasks[i]))
        else:
            lines.append(';'.join(str(i) for i in tasks[i])+'\n')
    f = open("task_planner.txt", "w")
    f.write(''.join(lines))
    f.close()
    print("Saved.")
