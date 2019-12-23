while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        x = int(input())
        if x % 2 == 1:
            print(x * 2 - 1)
        else:
            print(x * 2 - 2)
