n = int(input())
for x in range(1, n+1):
    x, y = map(int, input().split())
    c = 0
    suma = 0
    while c < y:
        if x % 2 == 1:
            c += 1
            suma += x
        x += 1
    print(suma)
