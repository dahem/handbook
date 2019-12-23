import math

cases = int(input())
for x in range(cases):
    [pa, pb, g1, g2] = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    found = False
    for i in range(100):
        inc = math.floor(float(pa) * g1/100.0)
        inc2 = math.floor(float(pb) * g2/100.0)
        pa += inc
        pb += inc2
        if pa > pb:
            print(i+1, "anos.")
            found = True
            break
    if not found:
        print("Mais de 1 seculo.")
