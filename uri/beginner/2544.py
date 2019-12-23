import math
while True:
    try:
        n = int(input())
        if n == 1:
            print(0)
        else:
            res = math.log2(n)
            print(int(res))
    except:
        break
