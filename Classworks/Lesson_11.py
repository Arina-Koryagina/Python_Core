# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
# n = 0
# num = [a, b, c, d]
# print(num[1])
# for el in num:
#     if el > 0:
#         n += 1
#
# # for i in range(4):
# #     if num[i] > 0:
# #         n += 1
# print(n)

# nums = [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]
# nul1 = 0
# nul2 = 0
# # one = 0
# # for el in nums:
# #     if el == 0:
# #         nul1 += 1
# #     if el == 0 and one == 0:
# #         nul2 += 1
# #     if el == 1:
# #         one += 1
# for el in nums:
#     if el == 0:
#         nul1 += 1
# i = 0
# while nums[i] == 0:
#     nul2 += 1
#     i += 1
# print(f"0 in total = {nul1}, 0 before 1 = {nul2}")

# nums = [1, 2, 4, 7, 7, 5, 3, 2]
# print(nums)
# print(nums.index(7))
# print(nums.count(7))
# nums.append(100)
# print(nums)
# nums.remove(1)
# print(nums)
# nums.reverse()
# print(nums)
# nums.insert(4, 999)
# print(nums)
# nums.pop(1)
# print(nums)

# import random
# print(random.randint(0, 10))
# n = int(input("n = "))
# nums = [random.randint(-100, -10) for i in range(n)]
# for i in range(n):
#     nums.append(random.randint(0, 10))
# print(nums)
# nums[1] = 999
# print(nums)
# print(len(nums))
# maxi = 0
# for i in range(len(nums)):
#     if nums[i] > maxi:
#         maxi = nums[i]
# for el in nums:
#     if el > maxi:
#         maxi = el
# for i in range(len(nums)):
#     if nums[i] > nums[i-1]:
#         maxi = nums[i]
# maxi = nums[0]
# index = 0
# for i in range(len(nums)):  # nums.index(max(nums))
#     if nums[i] > maxi:
#         maxi = nums[i]
#         index = i
# print(index)
# for el in nums:
#     if el < maxi:  # max(nums)
#         maxi = el

# print(max(nums))
# print(nums.index(max(nums)))

# s = "mama"
# for i in s:
#     print(i)

# import random
# n = int(input("n = "))
# nums = [random.randint(0, 10) for i in range(n)]
# print(nums)
#
# even = [el for el in nums if el % 2 == 0]
# # for el in nums:
# #     if el % 2 == 0:
# #         even.append(el)
# print(even)

# a = nums[0]
# # nums[0] = nums[len(nums) - 1]
# # nums[len(nums) - 1] = a
# nums[0] = nums[-1]
# nums[-1] = a
#
# print(nums)
#
# print(nums[1:4])
# print(sum(nums[1:4]))

# maxVal = nums[0]
# maxI = 0
# minVal = nums[0]
# minI = 0
# sum = 0
# for i in range(len(nums)):
#     if nums[i] > nums[maxI]:
#         maxI = 1
#     if nums[i] < nums[minI]:
#         minI = i
# a = minI if maxI > minI else maxI
# b = maxI if maxI > minI else minI
# for i in range(a+1, b):
#     sum += nums[i]
# print(sum)


