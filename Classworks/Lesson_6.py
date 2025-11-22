# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# c = input("Enter the operation (+  -  *  /): ")
# res = 0
#
# # if c == "+":
# #     res = a + b
# # elif c == "-":
# #     res = a - b
# # elif c == "*":
# #     res = a * b
# # elif c == "/":
# #     res = a / b
# # else:
# #     print("Error")
#
# match c:
#     case '+': res = a + b
#     case '-': res = a - b
#     case '*': res = a * b
#     case '/': res = a / b
#     case _: print("Error")
# print(res)

# C = str(input("C (N, E, S, W) = "))
# N1 = int(input("1st = "))
# N2 = int(input("2nd = "))
# loc = 0  # N - 0, E - 1, S - 2, W - 3
# match C:
#     case 'N': loc = 0
#     case 'E': loc = 1
#     case 'S': loc = 2
#     case 'W': loc = 3
# ans = (loc + N1 + N2) % 4
# match ans:
#     case 0: ans = 'N'
#     case 1: ans = 'E'
#     case 2: ans = 'S'
#     case 3: ans = 'W'
# print(ans)

D = int(input("Day = "))
M = int(input("Month = "))
D += 1
maxx = 0
if M == 2:
    maxx = 28
elif M == 4 or M == 9 or M == 11:
    maxx = 30
else:
    maxx = 31
if D > maxx:
    D -= maxx
    M += 1
    if M > 12:
        M -= 12
print(f"{D}/{M}")
# match M:
#     case 1: maxx = 31
#     case 2: maxx = 28
#     case 3: maxx = 31
#     case 4: maxx = 30
#     case 5: maxx = 31
#     case 6: maxx = 30
#     case 7: maxx = 31
#     case 8: maxx = 31
#     case 9: maxx = 30
#     case 10: maxx = 31
#     case 11: maxx = 30
#     case 12: maxx = 31
