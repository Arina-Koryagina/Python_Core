# m = int(input("m (kg) = "))
# z1 = int(input("z1 (kg) = "))
# z2 = int(input("z2 (g) = "))
# z = 1000 * z1 + z2  # g
# k = 1000 * m - z  # g
# if k > z:
#     print("Кролик")
# elif k == z:
#     print("Однаково")
# else:
#     print("Заяць")

L = float(input("L (l) = "))
if L > 0:
    L = L * 1000
    k1 = float(input("p (%) = "))
    if k1 > 0 and k1 < 100:
        k1 = L / 100 * k1
        L -= k1
        k2 = int(input("m (ml) = "))
        if k2 >= 0 and k2 <= L:
            k3 = L - k2
            if k1 > k3:
                print("k1")
            elif k1 == k3:
                print("Same")
            else:
                print("k3")
        else:
            print("Can't be done. 0 < k2 < L only. Try again.")
    else:
        print("Can't be done. 0 <= p <= 100 (%) only. Try again.")
elif L == 0:
    print("L = 0.")
else:
    print("Can't be done. L > 0 (l) only. Try again.")
