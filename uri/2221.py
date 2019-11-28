
cases = int(input())
for cas in range(cases):
    bonus = int(input())

    a1, b1, c1 = map(int, input().split())
    a2, b2, c2 = map(int, input().split())

    v1 = 0
    v2 = 0
    if c1 % 2 == 0:
        v1 = (a1 + b1) / 2 + bonus
    else:
        v1 = (a1 + b1) / 2
    if c2 % 2 == 0:
        v2 = (a2 + b2) / 2 + bonus
    else:
        v2 = (a2 + b2) / 2

    if v1 > v2:
        print("Dabriel")
    if v1 < v2:
        print("Guarte")
    if v1 == v2:
        print("Empate")
