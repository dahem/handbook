
n = int(input())
for x in range(n):
    a = int(input())
    i = 2
    found = False
    while i*i <= a:
        if a % i == 0:
            print(a, "nao eh primo")
            found = True
            break
        i += 1
    if not found:
        print(a, "eh primo")
