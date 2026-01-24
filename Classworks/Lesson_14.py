# def starLine():
#     for i in range(20):
#         print("*", end=' ')
#     print()
#
# starLine()
#
# starLine()

# def summ(a, b):
#     c = a + b
#     return c
#
# c = summ(3, 5)
# print(c)

# def even_number(n):
#     if n % 2 == 0:
#         return f"{num} is even."
#     else:
#         f"{num} is not even."
#
# print(even_number(42))

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# def isEven(num):
#     return num % 2 == 0
#
# print(isEven(42))

# def numCheck(num):
#     if num > 10:
#         return True, True
#     elif num > 0 and num <= 10:
#         return True, False
#     else:
#         return False, False
#
# print(numCheck(10))

# def isPositive(num):
#     return num > 0
# def MultipleOf(num, a):
#     return num % a == 0
#
# print(isPositive(10), MultipleOf(10, 2))

# def printLine(rang, symb):
#     for i in range(rang):
#         print(symb, end='')
#     print()
#
# printLine(20, "#")

# nums = [2, 3, 4, 6, 7, 8, 9, 0, 0, "hello"]
# int_nums = []

# for i in nums:
#    if i is int:
#        int_nums.append(i)
# print(int_nums)
# lenth = len(int_nums) * 2
# lenth = 0
# for i in nums:
#    if i is not int:
#        lenth += len(i)
#    else: lenth += i
# def starLine(symb: str, count: int):
#    for i in range(count):
#        print(symb, end='')
#    print()
#
# nums = [12, -3, 34, -455]#
#
# lenth = 0
# for i in nums:
#    lenth += len(str(i))
#
# lenth = lenth - 1 + len(nums)
#
# starLine("*", lenth)
# for i in nums:
#    print(i, end=' ')
# print()
# starLine("*", lenth)

num_a = int(input("a = "))
num_b = int(input("b = "))
num_c = int(input("c = "))
num_d = int(input("d = "))


def the_summ(a, b, c=0, d=0):
    return a + b + c + d


print(the_summ(num_a, num_b, num_c, num_d))
