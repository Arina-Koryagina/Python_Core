#  I
print("\t\tI")

n = int(input("Amount of digits: "))
print(f"All the {n}-digit Armstrong numbers are:")
for i in range(10**(n-1), 10**n):
    m = i
    armstrong_numbers = 0
    for j in range(n):
        digit = m % 10
        m //= 10
        armstrong_numbers += digit**n
    if i == armstrong_numbers:
        print(i, end='; ')

#  II
print("\n\t\tII")

summ = 0
for i in range(50000):
    m = i+1
    fourths = 0
    thirteenths = 0
    while m > 0:
        digit = m % 10
        if digit == 4 and fourths == 0 and thirteenths == 0:
            summ += 1
            fourths = 1
        elif digit == 3 and thirteenths == 0 and fourths == 0:
            three = m // 10 % 10
            if three == 1:
                summ += 1
                thirteenths = 1
        m //= 10
print(f"The amount of tanks that would be painted is  {summ}.")
