n = int(input())
c = 0
for x in range(n):
    a = int(input())
    if a >= 10 and a <= 20:
        c += 1
print(c, "in")
print(n-c, "out")
