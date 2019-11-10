arr = []
for x in range(20):
    a = int(input())
    arr.append(a)
arr2 = arr[::-1]
for x in range(20):
    print("N[%d] = %d" % (x, arr2[x]))
