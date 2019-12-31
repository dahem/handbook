def getOccurence(n, d):
    res = 0
    pot = 1
    rem = 0
    while n > 0:
        x = n % 10
        n //= 10
        if x > d:
            res += (n+1)*pot
        else:
            res += n*pot
        if x == d:
            res += rem + 1
        if d == 0:
            res -= pot
        rem += pot*x
        pot *= 10
    return res


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    ans = [getOccurence(b, i) - getOccurence(a-1, i) for i in range(10)]
    print(" ".join(map(str, ans)))
