# import random
#
# marks = [["Яромил"], ["Горигляд"], ["Ярополк"], ["Цвітан"], ["Наслав"], ["Іларіон"], ["Йозеф"], ["Худан"], ["Щастибог"]]
# for l in marks:
#     l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])
#
# f = open("marks.txt", 'w', encoding='utf-8')
# for i in range(len(marks)):
#     for j in range(len(marks[i])):
#         f.write(''.join(str(marks[i][j])+' '))
#     if i+1 < len(marks):
#         f.write('\n')

f = open("marks.txt", 'r', encoding='utf-8')
marks = [i.split() for i in f.read().split('\n')]
f.close()
for j in range(len(marks)):
    for i in range(len(marks[j])-1):
        marks[j][i+1] = int(marks[j][i+1])

def maxLength(m: list):
    maxLen = len(m[0][0])
    for i in range(len(m)):
        if len(m[i][0]) > maxLen:
            maxLen = len(m[i][0])
    return maxLen

def maxMarks(m: list):
    maxLen = len(m[0][1:])
    for i in range(len(m)):
        if len(m[i][1:]) > maxLen:
            maxLen = len(m[i][1:])
    return maxLen

def getAvg(m: list):
    avg = sum((m[1:])) / (len(m) - 1)
    return round(avg, 1)

def sortStudents(m: list):
    n = len(m)
    for j in range(n):
        for i in range(0, n-j-1):
            if getAvg(m[i]) < getAvg(m[i + 1]):
                m[i], m[i+1] = m[i+1], m[i]

def printStudent(m: list):
    maxLen = maxLength(m)
    maxMark = maxMarks(m)
    print("Names".center(maxLen+7) + "|" + "Marks".center((maxMark+1)*4) + "|" + "  Average")
    print("-"*(maxLen+(maxMark*4)+24))
    for i in range(len(m)):
        print(f"{i+1}".rjust(2), end='. ')
        print(m[i][0].ljust(maxLen+3), end='|  ')
        for j in range(1, len(m[i])):
            print(str(m[i][j]).rjust(3), end=' ')
        if maxMark > len(m[i][1:]):
            space = " " * ((maxMark - len(m[i][1:])) * 4)
        else:
            space = ""
        if getAvg(m[i]) < 10:
            avg = " "
        else:
            avg = ""
        print(f"{space}  |   {avg}{getAvg(m[i])}")

sortStudents(marks)
printStudent(marks)

def task_q():
    return int(input("\n1 - Add new mark\n2 - Delete the mark\n3 - Edit the mark\n4 - Save\nWhat would you like to do? Enter just the number: "))

task = task_q()
while task < 4:
    student = int(input("Enter the student's number: "))
    if task == 1:
        new_mark = int(input("Enter new mark: "))
        marks[student-1].append(new_mark)
        print("Done.")
        task = task_q()
    if task == 2:
        mark_delete = int(input("Enter mark to delete (index): "))
        marks[student-1].pop(mark_delete)
        print("Done.")
        task = task_q()
    if task == 3:
        mark_edit = int(input("Enter mark to edit (index): "))
        new_mark = int(input("Enter new mark: "))
        marks[student-1].pop(mark_edit)
        marks[student-1].insert(mark_edit, new_mark)
        print("Done.")
        task = task_q()
else:
    f = open("marks.txt", 'w', encoding='utf-8')
    for i in range(len(marks)):
        for j in range(len(marks[i])):
            f.write(''.join(str(marks[i][j])+' '))
        if i+1 < len(marks):
            f.write('\n')
    print("Saved.\n")
    sortStudents(marks)
    printStudent(marks)

