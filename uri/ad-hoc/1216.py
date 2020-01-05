tot = 0
ind = 0
while True:
    try:
        s = input()
        ind += 1
        n = int(input())
        tot += n
    except:
        print("%.1f" % (tot/ind))
        break
