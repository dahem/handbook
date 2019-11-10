sol = []
for x in range(10):
    a = int(input())
    if a <= 0:
        sol.append(1)
    else:
        sol.append(a)

for x in range(len(sol)):
    print("X[%d] = %d" % (x, sol[x]))
