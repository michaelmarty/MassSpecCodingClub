print(list(range(5)))

for i in range(5):
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)

'''
print(2==2)
print(1==2)
print(1>2)
print(2<=1)
print(2!=1)

if 1 == 2:
    print("TRUE")
elif 2 == 2:
    print("ELIF True")
else:
    print("FALSE")'''


def add(a, b, s=0, m=1, d=1):
    return m*(a + b - s)/d

c = add(1, 2, d=2)
print(c)
