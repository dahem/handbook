
n = int(input())

arr = [0 for x in range(2001)]

for i in range(n):
    arr[int(input())] += 1

for x in range(len(arr)):
    if arr[x] != 0:
        print("%d aparece %d vez(es)" % (x, arr[x]))
