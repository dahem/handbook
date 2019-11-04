for i in range(0, 22, 2):
    di = float(i)/10.0
    for j in range(1, 4):
        if di.is_integer():
            print("I=%0.0f J=%0.0f" % (di, di+float(j)))
        else:
            print("I=%0.1f J=%0.1f" % (di, di+float(j)))
