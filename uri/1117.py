x = None
while True:
    a = float(input())
    if a < 0 or a > 10:
        print("nota invalida")
        continue
    if x == None:
        x = a
        continue
    else:
        print("media = %.2f" % ((a+x)*0.5))
        break
