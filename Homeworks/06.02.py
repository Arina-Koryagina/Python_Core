import random

# I
print("\t\tI")
# Напишіть функцію, що обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається з функції.

the_list = [random.randint(2, 6) for i in range(4)]
print(f"The list: {the_list}")

def multProd(l: list):
    res = 1
    for i in l:
        res *= i
    return res

print(f"Multiple product: {multProd(the_list)}")

# II
print("\n\t\tII")
# Напишіть функцію для знаходження мінімуму в списку цілих.
# Список передається як параметр. Отриманий результат повертається з функції.

the_list = [random.randint(2, 42) for i in range(8)]
print(f"The list: {the_list}")

def minVal(l: list):
    value = l[0]
    for i in l:
        if i < value:
            value = i
    return value

print(f"Minimal number: {minVal(the_list)}")

# III
print("\n\t\tIII")
# Напишіть функцію, що визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається з функції.

the_list = [random.randint(2, 12) for i in range(10)]
print(f"The list: {the_list}")

def primeNum(l: list):
    n = 0
    for i in l:
        if i == 2 or i == 3 or i == 5 or i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            n += 1
    return n

print(f"Amount of prime numbers: {primeNum(the_list)}")

# IV
print("\n\t\tIV")
# Напишіть функцію, що видаляє зі списку цілих деяке задане число.
# З функції потрібно повернути кількість видалених елементів.

to_delete = int(input("Enter a number (2-6): "))
the_list = [random.randint(2, 6) for i in range(8)]
print(f"The list: {the_list}")

def exclude(to_del: int, l: list):
    n = 0
    for i in l:
        if i == to_del:
            l.remove(i)
            n += 1
    return n

print(f"Amount of deleted elements: {exclude(to_delete, the_list)}")

# V
print("\n\t\tV")
# Напишіть функцію, яка отримує два списки як параметр
# і повертає список, що містить елементи обох списків

list_1 = [random.randint(1, 9) for i in range(6)]
list_2 = [random.randint(1, 9) for i in range(6)]
print(f"List 1: {list_1}\nList 2: {list_2}")

def intersect(l1: list, l2: list):
    l = []
    for i in l1:
        if i in l2 and i not in l:
            l.append(i)
    return l

print(f"Intersection of lists: {intersect(list_1, list_2)}")

# VI
print("\n\t\tVI")
# Напишіть функцію, що вираховує ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список теж передається як параметр.
# Функція повертає новий список, що містить отримані результати.

degree = int(input("Enter a degree: "))
the_list = [random.randint(2, 9) for i in range(8)]
print(f"The list: {the_list}")

def countDegree(d: int, l: list):
    the_l = []
    for i in l:
        the_l.append(i**d)
    return the_l

print(f"List with numbers in a {degree} degree: {countDegree(degree, the_list)}")
