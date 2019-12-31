from itertools import product
querty = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"


def getPos(s):
    [x, y] = s
    x = int(x) - 1
    y = ord(y) - ord('a')
    return [x, y]


def knight_moves(x, y):
    moves = list(product([x-1, x+1], [y-2, y+2])) + \
        list(product([x-2, x+2], [y-1, y+1]))
    moves = [[x, y] for x, y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    return moves


def pawnAtack(x, y):
    return [[x-1, y-1], [x-1, y+1]]


def check(a, b):
    return a[0] == b[0] and a[1] == b[1]


def run(ind):
    s = input()
    k = getPos(s)
    kmoves = knight_moves(k[0], k[1])
    p = []
    for i in range(8):
        ps = input()
        pa = getPos(ps)
        pac = pawnAtack(pa[0], pa[1])
        flag1 = False
        flag2 = False
        for x in p:
            if check(x, pac[0]):
                flag1 = True

            if check(x, pac[1]):
                flag2 = True
        if not flag1:
            p.append(pac[0])
        if not flag2:
            p.append(pac[1])

    ans = len(kmoves)
    # print(kmoves)
    # print("ans", ans)
    # print(p)
    for x in kmoves:
        for y in p:
            if check(x, y):
                ans -= 1
    print("Caso de Teste #%d: %d movimento(s)." % (ind, ans))


ind = 0
while True:
    try:
        ind += 1
        run(ind)
    except:
        break
