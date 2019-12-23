arr = [2, 5, 10, 20, 50, 100]

pos = []

for x in range(6):
    for y in range(x+1, 6):
        pos.append(arr[x]+arr[y])
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    if m-n in pos:
        print("possible")
    else:
        print("impossible")
