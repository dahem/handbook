ah, am, bh, bm = map(int, input().split())
x = bh + 24 - ah

y = 0
if bm >= am:
    y = bm - am
else:
    x -= 1
    y = bm + 60 - am

if x > 24 or (x == 24 and y > 0):
    x %= 24

print("O JOGO DUROU", x, "HORA(S)", "E", y, "MINUTO(S)")
