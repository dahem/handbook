while True:
    n = input()
    if int(n) == 0:
        break
    a = set()
    a.add(n)
    ans = 1
    while True:
        s = str(int(n) * int(n))
        while len(s) < 2 * len(n):
            s = '0'+s
        n = s[2:6]
        if n in a:
            break
        a.add(n)
        ans += 1
    print(ans)
