dLine = input().split()
da = int(dLine[1])
hLine = input().split()
ha = int(hLine[0])
ma = int(hLine[2])
sa = int(hLine[4])

dLine = input().split()
db = int(dLine[1])
hLine = input().split()
hb = int(hLine[0])
mb = int(hLine[2])
sb = int(hLine[4])


def tosecond(d, h, m, s):
    return d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s


def printSec(sec):
    d = sec // (24 * 60 * 60)
    sec %= (24 * 60 * 60)
    h = sec // (60 * 60)
    sec %= (60 * 60)

    m = sec // 60
    sec %= 60

    s = sec

    print(d, "dia(s)")
    print(h, "hora(s)")
    print(m, "minuto(s)")
    print(s, "segundo(s)")


printSec(tosecond(db, hb, mb, sb) - tosecond(da, ha, ma, sa))
