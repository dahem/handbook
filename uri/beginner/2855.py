
import bisect
while True:
    try:
        n = int(input())
        arr = [int(x) for x in input().split()]
        m = int(input())
        idx = bisect.bisect_left(arr, m)
        idx += 1
        i = 2
        ans = True
        while i <= idx:
            if idx % i == 0:
                ans = False
                break
            idx -= idx // i
            i += 1
        if ans:
            print("Y")
        else:
            print("N")
    except:
        break
