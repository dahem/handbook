a, b, c = map(float, input().split())
a += 200
b += 200
c += 200
if a == b == c:
    print(":(")
    exit()
if (a + c) * 0.5 > b:
    print(":)")
elif (a + c) * 0.5 == b:
    if a > b > c:
        print(":(")
    else:
        print(":)")
else:
    print(":(")
