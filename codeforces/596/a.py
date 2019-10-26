
import math
n, m = map(int, input().split())


def run():
    for x in range(100):
        for y in range(100):
            if(str(x)[0] == str(n) and str(y)[0] == str(m)):
                if(x + 1 == y):
                    print(x, y)
                    return
    return print(-1)


run()
