import random

marks = [["Яромил"], ["Горигляд"], ["Ярополк"], ["Цвітан"], ["Наслав"], ["Іларіон"], ["Йозеф"], ["Худан"], ["Щастибог"]]
for l in marks:
    l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])

def maxLength(m):
    maxLen = len(m[0][0])
    for i in range(len(m)):
        if len(m[i][0]) > maxLen:
            maxLen = len(m[i][0])
    return maxLen

def maxMarks(m):
    maxMark = len(m[0][1:])
    for i in range(len(m)):
        if len(m[i][1:]) > maxMark:
            maxMark = len(m[i][1:])
    return maxMark

def getAvg(m):
    avg = sum(m[1:]) / (len(m) - 1)
    return round(avg, 1)

def sortStudents(m):
    n = len(m)
    for i in range(n):
        for j in range(0, n-i-1):
            if getAvg(m[j]) < getAvg(m[j + 1]):
                m[j], m[j + 1] = m[j + 1], m[j]

def printStudent(m):
    maxLen = maxLength(m)
    maxMark = maxMarks(m)
    sortStudents(m)
    for st in m:
        print(st[0].ljust(maxLen + 3), end='')
        for i in range(1, len(st)):
            print(str(st[i]).rjust(3), end=' ')
        if maxMark > len(st[1:]):
            space = " " * ((maxMark - len(st[1:])) * 4)
        else:
            space = ""
        print(f"{space}  |  {getAvg(st)}")

printStudent(marks)

###  H/W  ###

#  I
print("\n\t\tI")
# Напишіть програму, яка запитує в користувача три рядки і записує
# їх у файл data.txt, кожен рядок має бути записаний на новому рядку.

lines = input("Write the sentences: ").split(". ")  # Hello. My name is Anton. Python. Every morning I usually get up at 7 o'clock. (c)
f = open("data.txt", "w")
for i in range(len(lines)):
    if i+1 == len(lines):
        f.write(lines[i])
    else:
        f.write(lines[i] + "\n")
f.close()
print("Done.")

#  II
print("\n\t\tII")
# Напишіть програму, яка перевіряє, чи існує файл data.txt, і виводить
# відповідне повідомлення. Якщо файл існує, відкрийте його і виведіть
# кожен другий рядок у консоль.
# https://www.geeksforgeeks.org/python/check-if-a-file-exists-in-python/

from pathlib import Path

a = Path("data.txt")

if a.exists():
    print(f"File {a} exists.")
    f = open("data.txt", "r")
    s = f.readlines()
    f.close()
    for i in range(1, len(s), 2):
        print(s[i], end='')
else:
    print(f"File {a} does not exist.")

#  III
print("\n\t\tIII")
# Напишіть програму, яка читає файл data.txt, фільтрує рядки, що містять
# слово "Python", і записує їх у новий файл filtered.txt.

f = open("data.txt", "r")
s = f.readlines()
f.close()

filtered = []
for line in s:
    if "Python" not in line:
        filtered.append(line)

f = open("filtered.txt", "w")
for i in range(len(filtered)):
    f.write(filtered[i])
f.close()
print("Done.")

#  IV
print("\n\t\tIV")
# Напишіть програму, яка запитує в користувача ім'я файлу, відкриває його,
# видаляє всі цифри з вмісту і зберігає результат у новому файлі cleaned.txt.

name = input("Name of the file? ")  # nums

f = open(f"{name}.txt", "r", encoding="utf-8")
s = f.read()
f.close()

cleaned = ''.join(ch for ch in s if not ch.isdigit())
lines = []
for line in cleaned.split('\n'):
    lines.append(' '.join(line.split()))
cleaned = '\n'.join(lines)

f = open("cleaned.txt", "w", encoding="utf-8")
f.write(cleaned)
f.close()
print("Done.")

#  V
print("\n\t\tV")
# Напишіть програму, яка аналізує файл log.txt, визначає 10
# найпоширеніших слів, що зустрічаються найчастіше, і записує їх
# разом з їхньою частотою в word_stats.txt.

f = open(f"log.txt", "r")
text = f.read()
f.close()

words = text.lower().split()
the_w = []
the_f = []
for i in range(len(words)):
    w = words[i].strip(".,!?;:-()[]{}\"'")
    if w not in the_w:
        the_w.append(w)
for w in the_w:
    freq = 0
    for i in range(len(words)):
        if w == words[i].strip(".,!?;:-()[]{}\"'"):
            freq += 1
    the_f.append(freq)

for j in range(len(the_f)-1):
    for i in range(len(the_f)-1-j):
        if the_f[i] < the_f[i+1]:
            the_f[i], the_f[i+1] = the_f[i+1], the_f[i]
            the_w[i], the_w[i + 1] = the_w[i + 1], the_w[i]

f = open("word_stats.txt", "w", encoding="utf-8")
for i in range(10):
    if i == 9:
        f.write(f"{i + 1}. {the_w[i]}: {the_f[i]}")
    else:
        f.write(f"{i+1}. {the_w[i]}: {the_f[i]}\n")
f.close()
print("Done.")

#  VI
print("\n\t\tVI")
# Напишіть програму, яка читає файл data.txt, інвертує порядок рядків
# і зберігає результат у новому файлі reversed.txt.

f = open("data.txt", "r")
s = f.readlines()
f.close()

s.reverse()
for i in range(len(s)):
    s[i] = s[i].strip("\n")

f = open("reversed.txt", "w")
for i in range(len(s)):
    if i+1 == len(s):
        f.write(s[i])
    else:
        f.write(s[i] + "\n")
f.close()
print("Done.")
