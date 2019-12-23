a = int(input())
b = int(input())
s = 0
for x in range(min(a, b)+1, max(a, b)):
    if x % 2 == 1:
        s += x
print(s)
