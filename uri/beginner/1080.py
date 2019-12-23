ind = 0
maxi = 0
for x in range(100):
    a = int(input())
    if a > maxi:
        maxi = a
        ind = x
print(maxi)
print(ind+1)
