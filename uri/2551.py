import math
while True:
    try:
        n = int(input())
        a1, b1 = map(int, input().split())
        record = b1 / a1
        print(1)
        for i in range(n-1):
            a, b = map(int, input().split())
            if (b / a > record):
                print(i+2)
                record = b / a

    except:
        break
