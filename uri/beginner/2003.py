while True:
    try:
        h, m = map(int, input().split(':'))
        h += 1
        mm = h * 60 + m
        am = 8 * 60

        if mm - am <= 0:
            print("Atraso maximo: 0")
        else:
            print("Atraso maximo:", mm - am)
    except:
        break
