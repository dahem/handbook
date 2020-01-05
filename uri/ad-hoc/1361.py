def run():
    n = int(input())
    arr = []
    for x in range(n):
        num = int(input())
        arr.append((abs(num), num > 0))
    arr.sort()
    # print(arr)
    last = arr[0][1]
    ans = 1
    for a, b in arr:
        if last != b:
            ans += 1
            last = b
    print(ans)


cases = int(input())
for cas in range(cases):
    run()
