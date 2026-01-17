#  I
print("\t\tI")
# Користувач вводить з клавіатури арифметичний вираз.
# Наприклад, 23+12.
# Необхідно вивести на екран результат виразу.
# У нашому прикладі це 35.
# Арифметичний вираз може складатися тільки з трьох частин:
# число, операція, число. Можливі операції: +, -, *, /.

equation = input("Enter the equation: ")
operations = ["+", "-", "*", "/"]

for i in operations:
    if i in equation:
        numbers = equation.split(i)
        a = int(numbers[0])
        b = int(numbers[1])
        print("The answer is", end=' ')
        if i == "+":
            print(a + b)
        elif i == "-":
            print(a - b)
        elif i == "*":
            print(a * b)
        elif i == "/":
            print(a / b)

#  II
print("\n\t\tII")
# Користувач вводить з клавіатури деякий текст.
# У програмі визначено набір зарезервованих слів.
# Необхідно знайти в тексті всі зарезервовані слова
# і змінити їхній регістр на верхній. Вивести на екран змінений текст.

import string
# замість вводу
text = ("Crowley was currently doing 110 mph somewhere east of Slough. Nothing about him looked "
        "particularly demonic, at least by classical standards. No horns, no wings. Admittedly he was listening to "
        "a Best of queen tape, but no conclusions should be drawn from this because all tapes left in a car for "
        "more than about a fortnight metamorphose into Best of Queen albums. No particularly demonic thoughts "
        "were going through his head. In fact, he was currently wondering vaguely who Moey and Chandon "
        "were. \n"
        "crowley had dark hair and good cheekbones and he was wearing snakeskin shoes, or at least "
        "presumably he was wearing shoes, and he could do really weird things with his tongue. And, whenever "
        "he forgot himself, he had a tendency to hiss. \n"
        "He also didn't blink much. \n"
        "The car he was driving was a 1926 black Bentley, one owner from new, and that owner had been "
        "Crowley. He'd looked after it. \n"
        "The reason he was late was that he was enjoying the twentieth century immensely. It was much "
        "better than the seventeenth, and a lot better than the fourteenth. One of the nice things about Time, "
        "Crowley always said, was that it was steadily taking him further away from the fourteenth century, the "
        "most bloody boring hundred years on God's, excuse his French, Earth. The twentieth century was "
        "anything but boring. In fact, a flashing blue light in his rearview mirror had been telling crowley, for the "
        "last fifty seconds, that he was being followed by two men who would like to make it even more "
        "interesting for him. ")  # (C) Good Omens
words_reserved = ["Crowley", "Queen", "Bentley", "Earth"]
words = text.split()
the_text = []

for w in words:
    word = w.strip(string.punctuation)
    if word.lower() in [w.lower() for w in words_reserved]:
        w = w.replace(word, word.upper())
    the_text.append(w)

print(" ".join(the_text))

#  III
print("\n\t\tIII")
# Користувач вводить рядок і два символи.
# Видаліть із рядка всі символи між першим входженням
# першого символу і першим входженням другого символу,
# включаючи самі символи. Виведіть результат.

promt = input("Enter a sentence and two symbols (devided by spaces): ")

words = promt.split()
words = [w.strip() for w in words]
first_symbol = words[len(words)-2]
second_symbol = words[len(words)-1]
the_promt = " ".join(words[0:len(words)-2])
start = the_promt.find(first_symbol)
end = the_promt.find(second_symbol)
result = ""

for s in range(len(the_promt)):
    if s < start or s > end:
        result += the_promt[s]

print(result)
