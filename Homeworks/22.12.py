import random
n = 15

#  I
print("\t\tI")
# Користувач з клавіатури вводить список цілих чисел.
# Необхідно визначити кількість елементів у списку,
# які більші за попередній елемент. Результат вивести на екран.

array = [random.randint(0, 10) for i in range(n)]
print(f"The array: {array}")
amount = 0
for i in range(n-1):
    if array[i] < array[i+1]:
        amount += 1
print(f"The amount of numbers greater than the previous one is: {amount}.")

#  II
print("\t\tII")
# Користувач вводить список цілих чисел.
# Необхідно вивести тільки ті елементи, які
# зустрічаються у списку рівно один раз,
# зберігаючи порядок їхньої появи.

array = [random.randint(0, 10) for i in range(n)]
print(f"The array: {array}")
new_list = []
for el in array:
    if array.count(el) == 1:
        new_list.append(el)
print(f"Only unique elements: {new_list}")

#  III
print("\t\tIII")
# Користувач з клавіатури вводить список чисел.
# Необхідно знайти у списку найдовшу послідовність
# елементів, що зростають, і вивести її довжину та самі елементи.

array = [random.randint(0, 5) for i in range(n)]
print(f"The array: {array}")
longest_sequence = []
sequence = [array[0]]
for i in range(1, n):
    if array[i] > array[i-1]:
        sequence.append(array[i])
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    else:
        sequence = [array[i]]
print(f"The longest sequence of increasing elements is: {len(longest_sequence)}.\nThe sequence: {longest_sequence}")

#  IV
print("\t\tIV")
# Користувач із клавіатури вводить список цілих чисел.
# Необхідно реалізувати циклічний зсув списку вправо
# на N позицій. Результат вивести на екран.

array = [random.randint(0, 10) for i in range(n)]
print(f"The array: {array}")
N = int(input("Shift for: "))
for i in range(N):
    last = array[n - 1]
    for j in range(n-1, 0, -1):
        array[j] = array[j-1]
    array[0] = last
print(f"Shifted array: {array}")

#  V
print("\t\tV")
# Два списки цілих заповнюються випадковими числами. Необхідно:
# Сформувати третій список, що містить
#   елементи обох списків;
#   елементи обох списків без повторень;
#   елементи спільні для двох списків;
#   тільки унікальні елементи кожного зі списків;
#   тільки мінімальне і максимальне значення кожного зі списків.

first_array = [random.randint(0, 10) for i in range(n)]
second_array = [random.randint(0, 10) for i in range(n)]
print(f"The I array: {first_array}")
print(f"The II array: {second_array}")

third_array = first_array.copy()
for i in range(n):
    third_array.append(second_array[i])
print(f"Elements of both: {third_array}")

new_list = []
for el in third_array:
    if el not in new_list:
        new_list.append(el)
new_list.sort()
print(f"Unique elements of both: {new_list}")

third_array.sort()
new_list = []
for el in third_array:
    if el in first_array and el in second_array:
        new_list.append(el)
third_array.clear()
for el in new_list:
    if el not in third_array:
        third_array.append(el)
third_array.sort()
print(f"Shared elements of both: {third_array}")

third_array.clear()
new_list = []
for el in first_array:
    if first_array.count(el) == 1:
        third_array.append(el)
for el in second_array:
    if second_array.count(el) == 1:
        third_array.append(el)
for el in third_array:
    if el not in new_list:
        new_list.append(el)
new_list.sort()
print(f"Unique elements of each: {new_list}")

print(f"Min/max of each: {[min(first_array), max(first_array), min(second_array), max(second_array)]}")

#  VI
print("\t\tVI")
# Користувач вводить список цілих чисел.
# Необхідно відсортувати список так, щоб числа чергувалися:
# спочатку найменше, потім найбільше, потім
# друге за величиною, друге за мінімальністю тощо.

array = [random.randint(0, 10) for i in range(n)]
new_list = []
print(f"The array: {array}")
for j in range(n-1):
    for i in range(n-1-j):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
for j in range(n//2):
    new_list.append(array[n-1-j])
    new_list.append(array[j])
if n//2 != 0:
    new_list.append(array[n//2])
print(f"Sorted array: {new_list}")
