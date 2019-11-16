n = int(input())
sol = ""
M = n // 1000
n %= 1000
if M > 0:
    sol += ("M" * M)

C = n // 100
n %= 100
if C > 0:
    if C == 9:
        sol += "CM"
    if C > 4 and C < 9:
        sol += "D" + ("C" * (C - 5))
    if C == 4:
        sol += "CD"
    if C < 4:
        sol += ("C" * C)

X = n // 10
n %= 10
if X > 0:
    if X == 9:
        sol += "XC"
    if X > 4 and X < 9:
        sol += "L" + ("X" * (X - 5))
    if X == 4:
        sol += "XL"
    if X < 4:
        sol += ("X" * X)

I = n
if I > 0:
    if I == 9:
        sol += "IX"
    if I > 4 and I < 9:
        sol += "V" + ("I" * (I - 5))
    if I == 4:
        sol += "IV"
    if I < 4:
        sol += ("I" * I)
print(sol)
