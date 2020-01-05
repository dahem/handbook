def run():
    n = int(input())
    arr = [int(x) for x in input().split()]
    if sum(arr) % n != 0:
        print(-1)
    else:
        tot = 0
        avg = int(sum(arr))//n
        for x in arr:
            tot += abs(x - avg)
        print(tot//2 + 1)


# run()
while True:
    try:
        run()
    except:
        break
