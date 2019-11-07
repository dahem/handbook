op = input()
mat = [[float(input()) for y in range(12)] for x in range(12)]

suma = 0.0
tot = 0.0
for x in range(12):
    for y in range(12):
        if x > y and x + y <= 10:
            suma += mat[x][y]
            tot += 1.0
if op == 'S':
    print("%0.1f" % suma)
else:
    print("%0.1f" % (suma / tot))
