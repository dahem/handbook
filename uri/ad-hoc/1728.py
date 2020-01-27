while True:
    try:
        s = input().split('=')
        res = s[-1]
        res = res[::-1]
        [a, b] = s[0].split('+')
        a = a[::-1]
        b = b[::-1]
        print((int(a) + int(b)) == int(res))
    except:
        break
