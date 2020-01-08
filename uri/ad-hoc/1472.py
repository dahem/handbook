while True:
    n = int(input())
    if n == 0:
        break
    s = input().split()
    maxi = 0
    edges = []
    for x in s:
        [a, b] = x.split(',')
        a = int(a[1:])
        b = int(b[:-1])
        maxi = max(maxi, a)
        maxi = max(maxi, b)
        edges.append((a, b))
    g = [[] for x in range(maxi + 1)]
    vis = [False for x in range(maxi + 1)]
    for x in edges:
        g[x[0]].append(x[1])
        g[x[1]].append(x[0])

    ans = 0
    q = [1]

    while len(q) > 0:
        u = q.pop(0)
        vis[u] = True
        ans += 1
        for v in g[u]:
            if not vis[v]:
                q.append(v)
                vis[v] = True
    print(ans)
