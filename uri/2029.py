while True:
    try:
        v = float(input())
        d = float(input())
        r = d / 2
        pi = 3.14
        a = pi * r * r
        h = v / a
        print("ALTURA = %.2f" % h)
        print("AREA = %.2f" % a)
    except:
        break
