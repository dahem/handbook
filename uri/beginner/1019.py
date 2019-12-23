n = int(input())

a = n // 3600
n = n % 3600
b = n // 60
n = n % 60
c = n

print("%d:%d:%d" % (a, b, c))
