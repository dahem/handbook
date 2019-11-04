a, b, c = map(float, input().split())

d = [a, b, c]
d.sort(reverse=True)
[a, b, c] = d

if a >= b + c:
    print("NAO FORMA TRIANGULO")
    exit()
if a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")

if a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")

if a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
    exit()

if d[0] == d[1] or d[1] == d[2]:
    print("TRIANGULO ISOSCELES")
