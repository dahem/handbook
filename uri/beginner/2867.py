while True:
    try:
        cases = int(input())
        mini = 20.0
        for x in range(cases):
            time = float(input())
            mini = min(time, mini)
        print("%.2f" % mini)
    except:
        break
