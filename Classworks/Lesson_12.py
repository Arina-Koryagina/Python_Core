import random

# l = 10
# nums = [random.randint(-5, 5) for i in range(l)]
# print(nums)
# print(sum([el for el in nums if el > 0]))
# print([i for i in range(len(nums)) if nums[i] % 2 == 0])
# un = set(nums)
# print(un)

# l = 10
# nums = [random.randint(0, 10) for i in range(l)]
# print(nums)
# for i in range(l // 2):
#     nums[i], nums[l-1-i] = nums[l-1-i], nums[i]
# for i in range(l // 2):
#     t = nums[i]
#     nums[i] = nums[l-1-i]
#     nums[l-1-i] = t
# for i in range(l):
#     for j in range(l-1-i):
#         t = nums[i]
#         nums[i] = nums[l-1-i]
#         nums[l-1-i] = t
# print(nums)

h = 24
temp = [random.randint(1, 25) for i in range(h)]
print(temp)
# the_diff = 0
# hour = 0

# for i in range(h-1):
#     diff = abs(temp[i+1] - temp[i])
#     if diff > the_diff:
#         the_diff = diff
#         hour = i
# print(the_diff, hour)
# for i in range(h-1):
#     diff = abs(temp[i+1] - temp[i])
#     if temp[i] > temp[i+1]:
#         if diff > the_diff:
#             the_diff = diff
#             hour = i
# print(the_diff, hour)

for j in range(25):
    for t in range(24):
        if 25-j > temp[t]:
            print("      ", end='')
        else:
            print("  *   ", end='')
    print(25-j)
str_h = [i for i in range(24)]
for el in str_h:
    if el < 10:
        print(f'0{str(el)}:00', end=' ')
    else:
        print(f'{str(el)}:00', end=' ')

# n = 10
# a = 5
# nums = [random.randint(0, 10) for i in range(n)]
# print(nums)

# for j in range(n-1):
#     for i in range(n-1-j):
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
# for j in range(n-1):
#     for i in range(n-1-j):
#         if nums[i] < nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
# print(nums)

# for i in range(a):
#     print(nums[-i-1], end=' ')

# nums.sort()
# print(nums)
# for i in range(2):
#     print(nums[-i-1], end=' ')
# maxi = nums[0]
# index = []
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[j] > maxi:
#             maxi = nums[j]
#     if nums[i] == maxi:
#         index.append(i)
# print(index)


# n = 10
# # nums = [random.randint(0, 10) for i in range(n)]
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums)
# progression = nums[1] - nums[0]
# ans = True
# for i in range(n-1):
#     if nums[i+1] - nums[i] != progression:
#         ans = False
# print(ans)

# l = [[2, 3, 5], [2, 1, 4], [6, 8, 6]]
# # print(l)
# for i in range(len(l)):
#     the_sum = 0
#     for j in range(len(l[i])):
#         print(l[i][j], end='  ')
#         the_sum += l[i][j]
#     print(f"|  {the_sum}")
