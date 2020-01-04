def run():
    n, m = map(int, input().split())
    if n == m == 0:
        raise Exception()

    arr = [int(x) for x in input().split()]

    for i in range(m):
        a, b, v = map(int, input().split())
        arr[a-1] -= v
        arr[b-1] += v

    for x in arr:
        if x < 0:
            print("N")
            return
    print("S")


while True:
    try:
        run()
    except:
        break
