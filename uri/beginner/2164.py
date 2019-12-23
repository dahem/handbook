import math
n = float(input())
a = 5 ** 0.5
b = (1 + a) / 2
c = (1 - a) / 2
y = (b**n - c**n)/a

print("%.1f" % y)
