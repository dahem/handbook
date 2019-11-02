n = int(input())
print(n)
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

print(int(a), "nota(s) de R$ 100,00")
print(int(b), "nota(s) de R$ 50,00")
print(int(c), "nota(s) de R$ 20,00")
print(int(d), "nota(s) de R$ 10,00")
print(int(e), "nota(s) de R$ 5,00")
print(int(f), "nota(s) de R$ 2,00")
print(int(g), "nota(s) de R$ 1,00")
