A = [0, 1, 0, -1]
B = [1, 0, -1, 0]
ind = 0
while True:
    n, m = map(int, input().split())
    if ind != 0:
        print("")
    ind += 1
    if n == m == 0:
        break
    mat = []
    q = []
    vis = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        s = input()
        mat.append(list(s))
        for j in range(len(s)):
            if s[j] == 'T':
                vis[i][j] = True
                q.append((i, j))

    while len(q) > 0:
        u = q.pop(0)
        vis[u[0]][u[1]] = True
        mat[u[0]][u[1]] = 'T'
        for i in range(4):
            if 0 <= u[0] + A[i] < n and 0 <= u[1] + B[i] < m:
                if not vis[u[0] + A[i]][u[1] + B[i]] and mat[u[0] + A[i]][u[1] + B[i]] == 'A':
                    vis[u[0] + A[i]][u[1] + B[i]] = True
                    q.append((u[0] + A[i], u[1] + B[i]))

    for x in mat:
        print("".join(x))
