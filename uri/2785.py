import math

n = int(input())
mat = []
for i in range(n):
    arr = [int(x) for x in input().split()]
    mat.append(arr)

dp = [[0 for y in range(n)] for x in range(n)]
for j in range(n):
    dp[0][j] = mat[0][j]

for i in range(1, n):
    for j in range(i, n):
        a = 0
        for k in range(j - i, j+1):
            a += mat[i][k]

        dp[i][j] = a + min(dp[i-1][j-1], dp[i-1][j])
# for x in dp:
#     print(x)
print(dp[n-1][n-1])
