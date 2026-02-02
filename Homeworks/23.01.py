#  I
print("\t\tI")
# Напишіть функцію, яка приймає два числа як параметр і відображає
# всі парні числа між ними.

def write_final_list(start_num: int, end_num: int, num_list: list, final_list: list):
    while start_num+1 < end_num:
        start_num += 1
        num_list.append(start_num)
    for i in num_list:
        if i % 2 == 0:
            final_list.append(i)
    return final_list

def evenNumbers_find(a: int, b: int, final_list: list):
    nums_list = []
    if a > b:
        start = b
        end = a
        write_final_list(start, end, nums_list, final_list)
    elif a == b:
        print("They are the same number!")
    else:
        start = a
        end = b
        write_final_list(start, end, nums_list, final_list)
    return f"Every even number between {a_num} and {b_num}: {', '.join(str(i) for i in final_list)}."

a_num = int(input("First number: "))
b_num = int(input("Second number: "))
nums_final_list = []

print(evenNumbers_find(a_num, b_num, nums_final_list))

#  II
print("\n\t\tII")
# Напишіть функцію, яка відображає порожній або заповнений квадрат
# з деякого символу. Функція приймає як параметри: довжину сторони
# квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.

def print_symb(wide: int, symb: str, ending='  '):
    for i in range(wide):
        print(symb, end=ending)
    print()

def printRectangle(wide: int, symb: str, fill: str):
    if fill == "T": # через bool не приймає, не знаю чому. =(
        for i in range(wide):
            print_symb(wide, symb)
    else:
        print_symb(wide, symb)
        for i in range(wide - 2):
            inside_space = (len(symb) + len('  ')) * (wide - 1)
            print(symb + " " * (inside_space - 1) + symb)
        print_symb(wide, symb)


width = int(input("Enter the width of rectangle: "))
symbol = str(input("Enter the symbol: "))
filling = input("Is it filled? T/f: ").capitalize()

printRectangle(width, symbol, filling)

#  III
print("\n\t\tIII")
# Напишіть функцію, яка повертає мінімальне з п'яти чисел.
# Числа передаються як параметри

nums_list = []
num = 5

for i in range(num):
    a = float(input("Number = "))
    nums_list.append(a)

def numCount(nums: list, num_count: int):
    for j in range(num_count-1):
        for i in range(num_count-j-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums_list[0]


print(f"The minimal number out of {num}: {numCount(nums_list, num)}.")

#  IV
print("\n\t\tIV")
# Напишіть функцію, яка рахує кількість цифр у числі.
# Число передається як параметр. З функції потрібно повернути
# отриману кількість цифр.
# Наприклад, якщо передали 3456, кількість цифр буде 4.

num = int(input("Number = "))

def digitCount(number: float):
    num = number
    digit = 0
    while number > 10:
        digit += 1
        number //= 10
    else:
        digit += 1
        if number % 10 == 0:
            digit += 1
    return f"The amount of digit in {num} is {digit}."

print(digitCount(num))

#  V
print("\n\t\tV")
# Напишіть функцію, яка перевіряє чи є число паліндромом.
# Число передається як параметр. Якщо число паліндром,
# потрібно повернути з функції true, інакше false.

num = int(input("Number = "))

def is_palindrome(number: int):
    num_str = str(number)
    i = 0
    j = len(num_str) - 1
    while i < j:
        if num_str[i] != num_str[j]:
            return False
        i += 1
        j -= 1
    return True

print(f"Is the number {num} palindrom? {is_palindrome(num)}.")
