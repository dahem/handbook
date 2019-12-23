n = int(input())
mat = []
for i in range(n+1):
    arr = [int(x) for x in input().split()]
    mat.append(arr)

sol = [[0 for y in range(n)] for x in range(n)]

for i in range(1, n+1):
    for j in range(1, n+1):
        a = mat[i-1][j-1]
        b = mat[i-1][j]
        c = mat[i][j-1]
        d = mat[i][j]
        if a + b + c + d >= 2:
            sol[i-1][j-1] = 'S'
        else:
            sol[i-1][j-1] = 'U'
for x in sol:
    print("".join(x))
