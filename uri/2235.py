
arr = [int(x) for x in input().split()]

arr.sort()

[a, b, c] = arr
if a == b or b == c:
    print("S")
    exit()

if a + b == c:
    print("S")
    exit()
print("N")
