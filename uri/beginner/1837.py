import math
a, b = map(int, input().split())

x = a // b
y = a % b
if y >= 0:
  print(x, y)
else:
  print(x+1, abs(b)-abs(y))