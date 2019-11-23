cases = int(input())
# n, m = map(int, input().split())
for cas in range(cases):
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    sol = []
    for x in range(n):
        sol.append(arr2[x] - arr1[x])
    comp = 0
    item = 0
    status = False
    for x in range(n):
        if sol[x] > 0 and not status:
            status = True
            item = sol[x]
            comp += 1
        if sol[x] > 0 and status:
            if item != sol[x]:
                comp = 10000000000
                break
            continue
        if sol[x] == 0:
            status = False
        if sol[x] < 0:
            comp = 10000000000
            break
    if comp > 1:
        print("NO")
    else:
        print("YES")
