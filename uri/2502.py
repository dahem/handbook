while True:
    try:
        a, b = map(int, input().split())
        m = input().lower()
        mm = input().lower()
        dic = {}
        for i in range(a):
            dic[m[i]] = mm[i]
            dic[mm[i]] = m[i]
        for i in range(b):
            s = input()
            sol = ''
            for y in s:
                if y.lower() in dic.keys():
                    if y.isupper():
                        sol += dic[y.lower()].upper()
                    else:
                        sol += dic[y.lower()]
                else:
                    sol += y
            print(sol)
        print("")

    except:
        break
