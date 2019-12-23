import math
n = int(input())
for x in range(n):
    op = input()
    a, b, c = map(int, input().split())
    if op == 'min':
        print("Caso #%d: %d" % (x+1, min(a, b, c)))
    elif op == 'max':
        print("Caso #%d: %d" % (x+1, max(a, b, c)))
    elif op == 'mean':
        mean = (a+b+c)/3
        print("Caso #%d: %d" % (x+1, int(mean)))
    else:
        res = a*0.30 + b*0.59 + c*0.11
        print("Caso #%d: %d" % (x+1, int(res)))
