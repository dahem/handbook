c = 0
s = 0
for x in range(6):
    a = float(input())
    if a >= 0:
        c += 1
        s += a

print(c, "valores positivos")
print("%.1f" % (s/c))
