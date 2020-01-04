def run():
    n, m = map(int, input().split())
    if n == m == 0:
        raise Exception()

    arr = [n - int(x) for x in input().split()]
    # print(arr)
    ind = 1
    ans = arr[0]
    while ind < m:
        if arr[ind] > arr[ind-1]:
            ans += arr[ind] - arr[ind-1]
        ind += 1
    print(ans)


while True:
    try:
        run()
    except:
        break
