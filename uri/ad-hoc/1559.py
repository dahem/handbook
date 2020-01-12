from collections import Counter


def checRowOrCol(arr):
    zeros = arr.count(0)
    if zeros == 4:
        return False
    for i in range(1, 4):
        if arr[i] == arr[i-1] and arr[i] > 0:
            return True
    for i in range(4):
        if arr[i] == 0:
            zeros -= 1
        else:
            break
    if zeros > 0:
        return True
    return False


def check(move, mat):
    for x in mat:
        if 2048 in x:
            return False

    if move == 'DOWN':
        for j in range(4):
            col = []
            for i in range(4):
                col.append(mat[i][j])
            if checRowOrCol(col):
                return True

    elif move == 'LEFT':
        for i in range(4):
            if checRowOrCol(mat[i][::-1]):
                return True

    elif move == 'RIGHT':
        for i in range(4):
            if checRowOrCol(mat[i]):
                return True
    else:
        for j in range(4):
            col = []
            for i in range(1, 5):
                col.append(mat[-i][j])
            if checRowOrCol(col):
                return True
    return False


def run():
    mat = []
    for i in range(4):
        mat.append([int(x) for x in input().split()])
    moves = ['DOWN', 'LEFT', 'RIGHT', 'UP']
    ans = []
    for x in moves:
        if check(x, mat):
            ans.append(x)
    if len(ans) == 0:
        print("NONE")
    else:
        print(" ".join(ans))


cases = int(input())
while cases > 0:
    run()
    cases -= 1
