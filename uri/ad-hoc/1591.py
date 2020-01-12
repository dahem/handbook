def count(w, txt):
    n = len(txt)
    m = len(w)
    ans = 0
    for i in range(n-m+1):
        if w == txt[i:i+m]:
            ans += 1
    return ans


def search(w, mat):
    r = [count(w, x) for x in mat]
    return sum(r)


def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0

    # A loop to slide pat[] one by one
    for i in range(N - M + 1):

        # For current index i, check
        # for pattern match
        j = 0
        for j in range(M):
            if (txt[i + j] != pat[j]):
                break

        if (j == M - 1):
            res += 1
            j = 0
    return res


print(countFreq("a", "asa"))


def run():
    n, m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append(input())
    k = int(input())
    matinv = []
    for j in range(m):
        col = ""
        for i in range(n):
            col += mat[i][j]
        matinv.append(col)

    for i in range(k):
        s = input()
        if len(s) == 1:
            print(search(s, mat))
        else:
            print(search(s, mat) + search(s, matinv))


cases = int(input())
for cas in range(cases):
    run()
