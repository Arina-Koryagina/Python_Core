#  I
print("\t\tI")

A = float(input("Введіть A: "))
B = float(input("Введіть B: "))
C = float(input("Введіть C: "))
AB = abs(B - A)
AC = abs(C - A)
if AC > AB:
    print(f"Найближчою до точки А є точка B, із відстанню {AB}")
elif AC == AB:
    print(f"Найближчою до точки А є обидві точки: B і C, із відстанню {AB}")
else:
    print(f"Найближчою до точки А є точка C, із відстанню {AC}")

#  II
print("\n\t\tII")

n = int(input("Введіть n: "))
ans = ""
if n > 0:
    ans += "додатнє"
else:
    ans += "від'ємне"
if n == 0:
    ans = "нульове"
elif n % 2 == 0:
    ans += " парне"
else:
    ans += " непарне"
print(f"{n} це " + ans + " число")

#  III
print("\n\t\tIII")

n = int(input("Введіть № місяця: "))
if 1 <= n <= 2 or n == 12:
    print(f"Місяць №{n} це   зима")
elif 3 <= n <= 5:
    print(f"Місяць №{n} це   весна")
elif 6 <= n <= 8:
    print(f"Місяць №{n} це   літо")
else:
    print(f"Місяць №{n} це   осінь")

#  IV
print("\n\t\tIV")

n = int(input("Введіть кількість дірок N для порівняння: "))
k = int(input("Введіть рази K (зламаною вилкою): "))
z = int(input("Введіть кількість відломаних зубців Z: "))
l1 = int(input("Введіть рази L1 (цілою вилкою): "))
s = int(input("Введіть кількість зубців S: "))
holes = l1*s + k*(s-z)
if n > holes:
    print(f"Ні, дірок залишиться меньше за {n}")
elif n < holes:
    print(f"Так, дірок залишиться більше за {n}")
else:
    print(f"Дірок залишиться рівно {n}")

#  V
print("\n\t\tV")

m = float(input("Введіть грошову суму (грн): "))
discount = 0
final_sum = 0
if m > 1000:  # 1100 / 825
    discount = 25
elif m > 500:  # 510 / 459
    discount = 10
elif m > 100:  # 110 / 104.5
    discount = 5
final_sum = m - (m / 100 * discount)
print(f"Якщо покупець заплатить {m}, то отримає знижку {discount}%, тож фінальна сума: {final_sum}")
