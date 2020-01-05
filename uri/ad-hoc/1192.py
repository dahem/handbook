
n = int(input())


for i in range(n):
    x = input()
    a = int(x[0])
    b = int(x[2])
    if x[1].isupper():
        if a == b:
            print(a * b)
        else:
            print(b - a)
    else:
        if a == b:
            print(a * b)
        else:
            print(a + b)
