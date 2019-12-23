N = 110010
arr = [True] * N

a = 1
b = 1
arr[a] = False
while b < N:
    a, b = b, a + b
    if b >= N:
        break
    arr[b] = False

sol = []

for i in range(1, len(arr)):
    if arr[i]:
        sol.append(i)

x = int(input())

print(sol[x - 1])
