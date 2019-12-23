a = float(input())
b = a
c = 0
f = 0
if a >= 0 and a <= 400:
    b += a * 0.15
    c = a * 0.15
    f = 15
if a > 400 and a <= 800:
    b += a * 0.12
    c = a * 0.12
    f = 12

if a > 800 and a <= 1200:
    b += a * 0.10
    c = a * 0.10
    f = 10
if a > 1200 and a <= 2000:
    b += a * 0.07
    c = a * 0.07
    f = 7

if a > 2000:
    b += a * 0.04
    c = a * 0.04
    f = 4
print("Novo salario: %0.2f" % b)

print("Reajuste ganho: %0.2f" % c)


print("Em percentual:", f, "%")
