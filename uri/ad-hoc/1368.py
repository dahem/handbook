def check_cube(a, bp):
    b = bp[:]
    c = bp[:]
    for x in a:
        if x in b:
            b.remove(x)
    for x in a:
        if (x[1], x[0]) in c:
            c.remove((x[1], x[0]))

    return len(b) == 0 or len(c) == 0


def run(n):
    sol = []
    for i in range(n):
        a = int(input())
        arr = [int(x) for x in input().split()]
        b = int(input())
        item = [(a, b), (arr[0], arr[2]), (arr[1], arr[3])]

        if len(sol) == 0:
            sol.append(item)
            continue
        flag = False
        for y in sol:
            if check_cube(y, item):
                flag = True
        if not flag:
            sol.append(item)
    print(len(sol))


while True:
    n = int(input())
    if n == 0:
        break
    run(n)
