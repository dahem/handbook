

n = int(input())
inf = 1000000
dp = [[[inf for x in range(n)] for y in range(n)] for z in range(n)]
arr = [int(x) for x in input().split()]
pa = [x for x in arr if x > 0 and x % 2 == 0]
a = [x for x in range(2, n + 1, 2) if x not in pa]
pb = [x for x in arr if x > 0 and x % 2 == 1]
b = [x for x in range(1, n + 1, 2) if x not in pb]

len0 = len(a)
len1 = len(b)
if len(a) == len(b) == 0:
    ans = 0
    for i in range(1, len(arr)):
        if (arr[i] + arr[i-1]) % 2 == 1:
            ans += 1
    print(ans)
    exit()


def run(ind, lenA, lenB):
    if ind == n - 1:
        return 0
    if dp[ind][lenA][lenB] != inf:
        return dp[ind][lenA][lenB]
    if arr[ind] == 0:
        if lenA > 0:
            arr[ind] = 2
            dp[ind][lenA][lenB] = int((arr[ind] + arr[ind+1]) %
                                      2 != 0) + run(ind+1, lenA - 1, lenB)
        else:
            arr[ind] = 1
            dp[ind][lenA][lenB] = int((arr[ind] + arr[ind+1]) %
                                      2 != 0) + run(ind+1, lenA, lenB - 1)
    return dp[ind][lenA][lenB]


run(1, len0, len1)
