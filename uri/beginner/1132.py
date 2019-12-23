a = int(input())
b = int(input())
suma = 0
for x in range(min(a, b), max(a, b)+1):
    if x % 13 != 0:
        suma += x
print(suma)
