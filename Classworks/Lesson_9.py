# for i in range(5, 20, 2):  # ([first], (last), step)
#     print(i)

# n = float(input("The price = "))
# for i in range(1, 11):
#     print(f"Price of {i} kg is {n * i}")

# n = float(input("The price of 1 kg (UAH) = "))
# for i in range(1, 11):
#     print(f"Price of {i/10} kg is {n * i/10} UAH")

# n = float(input("The price of 1 kg (UAH) = "))
# for i in range(12, 22, 2):
#     print(f"Price of {i/10} kg is {n * i/10} UAH")
# for i in range(2, 12, 2):
#     print(f"Price of {1+i/10} kg is {n * (1+i/10)} UAH")

# A = int(input("A = "))
# B = int(input("B = "))
# S = 0
# # for i in range((B-A)+1):
# #     S += A+i
# for i in range(A, B+1):
#      S += i
# print(S)

# n = int(input("N = "))
# s = 0
# # for i in range(11, 12+n, 2):
# #     s += i/10
# # for i in range(12, 11+n, 2):
# #     s -= i/10
# for i in range(1, n+1):
#     p = (1+i/10) * (-1)**(i+1)
#     s += p
#     print(p, end=' ')
# print(s)

# f = int(input("Fridges = "))
# n = int(input("Shops = "))
# s = 0  # f * n
# for i in range(n):
#     s += f
# print(s)

# n = int(input("Shops = "))
# s = 0
# for i in range(n):
#     f = int(input(f"Fridges in {i+1} = "))
#     s += f
# print(s)

# n = int(input("Schools = "))
# s = 0
# for i in range(n):
#     p = int(input(f"Students in {i+1} = "))
#     if p > 1000:
#         s += 1
# print(s)

# s = 0
# for n in range(1, 1000000):
#     N6 = n % 10
#     N5 = n // 10 % 10
#     N4 = n // 100 % 10
#     N3 = n // 1000 % 10
#     N2 = n // 10000 % 10
#     N1 = n // 100000
#     if N1 + N2 + N3 == N4 + N5 + N6:
#         s += 1
# print(s)

# 00:00:00 - 23:59:59
# s = 0
# for h in range(24):
#     for m in range(60):
#         h1 = h // 10
#         h2 = h % 10
#         m1 = m // 10
#         m2 = m % 10
#         if h2 == m1 and h1 == m2:
#             print(f"{h1}{h2}:{m1}{m2}")
#             s += 1
# print(s)

# f = 0
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             h1 = h // 10
#             h2 = h % 10
#             m1 = m // 10
#             m2 = m % 10
#             s1 = s // 10
#             s2 = s % 10
#             if h1 == s2 and h2 == s1 and m1 == m2:
#                 print(f"{h1}{h2}:{m1}{m2}:{s1}{s2}")
#                 f += 1
# print(f)

A = int(input("A = "))
B = int(input("B = "))
for i in range(A, B+1):
    for j in range(i):
        print(i, end=' ')
    print()
