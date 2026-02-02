# def factorial(n: int):
#     ans = 1
#     for i in range(1, n+1):
#         ans *= i
#     return ans
#
# num = int(input("Number = "))
#
# print(f"Factorian {num}: {factorial(num)}")

# def fact(n):  # рекурсія
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(5))

# def num_line_print(n):
#     if n == 1:
#         return "1"
#     return str(n) + num_line_print(n - 1)
#
# print(num_line_print(5))

# def num(n):
#     print(n, end=' ')
#     if n > 1:
#         num(n-1)
#
# num(5)

# def num(n):
#     if n > 1:
#         num(n-1)
#     print(n, end=' ')
#
# num(5)

# def degree(a, n):
#     if n == 1:
#         return a
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1/degree(a, abs(n))
#     return a * (degree(a, n-1))
#
# print(degree(2, -2))

# def the_sum(a, b):
#     min_n = min(a, b)
#     max_n = max(a, b)
#     ans = min_n
#     if min_n+1 == max_n:
#         return ans + min_n + 1
#     return ans + the_sum(min_n+1, max_n)
#
# (print(the_sum(2, 8)))

def the_sum(n):
    ans = n%10
    if n//10 < 10:
        return ans + n//10
    return ans + the_sum(n//10)

print(the_sum(1654))
