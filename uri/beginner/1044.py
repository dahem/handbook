d = [float(x) for x in input().split()]
d.sort()

if d[1] % d[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
