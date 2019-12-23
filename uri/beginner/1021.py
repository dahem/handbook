import math
nf = float(input())
n = int(math.floor(nf))
rn = n
a = n // 100
n = n % 100
b = n // 50
n = n % 50
c = n // 20
n = n % 20
d = n // 10
n = n % 10
e = n // 5
n = n % 5
f = n // 2
n = n % 2
g = n

m = int((nf - rn) * 100.0)

g1 = m // 50
m = m % 50
g2 = m // 25
m = m % 25
g3 = m // 10
m = m % 10
g4 = m // 5
m = m % 5
g5 = m


print("NOTAS:")
print(int(a), "nota(s) de R$ 100.00")
print(int(b), "nota(s) de R$ 50.00")
print(int(c), "nota(s) de R$ 20.00")
print(int(d), "nota(s) de R$ 10.00")
print(int(e), "nota(s) de R$ 5.00")
print(int(f), "nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(g),  "moeda(s) de R$ 1.00")
print(int(g1), "moeda(s) de R$ 0.50")
print(int(g2), "moeda(s) de R$ 0.25")
print(int(g3), "moeda(s) de R$ 0.10")
print(int(g4), "moeda(s) de R$ 0.05")
print(int(g5), "moeda(s) de R$ 0.01")
