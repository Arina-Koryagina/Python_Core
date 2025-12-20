import random
n = 10

#  I
print("\t\tI")
# Користувач з клавіатури вводить елементи списку цілих.
# Необхідно порахувати суму всіх елементів та
# їхнє середньоарифметичне. Результати вивести на екран.

nums = [random.randint(0, 10) for i in range(n)]
print(f"The list: {nums}")
print(f"Sum of the elements: {sum(nums)}, arithmetic mean: {sum(nums) / n}.")


#  II
print("\t\tII")
# Користувач з клавіатури вводить елементи списку цілих і деяке число.
# Необхідно порахувати скільки разів дане число присутнє у списку.
# Результат вивести на екран.

row = list((input(f"Print numbers in a row (without spaces): ")))
number = input("Print the number to be found: ")
t = 0
for el in row:
    if el == number:
        t += 1
print(f"There are {t} of {number}.")


#  III
print("\t\tIII")
# Користувач з клавіатури вводить список чисел.
# Необхідно знайти суму всіх додатних чисел у списку.
# Результат вивести на екран.

nums = [random.randint(-5, 5) for a in range(n)]
sumN = 0
print(f"The list: {nums}")
for el in nums:
    if el > 0:
        sumN += el
print(f"The sum of all the positive numbers: {sumN}.")


#  IV
print("\t\tIV")
# Користувач з клавіатури вводить список цілих чисел.
# Необхідно визначити індекси всіх парних чисел у списку.
# Результат вивести на екран.

nums = [random.randint(0, 10) for b in range(n)]
print(f"The list: {nums}")
print("The indexes of even numbers are:", end=' ')
for b in range(n):
    if nums[b] % 2 == 0:
        print(b, end=' ')


#  V
print("\n\t\tV")
# Користувач з клавіатури вводить список цілих чисел.
# Необхідно видалити зі списку всі елементи, що повторюються,
# залишивши тільки унікальні. Результат вивести на екран.

nums = [random.randint(0, 10) for c in range(n)]
print(f"The list: {nums}")
new_list = []
for el in nums:
    if el not in new_list:
        new_list.append(el)
print(f"New list (only unique numbers): {new_list}")
