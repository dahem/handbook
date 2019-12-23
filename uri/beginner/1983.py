n = int(input())
c = 0
maxi = -1
stu = ''
for x in range(n):
    [a, b] = input().split()
    b = float(b)
    if b >= 8 and b > maxi:
        maxi = b
        stu = a

if maxi == -1:
    print("Minimum note not reached")
else:
    print(stu)
