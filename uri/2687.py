cases = int(input())
mat = None
n = 0


def dfs(i, j):
    if (0 <= i < n) and (0 <= j < n) and mat[i][j] == 0:
        mat[i][j] = -1
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i-1, j)
        dfs(i, j-1)


for cas in range(cases):
    n = int(input())
    mat = []
    for i in range(n):
        arr = [int(x) for x in input().split()]
        mat.append(arr)

    for i in range(n):
        dfs(i, 0)
        dfs(i, n-1)
        dfs(0, i)
        dfs(n-1, i)
    sol = 0
    for x in mat:
        for y in x:
            if y > -1:
                sol += 1
    print("%.2f" % (sol/2))
