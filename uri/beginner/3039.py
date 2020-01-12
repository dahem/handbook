n = int(input())
a = b = 0
for i in range(n):
    x, d = map(str, input().split())
    a += int(d == 'M')
    b += int(d == 'F')
print("%d carrinhos" % a)

print("%d bonecas" % b)
