def run():
    n, m = map(int, input().split())
    if n == m == 0:
        raise Exception()

    arr = [int(x) for x in input().split()]

    set_arr = set()
    for i in range(m):
        for j in range(i, m):
            set_arr.add(abs(arr[j] - arr[i]))

    # print(list(set_arr))
    if len(set_arr) == n+1:
        print("Y")
    else:
        print("N")


while True:
    try:
        run()
    except:
        break
