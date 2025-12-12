n = int(input("Asterics = "))
print("\n\t\tА")
for i in range(n):
    for j in range(i):
        print("   ", end='')
    for j in range(n-i):
        print("*  ", end='')
    print()

print("\n\t\tБ")
for i in range(n):
    for j in range(i+1):
        print("*  ", end='')
    print()

print("\n\t\tВ")
for i in range(n):
    for j in range(i):
        print("   ", end='')
    for j in range(n-2*i):
        print("*  ", end='')
    print()

print("\n\t\tГ")
for i in range(n):
    for j in range(n-i-1):
        print("   ", end='')
    for j in range(2*i-n+2):
        print("*  ", end='')
    print()

print("\n\t\tД")
for i in range(n):
    if i < n/2:
        for j in range(i):
            print("   ", end='')
        for j in range(n-2*i):
            print("*  ", end='')
    else:
        for j in range(n-i-1):
            print("   ", end='')
        for j in range(2*i-n+2):
            print("*  ", end='')
    print()

print("\n\t\tЕ")
for i in range(n):
    if i < n/2:
        for j in range(i+1):
            print("*  ", end='')
        for j in range(n-2*i-2):
            print("   ", end='')
        if i+1 >= n/2:
            for j in range(i):
                print("*  ", end='')
        else:
            for j in range(i+1):
                print("*  ", end='')
    else:
        for j in range(n-i):
            print("*  ", end='')
        for j in range(2*i-n):
            print("   ", end='')
        for j in range(n-i):
            print("*  ", end='')
    print()

print("\n\t\tЖ")
for i in range(n):
    if i < n/2:
        for j in range(i+1):
            print("*  ", end='')
    else:
        for j in range(n-i):
            print("*  ", end='')
    print()

print("\n\t\tЗ")
for i in range(n):
    if i < n/2:
        for j in range(n-i-1):
            print("   ", end='')
        for j in range(i+1):
            print("*  ", end='')
    else:
        for j in range(i):
            print("   ", end='')
        for j in range(n-i):
            print("*  ", end='')
    print()

print("\n\t\tИ")
for i in range(n):
    for j in range(n-i):
        print("*  ", end='')
    print()

print("\n\t\tК")
for i in range(n):
    for j in range(n-i-1):
        print("   ", end='')
    for j in range(i+1):
        print("*  ", end='')
    print()
