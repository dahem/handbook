
cases = int(input())
for cas in range(cases):
    n = int(input())
    arr = [int(x) for x in input().split()]
    sol = [x for x in arr if x % 2 == 1]
    sol.sort(reverse=True)
    n = len(sol)
    ans = []
    for i in range(n//2 + n % 2):
        ans.append(sol[i])
        if i != n - 1 - i:
            ans.append(sol[n - 1 - i])

    print(" ".join(map(str, ans)))
