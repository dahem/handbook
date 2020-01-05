def run():
    n = int(input())
    arr = [int(x) for x in input().split()]
    p = set()

    last = 0
    for x in arr:
        last += x
        p.add(last)

    if last % 3 != 0:
        print(0)
        return
    lenT = last // 3
    ans = 0
    for x in p:
        if x + lenT in p and x + 2 * lenT in p:
            ans += 1

    print(ans)


while True:
    try:
        run()
    except:
        break
