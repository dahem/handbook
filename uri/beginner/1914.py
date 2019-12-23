n = int(input())

for x in range(n):
    [a, b, c, d] = input().split()
    x, y = map(int, input().split())
    if (x+y) % 2 == 0:
        if b == "PAR":
            print(a)
        else:
            print(c)
    else:
        if b == "IMPAR":
            print(a)
        else:
            print(c)
