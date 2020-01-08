def run():
    n, m = map(int, input().split())
    if n == m == 0:
        raise Exception()
    mat = []
    c = [1, 1, 1, 0]
    pro = [0 for x in range(m)]
    d = 0

    for x in range(n):
        arr = [int(x) for x in input().split()]
        if arr.count(1) == m:
            c[0] = 0
        pro = [x + y for x, y in zip(arr, pro)]
        if arr.count(1) > 0:
            d += 1

    if pro.count(0) > 0:
        c[1] = 0

    if pro.count(n) > 0:
        c[2] = 0

    if d == n:
        c[3] = 1
    # print(c)
    print(sum(c))


while True:
    try:
        run()
    except:
        break
