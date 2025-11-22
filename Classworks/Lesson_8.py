# n1 = int(input("Forward = "))  # 4
# n2 = int(input("Backward = "))  # 2
# n3 = int(input("In between = "))  # 8
# d = 0  # 3
# while n3 > 0:
#     n3 -= n1
#     if n3 > 0:
#         n3 += n2
#     d += 1
# print(d)

# P = float(input("P (0-50%) = "))
# s = 10
# K = 1
# S = 10
# add = 0
# while S <= 200:
#     add = S / 100 * P
#     S += s + add
#     K += 1
#     print(f"Add = {add}, distance = {S}, days = {K}")
# print(f"Days = {K}, distance = {S}")

# n = 12555
# n1 = n % 10
# n2 = (n // 10) % 10
# n3 = (n // 100) % 10
# n4 = (n // 1000) % 10
# n5 = n // 10000
# print(n5, n4, n3, n2, n1, ((n1+n2+n3+n4+n5) % 9))

# n = 10000
# fives = 0
# numb = 0
# while n <= 99999:
#     n1 = n % 10
#     if n1 == 5:
#         fives += 1
#     n2 = (n // 10) % 10
#     if n2 == 5:
#         fives += 1
#     n3 = (n // 100) % 10
#     if n3 == 5:
#         fives += 1
#     n4 = (n // 1000) % 10
#     if n4 == 5:
#         fives += 1
#     n5 = n // 10000
#     if n5 == 5:
#         fives += 1
#     # print(n, fives)
#     if fives == 3:
#         if (n1+n2+n3+n4+n5) % 9 == 0:
#             print(n)
#             numb += 1
#     n += 1
#     fives = 0
# print(numb)

# n = 10000
# numb = 0
# while n <= 99999:
#     if n % 9 == 0:
#         fives = 0
#         m = n
#         while m > 0:
#             r = m % 10
#             if r == 5:
#                 fives += 1
#             m //= 10
#         if fives == 3:
#             print(n)
#             numb += 1
#     n += 1
# print(numb)

# n = int(input("n (2-10) = "))
# print("-------")
# m = 1
# while m < 11:
#     print(f"{n} * {m} = {n*m}")
#     m += 1
# print("-------")
# m = 1
# while m < 11:
#     print(f"{n*m} : {n} = {m}")
#     m += 1
# print("-------")
# m = 1
# while m < 11:
#     print(f"{n} ^ {m} = {n**m}")
#     m += 1
# print("-------")
# m = 1
# while m < 11:
#     print(f"{m} root of {n**m} = {n}")
#     m += 1
# print("-------")
# m = 1
# while m < 11:
#     print(f"square root of {n**m}  = {round(n**(m/2), 2)}")
#     m += 1

# f1 = 1
# f2 = 1
# n = int(input("n = "))
# fn = 0
# if n == 1 or n == 2:
#     print(f1)
# else:
#     while n > 2:
#         fn = f1 + f2
#         f1 = f2
#         f2 = fn
#         n -= 1
#     print(fn)

# f1 = 1
# f2 = 1
# fn = 1
# Fn = int(input("F_n = "))
# n = 2
# if Fn == f1:
#     print("1 or 2")
# else:
#     while fn != Fn:
#         fn = f1 + f2
#         f1 = f2
#         f2 = fn
#         n += 1
#     print(n)

n = float(input("n = "))
s = n
while n != 0:
    n = float(input("n = "))
    s += n
print(s)
