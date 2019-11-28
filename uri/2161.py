import math
n = float(input())


def raiz(step):
    if step == 0:
        return 0.0
    return 1.0 / (6.0 + raiz(step - 1))


print("%.10f" % (3.0 + raiz(n)))
