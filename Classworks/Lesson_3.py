# not -- унарний оператор логічної унверсїі, зазначається перед змінною
# > < == != <= >= or and -- бінарні оператори логіки

# a = int(input("a = "))
# res = a > 0
# print(res)

# a = int(input("a = "))
# res = a % 2 == 0
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# res = a > 2 and b <= 3
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = a < b and b < c
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = a < b and b < c or c < b and b < a
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# res = a % 2 == 1 or b % 2 == 1
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# # a1 = a % 2 == 1
# # b1 = b % 2 == 1
# # res = a1 and not b1 or not a1 and b1
# # res = a % 2 == 1 and b % 2 == 0 or a % 2 == 0 and b % 2 == 1
# res = a % 2 != b % 2
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = a > 0 and b > 0 and c > 0
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# a1 = a > 0
# b1 = b > 0
# c1 = c > 0
# # res = a1 and not b1 and not c1 or b1 and not a1 and not c1 or c1 and not b1 and not a1
# res = (a1 + b1 + c1) == 1
# print(res)

# a = int(input("a = "))
# # res = 0 < a // 100 < 9 and a % 2 == 1
# res = 100 < a < 1000 and a % 2 == 1
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = not (a != b and a != c and b != c)
# print(res)

# n = int(input("n = "))
# a = n % 10
# b = n // 10 % 10
# c = n // 100
# res = a != b and a != c and b != c
# print(res)

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = a == b and b == c
# print(res)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
a1 = a**2 == c**2 + b**2
b1 = b**2 == a**2 + c**2
c1 = c**2 == a**2 + b**2
res = a1 or b1 or c1
print(res)
