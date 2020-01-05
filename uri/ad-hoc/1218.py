def run(cas):
    n = input()
    arr = [x for x in input().split()]

    if cas != 1:
        print("")
    print("Caso %d:" % cas)
    f = 0
    m = 0
    for i in range(0, len(arr), 2):
        if n == arr[i]:
            if arr[i+1] == 'F':
                f += 1
            else:
                m += 1
    print("Pares Iguais: %d" % (f+m))
    print("F:", f)
    print("M:", m)


ind = 1
while True:
    try:
        run(ind)
        ind += 1
    except:
        break
