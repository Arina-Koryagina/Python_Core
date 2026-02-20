# f = open("text.txt", "w", encoding='utf-8')
# f.write("Слава Україні!")
# f.close()

# f = open("text.txt", "r")
# # s = f.read()
# # s = f.readline()
# s = f.readlines()
# print(s)
# f.close()

# import random

# arr = [random.randint(1, 50) for i in range(30)]
# print(arr)
#
# f = open("arr.txt", "w")
# f.write(" ".join([str(i) for i in arr]))
# f.close()

# f = open("arr.txt", "r")
# s = f.read().split()
# arr = [int(i) for i in s]
# print(arr[4])

# arr_w = ""
# for i in arr:
#     arr_w += str(i) + " "
#
# f = open("arr.txt", "w")
# f.write(arr_w)
# f.close()
# f = open("arr.txt", "r")
# l = f.read().split(" ")
# l.pop(-1)
# l = [int(i) for i in l]
# print(l)
# f.close()

# f = open("arr.txt", "r")
# s = f.read().split()
# # arr = [int(i) for i in s]
# arr = list(map(int, s))
# f.close()
#
# arr2 = [i for i in arr if i % 2 == 0]
# # for i in arr:
# #     if i % 2 == 0:
# #         arr2.append(i)
# f = open("arr2.txt", "w")
# f.write(" ".join(map(str, arr2)))
# # f.write(" ".join([str(i) for i in arr2]))
# f.close()

# f = open("test.txt", "r")
# # test = f.read().count('\n')
# lines = f.readlines()
# f.close()
#
# print(len(lines))
# words = 0
# symbols = 0
# for l in lines:
#     words += len(l.split())
#     symbols += sum(map(len, l.split()))
# print(words)
# print(symbols)

# def square(a):
#     return a * a
#
# arr = [random.randint(1, 5) for i in range(5)]
# print(arr)
# arr2 = list(map(square, arr))
# print(arr2)

s = "wxyzabcd"
m = ""
n = 3
for i in s:
    if ord(i) + n > ord("z"):
        m += chr(ord(i) + n - 26)
    else:
        m += chr(ord(i) + n)

print(m)
