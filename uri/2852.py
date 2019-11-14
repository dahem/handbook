s = 26
mat = [[0 for j in range(s)] for i in range(s)]

for i in range(s):
    for j in range(s):
        mat[i][j] = (i + j) % s


def convert(cad, pat, ind):
    sol = ''
    nexInd = ind
    for i in range(len(cad)):
        y = cad[i]
        nexInd = (nexInd) % len(pat)
        x = pat[nexInd]
        letterInd = mat[ord(x) - ord('a')][ord(y) - ord('a')]
        sol += chr(letterInd + ord('a'))
        nexInd += 1
    return sol, nexInd


keyWord = input()

n = int(input())
for x in range(n):
    arr = input().split()
    sol = []
    ind = 0
    for y in arr:
        if y[0] in ['a', 'e', 'i', 'o', 'u']:
            sol.append(y)
        else:
            cad, ind = convert(y, keyWord, ind)
            sol.append(cad)
    print(" ".join(sol))
