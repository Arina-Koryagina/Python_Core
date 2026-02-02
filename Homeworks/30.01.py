#  I
print("\t\tI")
# Написати рекурсивну функцію знаходження найбільшого спільного дільника двох цілих чисел.

def gcd_func(a: int, b: int):
    if b == 0:
        return a
    return gcd_func(b, a % b)

frst = int(input("First number: "))
scnd = int(input("Second number: "))

print(gcd_func(frst, scnd))

#  II
print("\n\t\tII")
# Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.
# Приклад:
# Введення: 123
# Виведення: 6 (оскільки 1+2+3=6).

def the_sum(n):
    ans = n % 10
    if n//10 < 10:
        return ans + n//10
    return ans + the_sum(n//10)

num = int(input("Number: "))

print(f"The sum of the digits in {num} is {the_sum(num)}.")

#  III
print("\n\t\tIII")
# Напишіть рекурсивну функцію, яка перевіряє, чи є заданий список симетричним.
# Симетричний список — це список, у якому елементи зліва направо і справа наліво збігаються.
# Приклад:
# Введення: [1,2,3,2,1]
# Висновок: "Список симетричний".

def the_check(l: list, i: int):
    if i >= len(l) - 1 - i:
        return True
    if l[i] == l[len(l) - 1 - i]:
        return the_check(l, i + 1)
    else:
        return False

def list_check(l: list):
    if the_check(l, 0):
        return "List is symmetrical."
    else:
        return "List is non symmetrical."

the_list = list(input('Enter the numbers separated by " ": ').split(' '))

print(list_check(the_list))

#  IV
print("\n\t\tIV")
# Написати гру "Бики та корови". Програма "загадує" чотирицифрове число і гравець має вгадати його.
# Після введення користувачем числа програма повідомляє, скільки цифр числа вгадано (бики) і
# скільки цифр вгадано і стоїть на потрібному місці (корови). Після відгадування числа на екран
# необхідно вивести кількість зроблених користувачем спроб. У програмі необхідно використовувати рекурсію.

def split_num(n: int, l: list):
    l.append(n % 10)
    if n // 10 < 10:
        l.append(n // 10)
        l.reverse()
        return l
    return split_num(n // 10, l)

def guess_check(l: list, num: list):
    global tries
    correct_guess_pos = []
    correct_guess = []
    num_copy = num.copy()
    for i in range(len(l)):
        if l[i] in num_copy:
            correct_guess.append(l[i])
            num_copy.remove(l[i])
        if l[i] == num[i]:
            correct_guess_pos.append(i)
    tries += 1
    return correct_guess, correct_guess_pos

def the_game(num):
    user_guess = int(input("Guess the number (1000-9999): "))
    guess = split_num(user_guess, [])
    res = guess_check(guess, num)
    if guess != num:
        print(f'Numbers guessed right: {" ".join([str(i) for i in res[0]])}.')
        print(f'Numbers in the right position: {" ".join([str(guess[i]) for i in res[1]])}, position(s): {" ".join([str(i+1) for i in res[1]])}.')
        print(f'Tries: {tries}')
        the_game(number)
    else:
        print(f"Correct! You win! Total amount of tries: {tries}.")
    return guess

import random
number_to_guess = random.randint(1000, 9999)
number = split_num(number_to_guess, [])
tries = 0

the_game(number)

#  V
print("\n\t\tV")
# Дано шахову дошку розміром 8×8 і шахового коня. Програма повинна запросити у користувача
# координати клітинки поля і поставити туди коня. Завдання програми знайти і вивести шлях
# коня, за якого він обійде всі клітинки дошки, стаючи в кожну клітину тільки один раз.
# (Оскільки процес відшукання шляху для різних початкових клітинок може затягнутися,
# то рекомендується спочатку випробувати задачу на полі розміром 6×6). У програмі необхідно використовувати рекурсію.

width = 6
board = [[i, j] for i in range(width) for j in range(width)]
moves = []
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def make_a_move(pos):
    if len(moves) == width * width:
        return True
    for x, y in knight_moves:
        next_pos = [pos[0] + x, pos[1] + y]
        if next_pos in board:
            moves.append(next_pos)
            board.remove(next_pos)
            if make_a_move(next_pos):
                return True
            board.append(next_pos)
            moves.pop()
    return False

start = input("Put in coordinates of the knight (ex. 0, 0): ").split(", ")
position = [int(start[0]), int(start[1])]
moves.append(position)
board.remove(position)

if make_a_move(position):
    print("Knight's way: ")
    print(moves)
else:
    print("Not solved.")
