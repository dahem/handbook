p, j1, j2, r, a = map(int, input().split())

s = j1+j2
win = None
if p == 1:
    if s % 2 == 0:
        win = 1
    else:
        win = 2
else:
    if s % 2 == 0:
        win = 2
    else:
        win = 1

if r == 1 and a == 0:
    win = 1

if r == 1 and a == 1:
    win = 2

if r == 0 and a == 1:
    win = 1

print("Jogador", win, "ganha!")
