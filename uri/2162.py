n = int(input())
d = [int(x) for x in input().split()]

if len(d) == 2:
    if d[0] == d[1]:
        print(0)
    else:
        print(1)
    exit()
ant = 0
for i in range(1, n):
    if d[i] == d[i-1]:
        print(0)
        exit()
    if d[i] > d[i-1]:
        if ant == 1:
            print(0)
            exit()
        else:
            ant = 1

    if d[i] < d[i-1]:
        if ant == -1:
            print(0)
            exit()
        else:
            ant = -1

print(1)
