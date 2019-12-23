def run():
    n = int(input())
    arr = []
    for x in range(n):
        cad = input()
        arr.append(cad)
    m = int(input())
    for x in range(m):
        cad = input()
        ans = 0
        len_max = 0
        for y in range(n):
            if arr[y].startswith(cad):
                ans += 1
                len_max = max(len_max, len(arr[y]))
        if ans == 0:
            print(-1)
        else:
            print(ans, len_max)


while True:
    try:
        run()
    except:
        break
