def check(s):
    s = list(s)
    return len(s) == len(set(s))


def run():
    n, m = map(int, input().split())
    ans = 0
    for x in range(n, m+1):
        if check(str(x)):
            ans += 1
    print(ans)


while True:
    try:
        run()
    except:
        break
