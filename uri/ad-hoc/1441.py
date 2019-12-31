
arr = []


def getSeq(n):
    arr.append(n)
    if n == 1:
        return
    if n % 2 == 0:
        getSeq(n//2)
    else:
        getSeq(3*n + 1)


while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    getSeq(n)
    print(max(arr))
