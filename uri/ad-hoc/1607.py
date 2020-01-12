n = int(input())
for x in range(n):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(len(set(arr)))
