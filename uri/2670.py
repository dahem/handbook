
a = int(input())
b = int(input())
c = int(input())

arr = [a, b, c]

p1 = arr[1]*2 + arr[2]*2*2
p3 = arr[0]*2*2 + arr[1]*2
p2 = arr[0]*2 + arr[2]*2
print(min(p1, p2, p3))
