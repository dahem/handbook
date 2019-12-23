a, b = map(int, input().split())
x = b + 24 - a
if x > 24:
    x %= 24
print("O JOGO DUROU", x, "HORA(S)")
