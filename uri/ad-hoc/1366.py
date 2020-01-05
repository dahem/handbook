def run(n):
    arr = []
    for x in range(n):
        a, b = map(int, input().split())
        arr.append(b)
    arr.sort()
    ans = 0
    ind = 0
    last = 0
    while(ind < n):
        if arr[ind] < 2:
            ind += 1
            continue
        ans += (arr[ind] // 4)
        arr[ind] %= 4

        if last == 0 and arr[ind] > 1:
            last = arr[ind]
        elif last > 0 and arr[ind] > 1:
            ans += 1
            last = 0
        ind += 1
    print(ans)


while True:
    n = int(input())
    if n == 0:
        break
    run(n)
