cases = int(input())


def checkSudo(sudo):
    for i in range(9):
        if (len(set(sudo[i][:])) != 9):
            return False

    for i in range(9):
        col = []
        for j in range(9):
            col.append(sudo[j][i])
        if (len(set(col)) != 9):
            return False

    for i in range(9):
        square = []
        for j in range(3):
            for k in range(3):
                square.append(sudo[(i//3)*3+j][(i % 3)*3+k])

        if (len(set(square)) != 9):
            return False
    return True


for cas in range(cases):
    sudo = []
    for i in range(9):
        arr = [int(x) for x in input().split()]
        sudo.append(arr)
    print("Instancia %d" % (cas+1))
    if (checkSudo(sudo)):
        print("SIM")
    else:
        print("NAO")
    print("")
