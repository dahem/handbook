ind = 1
while True:
    try:
        a = input()
        b = input()
        can = 0
        last = -1
        for i in range(len(b)):
            if len(a) + i <= len(b):
                x = b[i:i + len(a)]
                if x == a:
                    can += 1
                    last = i
        print("Caso #%d:" % ind)
        if can > 0:
            print("Qtd.Subsequencias: %d" % can)
            print("Pos: %d" % (last+1))
        else:
            print("Nao existe subsequencia")
        print("")
        ind += 1
    except:
        break
