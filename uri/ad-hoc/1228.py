def run():
    n = int(input())
    start = [int(x) for x in input().split()]
    end = [int(x) for x in input().split()]
    ans = 0
    i = 0
    print(start)
    while i < n:
        while start[i] != end[i]:
            temp = start.index(end[i])
            ans += 1
            start[temp], start[temp - 1] = start[temp - 1], start[temp]
            print(start)
        i += 1
    print(ans)


# run()
while True:
    try:
        run()
    except:
        break
