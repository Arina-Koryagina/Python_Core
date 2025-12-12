# summ = 0
# for i in range(50000):
#     m = i+1
#     fourths = 0
#     thirteenths = 0
#     while m > 0:
#         digit = m % 10
#         if digit == 4 and fourths == 0 and thirteenths == 0:
#             summ += 1
#             fourths = 1
#         elif digit == 3 and thirteenths == 0 and fourths == 0:
#             three = m // 10 % 10
#             if three == 1:
#                 summ += 1
#                 thirteenths = 1
#         m //= 10
# print(f"The amount of tanks that would be painted is  {summ}.")
import math

# c = 0
# for n in range(50000):
#     n1 = n % 10
#     n2 = n // 10 % 10
#     n3 = n // 100 % 10
#     n4 = n // 1000 % 10
#     n5 = n // 10000 % 10
#     if (n1 == 4 or n2 == 4 or n3 == 4 or n4 == 4 or n5 == 4 or
#             n5 == 1 and n4 == 3 or n4 == 1 and n3 == 3 or n3 == 1 and n2 == 3 or n2 == 1 and n1 == 3):
#         c += 1
# print(c)

# n = int(input("Asterics = "))
# for i in range(n):
#     print("*", end='')

# n = int(input("Asterics = "))
# for i in range(n):
#     for j in range(n):
#         print("*  ", end='')
#     print()

# n = int(input("Asterics = "))
# m = 1
# for i in range(n):
#     for j in range(m):
#         print("*  ", end='')
#     m += 1
#     print()
# n = int(input("Asterics = "))
# for i in range(n):
#     for j in range(i+1):
#         print("*  ", end='')
#     print()

# n = int(input("Asterics = "))
# for i in range(n):
#     for j in range(n-i-1):
#         print("   ", end='')
#     for j in range(i+1):
#         print("*  ", end='')
#     print()

# n = int(input("Asterics = "))
# for i in range(n):
#     for j in range(n-i-1):
#         print("   ", end='')
#     for j in range(2*i+1):
#         print("*  ", end='')
#     print()

# n = 5
# k = 2
# for m in range(3):
#     for i in range(n):
#         for j in range(n-i-1+k):
#             print("   ", end='')
#         for j in range(2*i + 5 - (k*2)):
#             print("*  ", end='')
#         print()
#     k -= 1

# n = 5
# k = 2
# for m in range(3):
#     for i in range(n-k):
#         for j in range(n-i-1+k):
#             print("   ", end='')
#         for j in range(2*i + 5 - (k*2)):
#             print("*  ", end='')
#         print()
#     k -= 1

# n = 5
# for m in range(3):
#     for i in range(m+3):
#         for j in range(n-i+1-m):
#             print("   ", end='')
#         for j in range(2*m + 2*i + 1):
#             if (i == m+2 and (j == 0 or j == (2*i + 2*m)) or
#                     i == 0 and m == 0):
#                 print("#  ", end='')
#             else:
#                 print("*  ", end='')
#         print()

R = int(input("R = "))
r = int(input("r = "))
h = int(input("h = "))
n = 0
for i in range(-R, R, h):
    for j in range(-R, R, h):
        l = math.sqrt(i*i + j*j)
        if l > r and l < R:
            n += 1
print(n)
