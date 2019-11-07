d = False


def pp(arr):
    sol = []
    for x in arr:
        if x < 10:
            sol.append("  "+str(x))
            continue
        if x < 99:
            sol.append(" "+str(x))
            continue
        if x == 100:
            sol.append(str(x))
    return sol


while(True):
    n = int(input())
    if d:
        print("")
    d = True
    if n == 0:
        break
    mat = [[0 for y in range(n)] for x in range(n)]
    for x in range(n):
        for y in range(n):
            mat[x][y] = min(x, y, (n - 1) - x, (n - 1) - y) + 1

    for x in mat:
        print(" ".join(pp(x)))
