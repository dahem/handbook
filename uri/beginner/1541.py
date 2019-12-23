import math
while True:
    s = input()
    if len(s) == 1:
        break
    a, b, c = map(float, s.split())
    res = a * b * (100.0 / c)
    print(math.floor(res ** 0.5))
