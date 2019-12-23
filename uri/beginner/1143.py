n = int(input())
for x in range(1, n+1):
    d = [x**i for i in range(1, 4)]
    e = [d[0], d[1]+1, d[2]+1]
    print(' '.join(map(str, d)))
    print(' '.join(map(str, e)))
