n = int(input())
arr = [int(x) for x in input().split()]
x2 = 0
x3 = 0
x4 = 0
x5 = 0
for x in arr:
    if x % 2 == 0:
        x2 += 1

    if x % 3 == 0:
        x3 += 1

    if x % 4 == 0:
        x4 += 1

    if x % 5 == 0:
        x5 += 1

print(x2, "Multiplo(s) de 2")
print(x3, "Multiplo(s) de 3")
print(x4, "Multiplo(s) de 4")
print(x5, "Multiplo(s) de 5")
