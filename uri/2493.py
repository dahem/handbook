while True:
    try:
        t = int(input())
        arrop = []
        for x in range(t):
            op = input().split()
            a = int(op[0])
            op2 = op[1].split('=')
            b = int(op2[0])
            c = int(op2[1])
            arrop.append([a, b, c])
        sol = []
        for x in range(t):
            pl = input().split()
            [a, b, c] = arrop[int(pl[1])-1]
            if pl[2] == '-':
                if a - b != c:
                    sol.append(pl[0])
            if pl[2] == '+':
                if a + b != c:
                    sol.append(pl[0])
            if pl[2] == '*':
                if a * b != c:
                    sol.append(pl[0])
            if pl[2] == 'I':
                if a * b == c or a - b == c or a + b == c:
                    sol.append(pl[0])
        if len(sol) == 0:
            print("You Shall All Pass!")
            continue
        if len(sol) == t:
            print("None Shall Pass!")
            continue
        sol.sort()
        print(" ".join(sol))
    except:
        break
