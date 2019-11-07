a, b = map(float, input().split())

if a > 0 and b > 0:
    print("Q1")
    exit()

if a < 0 and b > 0:
    print("Q2")
    exit()

if a < 0 and b < 0:
    print("Q3")
    exit()

if a > 0 and b < 0:
    print("Q4")
    exit()

if a == 0 and b != 0:
    print("Eixo Y")
    exit()

if b == 0 and a != 0:
    print("Eixo X")
    exit()

print("Origem")
