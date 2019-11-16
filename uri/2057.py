a, b, c = map(int, input().split())
x = (a + b + c) % 24
if x < 0:
    x += 24
print(x)
