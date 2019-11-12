a = int(input())
c = 0
for x in range(a, a + 1000):
    if x % 2 == 1:
        print(x)
        c += 1
    if c == 6:
        break
