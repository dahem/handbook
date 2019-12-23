n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if c == 0:
        print("%02d:%02d - A porta fechou!" % (a, b))
    else:
        print("%02d:%02d - A porta abriu!" % (a, b))
