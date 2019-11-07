d = [float(x) for x in input().split()]
e = d.copy()
d.sort()

if d[0]+d[1] <= d[2]:
    print("Area = %0.1f" % ((e[0]+e[1]) * e[2] * 0.5))
else:
    print("Perimetro = %0.1f" % sum(d))
