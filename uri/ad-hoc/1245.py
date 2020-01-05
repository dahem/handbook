def run():
    n = int(input())
    dic = {}
    for x in range(n):
        a, b = map(str, input().split())
        a = int(a)
        if not a in dic:
            if b == 'D':
                dic[a] = [1, 0]
            else:
                dic[a] = [0, 1]
        else:
            if b == 'D':
                dic[a][0] += 1
            else:
                dic[a][1] += 1
    ans = 0
    for k, v in dic.items():
        ans += min(v)
    print(ans)


# run()
while True:
    try:
        run()
    except:
        break
