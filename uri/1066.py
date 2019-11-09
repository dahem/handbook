c = 0
d = 0
e = 0
f = 0
for x in range(5):
    a = float(input())
    if a % 2 == 0:
        c += 1
    if a % 2 == 1:
        d += 1
    if a > 0:
        e += 1
    if a < 0:
        f += 1

print(c, "valor(es) par(es)")
print(d, "valor(es) impar(es)")
print(e, "valor(es) positivo(s)")
print(f, "valor(es) negativo(s)")
# print("%.1f" % (s/c))
