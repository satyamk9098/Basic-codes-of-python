num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(0, i):
        print((i + j) % 2, end=" ")
    print()
