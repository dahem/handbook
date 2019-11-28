

while True:
    try:
        mat = []
        n, m = map(int, input().split())
        for i in range(n):
            arr = [int(x) for x in input().split()]
            mat.append(arr)
        one = []
        two = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    one = [i, j]
                if mat[i][j] == 2:
                    two = [i, j]

        print(abs(one[0]-two[0]) + abs(one[1]-two[1]))

    except:
        break
