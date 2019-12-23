#     e   f   m   a  m   j    j    a   s  o   n   d
ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    try:
        m, d = map(int, input().split())
        d1 = sum(ms[:m-1]) + d
        d2 = sum(ms[:12-1]) + 25
        r = d2 - d1
        if r == 0:
            print("E natal!")
            continue
        if r == 1:
            print("E vespera de natal!")
            continue
        if r < 0:
            print("Ja passou!")
            continue
        print("Faltam %d dias para o natal!" % r)
    except:
        break
