arr = []
while True:
    a = float(input())
    if a < 0:
        print("%.2f" % (sum(arr)/len(arr)))
        break
    arr.append(a)
