
n, m = map(int, input().split())
#
arr1 = [int(x) for x in input().split()]
arr1.sort()

sol = [arr1[0]]
for x in range(1, n):
    sol.append(arr1[x] + sol[x-1])

for x in range(m, n):
    sol[x] += sol[x-m]
print(" ".join(map(str, sol)))
