
n = int(input())
sol = 0.0
for i in range(n):
    c, p = map(float, input().split())
    sol += c/p
if sol <= 1.0:
    print("OK")
else:
    print("FAIL")
