def calc(a, b, arr):
    for i in range(1, len(arr)):
        if arr[i] == 0:
            if arr[i-1] % 2 == 0:
                if len(a) > 0:
                    arr[i] = a.pop()
                else:
                    arr[i] = b.pop()
            else:
                if len(b) > 0:
                    arr[i] = b.pop()
                else:
                    arr[i] = a.pop()
            # print(arr)
    ans = 0
    for i in range(1, len(arr)):
        if (arr[i] + arr[i-1]) % 2 == 1:
            ans += 1
    return ans


n = int(input())

arr = [int(x) for x in input().split()]
arrarr = arr[:]
pa = [x for x in arr if x > 0 and x % 2 == 0]
a = [x for x in range(2, n + 1, 2) if x not in pa]
aa = a[:]
pb = [x for x in arr if x > 0 and x % 2 == 1]
b = [x for x in range(1, n + 1, 2) if x not in pb]
bb = b[:]

if len(a) == len(b) == 0:
    ans = 0
    for i in range(1, len(arr)):
        if (arr[i] + arr[i-1]) % 2 == 1:
            ans += 1
    print(ans)
    exit()

if arr[0] == 0:
    if len(a) > 0:
        arr[0] = a.pop()
    else:
        arr[0] = b.pop()
    if len(bb) > 0:
        arrarr[0] = bb.pop()
    else:
        arrarr[0] = aa.pop()
    print(min(calc(a, b, arr), calc(aa, bb, arrarr)))
else:
    # print("a", a)

    # print("b", b)
    print(calc(a, b, arr))
