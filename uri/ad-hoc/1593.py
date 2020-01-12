n = int(input())
for x in range(n):
    s = int(input())
    arr = list(bin(s))
    # print(arr)
    print(arr.count('1'))
