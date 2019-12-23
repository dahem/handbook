import math


def run():
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        arr = [int(x) for x in input().split()]
        mat.append(arr)

    sol = [[0 for y in range(m)] for x in range(n)]

    A = [1, 0, 0, -1]
    B = [0, 1, -1, 0]

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                sol[i][j] = 9
                continue
            ans = 0
            for x in range(4):
                if (0 <= i + A[x] < n) and (0 <= j + B[x] < m):
                    ans += mat[i + A[x]][j + B[x]]
            sol[i][j] = ans
    # print(sol)
    for x in sol:
        print("".join(map(str, x)))


while True:
    try:
        run()

    except:
        break
