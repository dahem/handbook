a = int(input())
op = input()
mat = [[float(input()) for y in range(12)] for x in range(12)]

if op == 'S':
    print("%0.1f" % sum(mat[a]))
else:
    print("%0.1f" % (sum(mat[a])/12.0))
