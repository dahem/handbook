n = int(input())

for x in range(n):
    x = int(input())
    x -= 2015
    x += 1
    if x > 0:
        print(x, "A.C.")
    else:
        print(-x + 1, "D.C.")
