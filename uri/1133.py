a = int(input())
b = int(input())
suma = 0
for x in range(min(a, b)+1, max(a, b)):
    if x % 5 == 2 or x % 5 == 3:
        print(x)
