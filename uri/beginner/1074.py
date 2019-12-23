n = int(input().strip())
for x in range(n):
    a = int(input().strip())
    if a == 0:
        print("NULL")
        continue
    if a % 2 == 0:
        print("EVEN", end=" ")
    else:
        print("ODD", end=" ")
    if a < 0:
        print("NEGATIVE")
    else:
        print("POSITIVE")
