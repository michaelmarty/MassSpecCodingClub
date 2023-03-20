list1 = []
list2 = []

for penguin in range(0, 10):
    a = 0
    b = 1
    if penguin >= 2:
        a = 1

    if penguin < 3:
        b = 2

    list1.append(a)
    list2.append(b)

print(list1)
print(list2)
