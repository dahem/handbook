def run():
    n, m = map(float, input().split())
    arr = [float(x) for x in input().split()]
    avg = sum(arr) / len(arr)
    measure = 0.0
    for x in range(len(arr)):
        measure += (arr[x]-avg)*(arr[x]-avg)
    ans = measure/(len(arr) - 1.0)
    ans = ans**0.5
    print("%.5f" % ans)


# run()
while True:
    try:
        run()
    except:
        break
