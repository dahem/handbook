
n, p = map(int, input().split())
# arr = [int(x) for x in input().split()]

for x in range(1, 40):
    if x >= bin(n - x*p).count('1') > 0 and n - p*x >= x:
        print(x)
        exit()
print(-1)
