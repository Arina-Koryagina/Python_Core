# a = 1
# while a <= 5:
#     print(a, end=' ')
#     a += 1

# a = 5
# while a > 0:
#     print(a, end=' ')
#     a -= 1

# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     while a >= b:
#         print(a, end=' ')
#         a -= 1
# else:
#     while a <= b:
#         print(a, end=' ')
#         a += 1

# a = int(input("a = "))
# b = int(input("b = "))
# while a >= b:
#     a -= b
# print(a)

# a = int(input("a = "))
# b = int(input("b = "))
# c = 0
# while a >= b:
#     a -= b
#     c += 1
# print(c)

# N = int(input("N = "))
# while N % 3 == 0:
#     N /= 3
# if N == 1:
#     print("True")
# else:
#     print("False")

# N = int(input("N = "))
# k = 1
# while k < N:
#     k *= 3
# print(k == N)

# N = int(input("N = "))
# k = 0
# while N > 1:
#     N /= 2
#     k += 1
# print(k)

# N = int(input("N = "))
# k = 1
# s = 0
# while N > k:
#     k *= 2
#     s += 1
# print(s)

# N = int(input("N = "))
# k = 1
# # while (k+1)**2 <= N:
# #     k += 1
# # print(k)
# while k**2 <= N:
#     k += 1
# print(k-1)

# N = int(input("N = "))
# k = 0
# # while N > 9:
# #     k += N % 10
# #     N //= 10
# # print(k + (N % 10))
# while N > 0:
#     k += N % 10
#     N //= 10
# print(k)

# N = int(input("N = "))
# i = 1
# s = 0
# # while i < N:
# #     s += (i * 10) + i
# #     i += 1
# # print(s)
# # while i < N:
# #     s += i * 11
# #     i += 1
# # print(s)
# while i <= N:
#     m = int(str(i) + str(i))
#     s += m
#     i += 1
#     print(m, end=' + ')
# print(f"\n= {s}")

# N = int(input("N = "))
# k = 0
# while N > 0:
#     N //= 10
#     k += 1
# print(k)

N = int(input("N = "))
i = 1
s = 0
while i <= N:
    if i % 2 == 0:
        s -= i
        print(i, end=" + ")
    else:
        s += i
        print(i, end=" - ")
    i += 1
print(f"\n= {s}")
