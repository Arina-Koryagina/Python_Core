import random
# def show(*args):
#     print(type(args))
#     # for el in args:
#     #     print(el)
#
# def boo(a, b):
#     return a + b


# show(12, 324, 2345, 345, 67890, "234234", True)
# print(boo(b=3, a=5))

# def foo(*args, **kwargs):
#     print(type(args, kwargs))
#     for key in kwargs:
#         print(f"Key - {key}, value - {kwargs[key]}")
#
#
# foo(2, 4, c="mama", age=20, isDay=True)

# b = boo
# print(b(3, 5))
#
#
# def printLine(symbol='*', count=10):
#     for i in range(count):
#         print(symbol, end='')
#     print()
#
#
# def func(method):
#     method()
#
#
# func(printLine)
#
#
# def hello():
#     print("Hello")
#
#
# def goodbye():
#     print("Goodbye")
#
#
# message = hello
# message()
# message = goodbye
# message()
#
# message_list = [hello, goodbye]
# for f in message_list:
#     f()
#
# nums = [12, 324, 2345, 345, 67890]
# for j in range(len(nums)-1):
#     for i in range(len(nums)-1-j):
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
# print(nums)

# def bubble_sort(_list: list, asc=True):
#     for j in range(len(_list) - 1):
#         for i in range(len(_list) - 1 - j):
#             if asc:
#                 if _list[i] > _list[i + 1]:
#                     _list[i], _list[i + 1] = _list[i + 1], _list[i]
#             else:
#                 if _list[i] < _list[i + 1]:
#                     _list[i], _list[i + 1] = _list[i + 1], _list[i]

# def asc(a, b):
#     return a > b
#
# def desk(a, b):
#     return a < b
#
# def evenFirst(a, b):
#     if a % 2 == 1 and b % 2 == 0:
#         return True
#     if a % 2 == 0 and b % 2 == 1:
#         return False
#     return asc(a, b)
#
# def firstNum(n):
#     if n < 10:
#         return n
#     n //= 10
#     return firstNum(n)
#
# def numberSort(a, b):
#     a_f, b_f = a, b
#     a, b = firstNum(a), firstNum(b)
#     if a > b:
#         return True
#     if a < b:
#         return False
#     return asc(a_f, b_f)

# def numberSort(a, b):
#     if a % 10 > b % 10:
#         return True
#     if a % 10 < b % 10:
#         return False
#     return asc(a, b)

# def bubble_sort(_list: list, method=asc):
#     for j in range(len(_list) - 1):
#         for i in range(len(_list) - 1 - j):
#             if method(_list[i], _list[i + 1]):
#                 _list[i], _list[i + 1] = _list[i + 1], _list[i]
#
# l = [random.randint(1, 100) for i in range(20)]
# print(l)
# bubble_sort(l, numberSort)
# print(l)

marks = [["Яромил"], ["Горигляд"], ["Ярополк"], ["Цвітан"], ["Наслав"], ["Іларіон"], ["Йозеф"], ["Худан"], ["Щастибог"]]
for l in marks:
    l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])

def maxLength(marks):
    maxLen = len(marks[0][0])
    for i in range(len(marks)):
        if len(marks[i][0]) > maxLen:
            maxLen = len(marks[i][0])
    return maxLen

def getAvg(marks):
    avg = sum(marks[1:]) / (len(marks) - 1)
    return round(avg, 2)

def sortStudents(marks):
    the_avg = 0
    for i in range(len(marks)):
        avg = getAvg(marks[i])
        if the_avg < avg:
            the_avg = avg
            marks[i], marks[i+1] = marks[i+1], marks[i]

def printStudent(marks):
    maxLen = maxLength(marks)
    sortStudents(marks)
    for st in marks:
        print(st[0].ljust(maxLen + 3,), end='')
        for i in range(1, len(st)):
            print(str(st[i]).rjust(3), end=' ')
        print(f"  |  {getAvg(st)}")
#
# def indBestStudent(marks):
#     iBest = 0
#     avg = 0
#     for i in range(len(marks)):
#         s1 = getAvg(marks[i])
#         if s1 > avg:
#             iBest = i
#             avg = s1
#     return iBest

# def bestStudent(marks):
#     avg = 0
#     ID = 0
#     for j in range(len(marks)):
#         summ = 0
#         for i in range(1, len(marks[j])):
#             summ += i
#         summ = summ / len(marks[j])
#         if summ > avg:
#             avg = summ
#             ID = j
#     return ID
#
printStudent(marks)
print(indBestStudent(marks))
# print(bestStudent(marks))

# def marksList(_list: list):
#     for i in range(len(_list)):
#         _list.remove(_list[i][0])
#
# print(marks)
# marksList(marks)
# print(marks)
#
# maxLen = len(marks[0][0])
# for i in range(len(marks)):
#     if len(marks[i][0]) > maxLen:
#         maxLen = len(marks[i][0])
#
# for i in range(len(marks)):
#     print(marks[i][0].ljust(maxLen+3, ' ') + str(marks[i][j] for j in range(len(marks[i]))))
